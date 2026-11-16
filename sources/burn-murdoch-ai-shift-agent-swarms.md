---
sourceUrl: https://www.ft.com/content/1cc2516d-b718-4e2c-a3b2-1f8bd8acce01
fetched: 2026-10-29
source: pasted text, shared via the FT gift-article link (FT returns 403 to the archiver)
---

# The AI Shift: agents at the FT

*Welcome back to The AI Shift, our weekly exploration of how models and agents
are disrupting work and jobs. We've been writing this newsletter for a year
now, and during that time a huge amount has changed in terms of both AI's
capabilities and its emerging impacts on work. Usually we turn our gaze outward
to look into impacts on particular sectors or the broader labour market, but
this week we wanted to flip that and give you a sense of how AI agents are
changing the way we do our jobs at the FT.*

*Sarah is away this week so I'm delighted to be joined by my colleague Clara
Murray, a fellow data reporter and fellow increasingly-heavy-user of AI tools.
Clara, do you want to kick things off?*

## Clara writes

I've been something of an AI sceptic for a while: I've written about how
inadequate many AI tools for email are, for example, and how most AI-generated
disinformation doesn't appear to be effective. So I was happy restricting my
own use to copy and pasting code error messages back and forth with a chatbot.
Anything more was lazy, or just hype, I thought.

But more and more software developer friends and FT colleagues told me that,
thanks to tools such as Codex, OpenAI's agentic platform, they had barely
written a line of code in months. I had to try it myself.

My first week with Codex was a test: could it do my job? I had two large data
projects to throw at it. One involved scraping product prices from websites in
multiple languages, the other building an interactive calculator from millions
of data points.

I gave Codex access to the project folders, sent a few prompts and was up and
running. It was immediately different to working with a chatbot. There is
little back-and-forth or insight into what exactly is going on. You just have
an idea, direct your agent and wait.

By midweek, I had magicked up a whizzy calculator prototype — without a
designer or developer — and prices for thousands of products. I'd grown
confident enough to set dozens of agents working in parallel, seeking to speed
up the work even more.

But I was definitely not working less. Feeling unable to leave my agents
unattended, I was glued to my screen late into the evening as they spat out
line after line of code and requests for attention. My laptop crashed at one
point, unable to cope with the volume.

Come Friday morning, I realised that the pricing data, which on small test runs
looked perfect, contained major flaws. One agent had guessed product prices by
taking the biggest number it found on the webpage. Another got muddled by items
available in different colours.

Meanwhile, because I had not looked at the inputs in detail, I had no idea
whether the numbers the calculator returned were correct. It was not something
I could put in front of FT readers (or the legal departments of the companies
it named).

I'm not the only one finding agents can make work harder, not easier. The
strain of constant task-switching and keeping track of multiple workstreams has
been a growing theme in the debate over AI at work. Princeton professor Arvind
Narayanan recently described overseeing agents as combining all the worst parts
of being a manager (more stress, taking responsibility for others' mistakes)
without the good bits (more money!).

For data journalists, where accuracy is everything, the stakes are high. Agents
can make the part of our jobs that involves building things dramatically
faster. But data analysis is, like writing, a way of thinking: you need to
understand the numbers to draw conclusions that can be trusted. The busy work
of overseeing dozens of AI bots is, it turns out, not a great way to understand
things.

So while I'm still using Codex, it's with much more awareness of its (and my)
limits. John, you've been managing agent swarms a little longer than I have —
where have you been getting the most (and least) value out of them?

## John writes

Thanks for pulling back the curtain on all of that, Clara. I suspect your
experience will ring true for a lot of our readers who have dipped their toes
into agentic AI tools over recent months — the initial 'wow' moment, the rapid
realisation that agents' voluminous output requires voluminous verification,
and the quiet shift to becoming a manager whose team is eager for feedback or
new assignments around the clock.

I certainly had some similar early experiences. In one project where I deployed
agents at scale (to help me score different political regimes on measures of
democratic backsliding), I had to spend a huge amount of time verifying all the
research that came back. One thing that emerged from that process was my
development of an AI skill that I call 'adversarial audit', where I tell another
AI model to scour everything I've done for factual errors, and to assume there
will be some. This can obviously never fully replace human fact-checking, but
in performing a first pass of error identification and correction, it slims
down what then needs to be checked manually.

But even when I do find myself spending a full day or more on verification, I'm
still now often taking on analysis projects that would simply not have been
possible before agentic AI — my own personal Jevons paradox, as it were — such
as collating city-level housebuilding statistics from dozens of countries and
datasets. Slimming down the verification process in that project meant building
in an audit trail as I went, so that every final data point was accompanied by
a source URL where I could manually check the original raw data, definitions
and provenance with a couple of clicks at most.

When it comes to agentic data analysis, I've found a couple of additional
things useful. One is to begin any project by replicating existing research (or
my own pre-AI work) that uses the same dataset, to ensure everything is working
as it should. I also have AI run both methodological and technical audits to
make sure I've made reasonable choices in my analysis and that all the
calculations are correct. And where some AI-written code throws up a
particularly startling result (such as my finding that on an average day one in
ten young Americans has zero interactions with other people), I don't just
check that the AI-generated code was correct, I open up a new file and write my
own version of the analysis from scratch to make sure I get the same result.

I've also recently begun automating more of my chart-making workflow, but the
two things that are critical in good chart design — the title, and the colours
used for the different series — are determined from the ground up by me. I
don't even allow AI to make suggestions on either of those for me to edit, 100
per cent comes proactively from me. In Narayanan and Kapoor's
decide-execute-deliver parlance, before AI I conceived of a chart, built the
chart, and refined the chart. Now I just do the concept and refining while AI
handles the building. I make a lot of charts, so this alone can save me a
couple of hours per week that I can now devote to higher-value tasks.

And I'm completely with you on protecting independent thinking at all costs.
Quite aside from our editorial code of conduct (every word you read in the FT
should have been conceived of and written by the human author, not by AI), I'm
a firm believer that writing is thinking. I sometimes spend 45 minutes writing
a single paragraph, but the idea contained in that paragraph didn't exist in my
head until I spent those 45 minutes formulating it on the page.

Overall I would say my overarching approach has been to draw a clear line
between routine, mechanical, easily verifiable work where automation provides a
big benefit without subtracting any of the value I provide as an analyst,
writer or designer — and the creative, thoughtful and analytical parts where I
want every idea, every word and every pixel to be mine. I'm sure the specific
ways I use AI will be quite different a year from now, but that dividing line
will remain.
