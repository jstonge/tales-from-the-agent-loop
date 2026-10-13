---
sourceUrl: https://github.com/deepseek-ai/deepseek-harness
fetched: 2026-10-13
source: article text
---

English | 中文

DeepSeek Harness (`dsh`) is an open-source agent harness developed by DeepSeek AI.

It is built on an **everything-is-a-plugin** architecture and powered by Cordis, whose design is described in *A Programming Paradigm for Spatiotemporal Composability*.

Documentation: https://deepseek-harness.github.io/deepseek-harness/

DeepSeek Harness is in *developer preview* and iterating rapidly. **THERE WILL BE COMPATIBILITY-BREAKING CHANGES.**

Review the safety notice before running the project.

Install `Node.js`, then run:

`npx @deepseek-ai/dsh web`
The command starts the Web UI at `http://127.0.0.1:3080` by default and opens it in the default browser for a local launch. An SSH launch only prints the host URL because the SSH client or editor owns the local forwarded address. Pass `--no-open` to run the server without opening a browser. See Web UI guide.

To run from a repository checkout:

```
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```
`pnpm run build` prepares the repository artifacts. `pnpm dsh web` uses those built artifacts without rebuilding.

- Submit feedback or bug reports through GitHub Discussions.
- Add the `dsh-plugin` topic to your plugin repository for discoverability.
- Join DeepSeek Harness Discord community.

See CONTRIBUTING.md.

Start with the development guide and architecture documentation.

`pnpm run dev:web` builds, serves, and rebuilds client bundles on source edits in one terminal, and `make help` lists the matching Make targets for Web and Desktop; the guide's application commands section owns the full table.

For agents, follow AGENTS.md.

```
@misc{deepseek-harness2026,
  title={DeepSeek Harness: Everything is a Plugin},
  author={DeepSeek-AI},
  year={2026},
  publisher={GitHub},
  howpublished={\url{https://github.com/deepseek-ai/deepseek-harness}},
}
```
Third-party dependencies and their licenses are disclosed in THIRD\_PARTY\_NOTICES.md.
