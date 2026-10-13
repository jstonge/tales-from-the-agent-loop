---
sourceUrl: https://tidydesign.substack.com/p/a-coding-agent-is-six-functions-in
fetched: 2026-10-13
---

Coding agents like Claude Code, Cursor, and Codex have taken the software engineering field by storm. Since November 2025 they have radically changed the practice of software development for many programmers (including me), and in this week’s post I want to dive into what makes them tick.

We’ve now talked about tools (functions) and harnesses (a system for running tools on behalf of the LLM). And you know that an agent is a harness with tools for reading and writing. So what makes an agent a **coding** agent? The answer is the specific tools that it supplies: ones that let an LLM explore and edit a codebase the same way a human would.

Most coding agents provide some variation on the following tools:

- **Read file**: read the contents of a file, or a subset of one.
- **Write file**: create a new file with fresh content.
- **Edit file**: make a targeted change to an existing file, usually by replacing one chunk of text with another.
- **List files**: show the files and directories at a given path so the agent can orient itself in the project structure.
- **Search**: find lines matching a pattern across the codebase so the agent can locate relevant code quickly.
- **Run command**: execute an arbitrary shell command, which allows the agent to do anything else it might need.

A good coding agent also usually contains a big prompt with advice about good practices. While these prompts are not open source, they are fairly easy to sniff out, so various folks have extracted them. It’s informative to take a look just to get a sense of how complex they are.

## **Building a minimal coding agent**

Of the six tools above, only three are really essential for a basic coding agent. To prove it, I’m going to build a tiny coding agent in R with ellmer. We’ll start ruthlessly minimal — with just read file, write file, and run command — and then work our way up. We’ll lose some niceties, but in exchange we get something you can read in one sitting.

First, the three tool functions. I’ve written them with deliberately boring R:

```
read_file <- function(path) {
  paste(readLines(path), collapse = "\n")
}
write_file <- function(path, content) {
  writeLines(content, path)
  paste0("Wrote ", path, ".")
}
run_command <- function(command) {
  paste(system(command, intern = TRUE), collapse = "\n")
}
```
Each function returns a string which is fed back to the LLM as the result of the tool call: `read_file` returns the file’s contents, `write_file` confirms what it did, and `run_command` returns whatever the command printed to the console.

Next we create a chat and register the three functions as tools. As before, the descriptions matter: they tell the LLM when and how to reach for each tool. We also include a very basic prompt.

```
library(ellmer)
#> Warning: replacing previous import 'S7:::=' by 'rlang:::=' when loading
#> 'ellmer'
chat <- chat_anthropic(
  system_prompt = "
    You are a coding assistant working in the user's current directory.
    Use the tools to explore and modify their project. Before editing a
    file, read it first. After making changes, run any relevant tests or
    checks to confirm your work. Keep going until the task is done.
  "
)
#> Using model = "claude-sonnet-4-5-20250929".
chat$register_tool(tool(
  read_file,
  description = "Read the entire contents of a text file.",
  arguments = list(
    path = type_string("Path to the file, relative to the working directory.")
  )
))
chat$register_tool(tool(
  write_file,
  description = "Write content to a file, overwriting it if it already exists.
    Always read the file first if you only want to change part of it.",
  arguments = list(
    path = type_string("Path to the file, relative to the working directory."),
    content = type_string("The full new contents of the file.")
  )
))
chat$register_tool(tool(
  run_command,
  description = "Run a shell command and return its output. Use this to list
    files (ls), search code (grep), run tests, or use git.",
  arguments = list(
    command = type_string("The shell command to run.")
  )
))
```
And that’s the whole agent!

The shell tool is our “get out of jail free” card because if you can run a shell command you can do anything: you can call `ls` to list directories, `grep` to search for code, `Rscript` to run R code, and `git` for git. (Technically we don’t even need read and write tools because the agent could use `echo` and `cat`, but we’re going to throw the agent a bone here.) The shell tool is also rather dangerous; we’ll come back to that later.

You can now use this agent for a simple task:

`chat$chat("Find the function that parses dates and add a unit test for it.")`
Behind the scenes the model might use `run_command` to `grep` for the function then `read_file` to study it. Next, to create the test, it will need to read the existing test files with `read_file`, then `write_file` to add the new test, and finish up by using `run_command` to run the test suite. It’s no Claude Code, but it’s in the same galaxy.

## **Finding files: list and search**

Our minimal agent can already list and search files via `run_command`, but leaning on the shell for everything has downsides. Shell commands vary between platforms (Windows doesn’t have `ls` or `grep`) and their output is noisy. More importantly, handing the model a general-purpose shell is a security nightmare: it’s very difficult to tell if a specific shell command is safe or dangerous. It’s much easier to add safeguards to stricter tools.

Let’s see what that might look like by implementing list and search tools, then seeing how we could make them safer.

```
list_files <- function(path = ".") {
  paste(list.files(path), collapse = "\n")
}
search_files <- function(pattern, path = ".") {
  files <- list.files(path, recursive = TRUE, full.names = TRUE)
  hits <- character()
  for (file in files) {
    lines <- readLines(file, warn = FALSE)
    matches <- grep(pattern, lines)
    hits <- c(hits, paste0(file, ":", matches, ": ", lines[matches]))
  }
  paste(hits, collapse = "\n")
}
```
And then add them to our harness:

```
chat$register_tool(tool(
  list_files,
  description = "List the files and directories at a given path.",
  arguments = list(
    path = type_string("Directory to list. Defaults to the working directory.")
  )
))
chat$register_tool(tool(
  search_files,
  description = "Search the contents of all files for a regular expression,
    returning matching lines as 'path:line: text'.",
  arguments = list(
    pattern = type_string("A regular expression to search for."),
    path = type_string("Directory to search. Defaults to the working directory.")
  )
))
```
## **Keeping it safe**

These list and search tools are easier to make safe than a general shell, because they have simpler inputs. But they’re not automatically safe: there’s nothing stopping the model passing `path = ".."` or an absolute path like `/etc`, so our “search the project” tool could happily read your entire hard drive, including your passwords.

Let’s make them safer by checking that paths stay within the project directory. We resolve the path (which collapses `..` and follows symlinks) and check that it still sits underneath the working directory:

```
safe_path <- function(path) {
  root <- normalizePath(".", winslash = "/", mustWork = TRUE)
  full <- normalizePath(path, winslash = "/", mustWork = FALSE)
  within_root <- full == root || startsWith(full, paste0(root, "/"))
  if (!within_root) {
    stop("Path is outside the project directory: ", path)
  }
  path
}
```
It’s also worth verifying that they can’t read the `.Renviron` file, where R programmers conventionally stash API keys and other secrets. Luckily we get that for free: `list.files()` defaults to `all.files = FALSE`, which skips dotfiles, so `.Renviron`, `.Rhistory`, and the contents of `.git/` are already excluded from our search.

Putting both together, `search_files` becomes:

```
search_files <- function(pattern, path = ".") {
  files <- list.files(safe_path(path), recursive = TRUE, full.names = TRUE)
  hits <- character()
  for (file in files) {
    lines <- readLines(file, warn = FALSE)
    matches <- grep(pattern, lines)
    hits <- c(hits, paste0(file, ":", matches, ": ", lines[matches]))
  }
  paste(hits, collapse = "\n")
}
```
The same `safe_path()` wrapper belongs on `read_file`, `write_file`, and `list_files` too; otherwise the model can still reach outside the project by reading or writing a file directly.

## **Making it efficient**

The biggest weakness of our minimal agent is that the only way to change a file is to rewrite it from scratch with `write_file`. For a 500-line file where you want to change one line, that means the model has to reproduce all 500 lines perfectly — slow, expensive, and challenging for today’s models. The fix is a targeted edit tool that swaps one chunk of text for another:

```
edit_file <- function(path, old, new) {
  path <- safe_path(path)
  content <- paste(readLines(path), collapse = "\n")
  if (!grepl(old, content, fixed = TRUE)) {
    stop("Could not find the text to replace in ", path, ".")
  }
  content <- sub(old, new, content, fixed = TRUE)
  writeLines(content, path)
  paste0("Edited ", path, ".")
}
```
```
chat$register_tool(tool(
  edit_file,
  description = "Replace an exact span of text in a file with new text. The
    'old' text must appear exactly once in the file. Prefer this over
    write_file for changing part of an existing file.",
  arguments = list(
    path = type_string("Path to the file to edit."),
    old = type_string("The exact existing text to replace."),
    new = type_string("The text to replace it with.")
  )
))
```
This is useful for two reasons. First, the model only has to write the few lines that change, not the whole file, so it’s both faster and cheaper. Second, it’s much safer: because the `old` text has to match exactly, a botched edit fails loudly instead of silently corrupting the file. This is exactly how the edit tools in real coding agents work, give or take some cleverness with whitespace, safeguards against multiple matches, and detecting when a human is also editing the file.

Next we’ll we come back to the topic of security in more detail, and explore the approaches you can use to make general tools (like running a shell command) as safe as possible.
