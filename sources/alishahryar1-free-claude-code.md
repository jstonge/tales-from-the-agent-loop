---
sourceUrl: https://github.com/Alishahryar1/free-claude-code
fetched: 2026-10-13
source: article text
---

*Independent open-source project. Not affiliated with or endorsed by Anthropic. Claude and Claude Code are trademarks of Anthropic.*

- **61 ToS-friendly providers. 1.3B+ free tokens every month.** Use free, paid, subscription, and local models from one searchable UI without putting your account at risk. FCC follows provider terms and removes integrations if they stop being allowed.
- **11 coding agents. One model catalog.** Run Claude Code, Codex, Pi, OpenCode, Cline, Hermes, DeepSeek Harness, Grok Build, Muse Code, Aider, or VS Code Chat with your FCC models.
- **Keep coding through provider outages.** After retries are exhausted, FCC automatically tries your next configured model without making you restart the turn. This works across every client.
- **Up to 90% lower token usage.** Optional RTK filters common command output, and Headroom compresses tool results. Five FCC optimizations handle quota probes, command-prefix detection, titles, suggestions, and filepaths without calling a provider.
- **Native Code sessions in your browser.** Choose a folder and run Codex in the browser with real-time and background support. Freely switch providers/models in the same session. Support for switching harnesses in the same session coming soon!
- **Terminal, desktop, IDE, or phone.** Work through native launchers, VS Code, Codex App, JetBrains, Discord, or Telegram.
- **Voice notes in. Code out.** Talk to your agent using local Whisper or NVIDIA NIM transcription.
- **Agent capabilities stay intact.** Stream responses, use tools, preserve native interleaved thinking for maximum performance, send images, and route Fable, Opus, Sonnet, and Haiku independently with compatible models.

Free-tier availability and limits are controlled by each provider and may change.

macOS/Linux:

`curl -fsSL "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.sh" | sh`
Windows PowerShell:

`& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.ps1")))`
When prompted, choose at least one coding agent and optionally enable RTK + Headroom token optimization for supported agents.

Open **Free Claude Code** from your desktop or Start menu.

Open **Free Claude Code** from your desktop or Applications folder.

Run:

`fcc-server`
FCC opens the Admin UI after starting. On Windows and macOS, use the tray or
menu-bar icon to open Admin, restart, or quit. When using `fcc-server`, keep its
terminal open.

1. Create an API key at build.nvidia.com/settings/api-keys.
2. Open the Admin UI URL from the server log.
3. Open NVIDIA NIM in **Providers**, click **Add key**, paste the key, and click **Save**.
4. Leave `MODEL` on the default `nvidia_nim/nvidia/nemotron-3-super-120b-a12b`, or search the model dropdown and select another model.
5. Click **Apply** to save your model selection.

To protect the local proxy with a bearer token, enable **Proxy Authentication**
in Admin.

Claude Code:

`fcc-claude`
Codex:

`fcc-codex`
Pi:

`fcc-pi`
OpenCode 2:

`fcc-opencode`
Cline:

`fcc-cline`
Hermes:

`fcc-hermes`
DeepSeek Harness Web:

`fcc-dsh`
Grok Build:

`fcc-grok`
Muse Code:

`fcc-muse`
Aider:

`fcc-aider`
1. Open a provider link below for its key, models, or setup instructions.
2. In the Admin UI, configure the listed setting. For OpenAI / ChatGPT
subscription access, use **Providers → OAuth providers** instead.
3. Search the `MODEL` dropdown and select a model. If the provider cannot list
models, enter `<provider-id>/<exact-provider-model-id>` manually.
4. Click **Apply**.

Optional: add an ordered **Fallback Models** list under **Model Config**. It
applies to every connected client. A failed request may reach and consume usage
from more than one provider before succeeding.

Provider modals support numbered API keys. Use **Add key**, remove rows, or drag their handles to reorder them. FCC uses key 1.

For another API endpoint, open **Providers → Custom providers → Add provider**. Enter its API base URL, optional keys, and API format. Leave **Model IDs** empty to discover models automatically, or enter one upstream model ID per line. Save, then select a model in **Model Config**.

## **Provider catalog**

| Provider | Admin UI setting | Example `MODEL` | 
|---|---|---|
| NVIDIA NIM | `NVIDIA_NIM_API_KEY` | `nvidia_nim/nvidia/nemotron-3-super-120b-a12b` | 
| OpenRouter | `OPENROUTER_API_KEY` | `open_router/openrouter/free` | 
| Groq | `GROQ_API_KEY` | `groq/llama-3.3-70b-versatile` | 
| ClinePass | `CLINE_API_KEY` | `cline_pass/cline-pass/kimi-k3` | 
| OpenAI / ChatGPT | Connect ChatGPT in the Admin UI | `openai/<model-id>` | 
| OpenAI API | `OPENAI_API_KEY` | `openai_api/gpt-5.6-sol` | 
| GitHub Copilot | Connect GitHub Copilot in the Admin UI | `github_copilot/<model-id>` | 
| xAI (Grok) | `XAI_API_KEY` | `xai/grok-4.5` | 
| Alibaba Cloud | `ALIBABA_CLOUD_API_KEY` | `alibaba_cloud/<model-id>` | 
| QwenCloud Token Plan | `QWENCLOUD_API_KEY` | `qwencloud/qwen3.7-plus` | 
| QwenCloud Coding Plan | `QWENCLOUD_CODING_API_KEY` | `qwencloud_coding/qwen3.7-plus` | 
| Together AI | `TOGETHER_API_KEY` | `together/zai-org/GLM-5.2` | 
| DeepInfra | `DEEPINFRA_API_KEY` | `deepinfra/deepseek-ai/DeepSeek-V4-Flash` | 
| SiliconFlow | `SILICONFLOW_API_KEY` | `siliconflow/Qwen/Qwen3-32B` | 
| Nebius Token Factory | `NEBIUS_API_KEY` | `nebius/Qwen/Qwen3-30B-A3B` | 
| Chutes | `CHUTES_API_KEY` | `chutes/Qwen/Qwen3-32B-TEE` | 
| Featherless AI | `FEATHERLESS_API_KEY` | `featherless/Qwen/Qwen3-32B` | 
| Agnes AI | `AGNES_API_KEY` | `agnes/agnes-2.0-flash` | 
| ZenMux | `ZENMUX_API_KEY` | `zenmux/deepseek/deepseek-v4-flash-free` | 
| W&B Inference | `WANDB_API_KEY` | `wandb/openai/gpt-oss-20b` | 
| Anthropic | `ANTHROPIC_API_KEY` | `anthropic/<model-id>` | 
| Azure OpenAI | `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_BASE_URL` | `azure_openai/<deployment-name>` | 
| Google AI Studio (Gemini) | `GEMINI_API_KEY` | `gemini/models/gemini-3.1-flash-lite` | 
| Google Vertex AI | `VERTEX_PROJECT_ID` + ADC | `vertex/google/gemini-3.5-flash` | 
| DeepSeek | `DEEPSEEK_API_KEY` | `deepseek/deepseek-chat` | 
| Mistral La Plateforme | `MISTRAL_API_KEY` | `mistral/devstral-small-latest` | 
| Mistral Codestral | `CODESTRAL_API_KEY` | `mistral_codestral/codestral-latest` | 
| OpenCode Zen | `OPENCODE_API_KEY` | `opencode_zen/gpt-5.3-codex` | 
| OpenCode Go | `OPENCODE_API_KEY` | `opencode_go/minimax-m2.7` | 
| Vercel AI Gateway | `AI_GATEWAY_API_KEY` | `vercel/openai/gpt-5.5` | 
| Amazon Bedrock | `AWS_BEARER_TOKEN_BEDROCK` | `bedrock/openai.gpt-oss-120b` | 
| Hugging Face Inference Providers | `HUGGINGFACE_API_KEY` | `huggingface/Qwen/Qwen3-Coder-480B-A35B-Instruct:fastest` | 
| Cohere | `COHERE_API_KEY` | `cohere/command-a-plus-05-2026` | 
| Wafer | `WAFER_API_KEY` | `wafer/DeepSeek-V4-Pro` | 
| Kimi API | `KIMI_API_KEY` | `kimi/kimi-k2.5` | 
| Kimi Code | `KIMI_CODE_API_KEY` | `kimi_code/k3` | 
| MiniMax | `MINIMAX_API_KEY` | `minimax/MiniMax-M3` | 
| Cerebras Inference | `CEREBRAS_API_KEY` | `cerebras/gpt-oss-120b` | 
| SambaNova | `SAMBANOVA_API_KEY` | `sambanova/Meta-Llama-3.3-70B-Instruct` | 
| Kilo.ai | `KILO_API_KEY` | `kilo/kilo-auto/free` | 
| Fireworks AI | `FIREWORKS_API_KEY` | `fireworks/accounts/fireworks/models/llama-v3p3-70b-instruct` | 
| Novita AI | `NOVITA_API_KEY` | `novita/deepseek/deepseek-v4-flash-0731` | 
| Cloudflare Workers AI | `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` | `cloudflare/@cf/moonshotai/kimi-k2.6` | 
| Z.ai Coding Plan | `ZAI_API_KEY` | `zai/glm-5.2` | 
| Z.ai API (pay as you go) | `ZAI_API_KEY` | `zai_api/glm-4.7-flash` | 
| TokenRouter | `TOKENROUTER_API_KEY` | `tokenrouter/moonshotai/kimi-k3-free` | 
| NaraRoute | `NARAROUTE_API_KEY` | `nararoute/kimi-k3-free` | 
| Poolside AI | `POOLSIDE_API_KEY` | `poolside/poolside/laguna-s-2.1` | 
| LLM7.io | `LLM7_API_KEY` | `llm7/default` | 
| Scaleway | `SCW_SECRET_KEY` | `scaleway/deepseek/deepseek-v4-flash` | 
| Lightning AI | `LIGHTNING_API_KEY` | `lightning/lightning-ai/Qwen3.8-27B` | 
| Experiential Labs | `EXPLABS_API_KEY` | `experiential/union-alpha` | 
| Cheaper Inference | `CHEAPER_INFERENCE_API_KEY` | `cheaperinference/gpt-5.4-mini` | 
| OrcaRouter | `ORCAROUTER_API_KEY` | `orcarouter/deepseek/deepseek-v4-flash-free` | 
| Atlas Cloud | `ATLASCLOUD_API_KEY` | `atlascloud/deepseek-ai/deepseek-v4-flash` | 
| xKiro | `XKIRO_API_KEY` | `xkiro/qwen/qwen3.7-flash:free` | 
| Opper | `OPPER_API_KEY` | `opper/claude-sonnet-4-6` | 
| Ollama Cloud | `OLLAMA_API_KEY` | `ollama_cloud/qwen3-coder:480b` | 
| LM Studio | `LM_STUDIO_BASE_URL` | `lmstudio/<model-id>` | 
| llama.cpp | `LLAMACPP_BASE_URL` | `llamacpp/<model-id>` | 
| Ollama | `OLLAMA_BASE_URL` | `ollama/<model-tag>` | 

## **Provider-specific setup**

- OpenAI / ChatGPT uses your ChatGPT subscription rather than an API key. Connect from
**Providers → OAuth providers → OpenAI / ChatGPT → Connect** in the Admin UI
and finish signing in through your browser. Restart an already-running agent after connecting.
- Anthropic uses a separately billed API key. Add it under
**Providers → Cloud providers → Anthropic → Configure**, then choose a discovered
model. Multi-workspace keys also require `ANTHROPIC_WORKSPACE_ID`.
- OpenAI API uses a separate Platform API key. Enter it under
**Providers → Cloud providers → OpenAI API → Configure**. The model list may
include IDs that cannot handle coding requests. Choose a text-generation model.
- GitHub Copilot uses your signed-in GitHub account and subscription. Install
Copilot CLI 1.0.83
on PATH, then choose **Providers → OAuth providers → GitHub Copilot → Connect**.
Finish signing in, then select a `github_copilot/<model-id>` from the model picker.
Available models and quotas depend on your subscription and organization policies.
Restart an already-running agent after connecting.
- Azure OpenAI uses the deployment names from your resource. Set
`AZURE_OPENAI_BASE_URL` to its complete v1 endpoint, such as `https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/`, and select a
deployment that supports Chat Completions. Enter the deployment name as a
custom model slug if it does not appear in the model dropdown.
- Mistral Codestral uses a separate key from Mistral La Plateforme.
- Kimi Code subscription keys use `kimi_code/`. Kimi API credit keys use `kimi/`. Kimi Code plans are for personal interactive coding-agent use under
Kimi's community guidelines.
- Alibaba Cloud uses a Model Studio pay-as-you-go key and defaults to Singapore.
For another region or workspace, set `ALIBABA_CLOUD_BASE_URL` to its
OpenAI-compatible endpoint
ending in `/compatible-mode/v1`. The key and endpoint must use the same region.
- QwenCloud Coding Plan keys use `qwencloud_coding/`. QwenCloud Token Plan keys
use `qwencloud/`. The keys and endpoints are not interchangeable. Coding Plan
is for local, personal, interactive coding-agent use under the
Coding Plan terms.
- OpenCode Zen and OpenCode Go share `OPENCODE_API_KEY` but use the explicit `opencode_zen/` and `opencode_go/` model prefixes.
- For Amazon Bedrock, set `BEDROCK_BASE_URL` to the URL for the same region as
the API key and select one of the listed models.
- Vertex AI uses Google Application Default Credentials instead of an API key.
Locally, run `gcloud auth application-default login` once. Service-account
files and attached service accounts also work. Set `VERTEX_PROJECT_ID`, and
optionally change `VERTEX_LOCATION` from its `global` default.
- Cloudflare requires both its API token and account ID.
- For Ollama Cloud, use the exact model IDs shown in the model picker. Local
Ollama uses the separate `ollama/` prefix.
- Prefer tool-capable models for coding agents. Local models also need enough context for the agent's system prompt and tool definitions.

## **Local provider setup**

Start LM Studio's local server, load a tool-capable model, and use the model identifier shown by LM Studio with the `lmstudio/` prefix. The default URL is `http://localhost:1234/v1`.

Start `llama-server` with its OpenAI-compatible Chat Completions API and enough context for the model. Use the local model ID with the `llamacpp/` prefix. `LLAMACPP_BASE_URL` defaults to `http://localhost:8080/v1`.

```
ollama pull llama3.1
ollama serve
```
Use the tag shown by `ollama list` with the `ollama/` prefix. `OLLAMA_BASE_URL` defaults to `http://localhost:11434`.

## **Optional model-tier routing**

`MODEL` is the fallback for every request. Select a model for `MODEL_FABLE`, `MODEL_OPUS`, `MODEL_SONNET`, or `MODEL_HAIKU` to override an individual Claude Code tier. Select **None** to use `MODEL`.

In **Admin UI → Model Config**, add **Fallback Models** in the order FCC should try them if the selected model fails. Each fallback has its own reasoning effort: **Inherit**, **Off**, **From client**, **Low**, **Medium**, **High**, **X-High**, or **Max**.

Choose a model, effort, and API key number in the bottom row, then click **+**. **Key 1**, **Key 2**, and so on refer to the current numbered keys in that provider's settings. Edit the selections in place, drag the handle to change the order, or click the red trash button to remove a fallback.

**Inherit** keeps the original request's resolved reasoning setting. **From client** uses the effort or token budget sent by your coding agent, bypassing the global or tier setting. You can select the same model with another key number.

## **Reasoning control**

Open **Admin UI → Model Config → Model Routing** and choose an effort beside each model. **Default Effort** starts at **From client**. Fable, Opus, Sonnet, and Haiku start at **Inherit**.

| Selection | Behavior | 
|---|---|
| **From client** | Use the effort sent by your coding agent. If none is sent, keep the provider default. | 
| **Off** | Request reasoning to be disabled. | 
| **Low**, **Medium**, **High**, **X-High**, or **Max** | Override the client with the selected reasoning level. | 
| **Inherit** | Tier overrides use Default Effort. Fallbacks keep the original request's resolved effort. | 

FCC launchers automatically start the server.

For editor and app integrations, install the client, start FCC, then open
**Admin UI → Integrations** and click **Connect** on its card.

- **Claude Code in VS Code**: Install the Claude Code extension.
- **VS Code Chat**: Install the latest VS Code, connect, and select an FCC model in its built-in Chat model picker.
- **Claude Desktop**: Install Claude Desktop. Fully quit it before connecting or disconnecting, then reopen it. Disconnect returns to normal Claude sign-in.
- **Codex in VS Code and App**: Install the Codex extension or Codex App.
- **DeepSeek Harness Desktop**: Install and open the app once before connecting. Start a new session to use FCC models.
- **Claude Code in JetBrains ACP**: Install Claude Agent in JetBrains AI Assistant and start it once, then click **Connect** in FCC. Reopen the IDE, select **Claude Code (FCC)**, and start a new chat. After JetBrains updates the agent, restart FCC before starting a new chat. Requires a local IDE in its standard installation locations.

Reload VS Code or restart the app/IDE after connecting. In Codex and Claude Desktop, select an FCC
model from the model picker. Reload or restart the client when FCC reports updated settings. Use
**Disconnect** on the same card to remove the integration.

To complete Claude Code onboarding separately, open **Admin UI → Integrations →
Claude Code onboarding** and click **Complete onboarding**. Connecting Claude Code
in VS Code also completes onboarding.

Run FCC on the same computer and in the same user environment as the client you are configuring.

Configure integrations from **Admin UI → Messaging**, then click **Apply**.

## **Discord bot**

1. Create a bot in the Discord Developer Portal.
2. Enable **Message Content Intent** and invite it with read, send,
message-history, and **Manage Messages** permissions so `/clear` can remove
user prompts.
3. Set **Messaging Platform** to **discord**.
4. Enter **Discord Bot Token**, **Allowed Discord Channels**, and an absolute **Allowed Directory**.
5. Apply the settings and restart the server if requested.

## **Telegram bot**

1. Create a bot with @BotFather.
2. Get your numeric user ID from @userinfobot. In groups, grant the bot permission to delete messages.
3. Set **Messaging Platform** to **telegram**.
4. Enter **Telegram Bot Token**, **Allowed Telegram User ID**, and an absolute **Allowed Directory**.
5. Apply the settings and restart the server if requested.

| Usage | Behavior | 
|---|---|
| `/stats` | Show session state. | 
| Standalone `/stop` | Cancel all work. | 
| Reply with `/stop` | Cancel only the selected request while other queued requests continue. | 
| Standalone `/clear` | Clear all FCC conversations and their messages in this chat. | 
| Reply with `/clear` | Delete the selected message and the chain of replies to it. Keep other conversations. | 

## **Voice notes**

NVIDIA NIM transcription support is included in every installation. In **Admin UI → Messaging → Voice**, enable voice notes, select `nvidia_nim`, and choose a supported model. Configure your **NVIDIA NIM API key** on the Providers page.

For local Whisper on CPU or CUDA, re-run the installer with the local voice option:

macOS/Linux:

Local Whisper on CPU or CUDA:

`curl -fsSL "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.sh" | sh -s -- --voice-local`
Local Whisper with CUDA 13.0:

`curl -fsSL "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.sh" | sh -s -- --voice-local --torch-backend cu130`
Windows PowerShell:

Local Whisper on CPU or CUDA:

`& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.ps1"))) -VoiceLocal`
Local Whisper with CUDA 13.0:

`& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install.ps1"))) -VoiceLocal -TorchBackend cu130`
After installing local support, restart `fcc-server`. In **Admin UI → Messaging → Voice**, enable voice notes, select `cpu` or `cuda`, and choose the Whisper model. Local gated models need `HUGGINGFACE_API_KEY`.

Run `fcc-server --version` to check the installed version without starting FCC.

Stop all running FCC commands, then run:

`fcc-update`
To reinstall FCC or change optional components while already up to date, run the installer directly.

For local voice support, include `--voice-local` (macOS/Linux) or `-VoiceLocal` (Windows), plus your `--torch-backend` or `-TorchBackend` option if used.

To install or update only Muse Code:

`& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/install-muse.ps1")))`
To remove the Muse Code copy installed by FCC, keeping its data:

`& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/uninstall-muse.ps1")))`
Uninstalling FCC leaves Muse Code installed.

Stop every running FCC command before uninstalling.

**Removes**

- Free Claude Code, including its desktop launcher and commands
- `~/.fcc/`

**Keeps**

- uv and Python
- Your coding agents, RTK, and Headroom

macOS/Linux:

`curl -fsSL "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/uninstall.sh" | sh`
Windows PowerShell:

`& ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Alishahryar1/free-claude-code/main/scripts/uninstall.ps1")))`
For a problem after installation, run the command below and paste its output into your bug report.

`fcc-doctor`
GNU Affero General Public License version 3 only (`AGPL-3.0-only`). See LICENSE for details.
