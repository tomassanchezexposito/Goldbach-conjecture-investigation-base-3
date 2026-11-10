# CoCalc ↔ GitHub research handoff (English-only repository)

## Architecture and limitations

- ChatGPT can inspect and update this private GitHub repository using the connected GitHub integration.
- The CoCalc Codex agent runs SageMath **inside** the CoCalc project and can edit its local files.
- The two agents do **not** share live memory, conversations, or a direct execution channel.
- CoCalc's red **Network** indicator may mean outbound GitHub access is blocked. Do not assume `git pull` or `git push` works until a harmless connectivity test succeeds.
- Never paste personal access tokens, SSH private keys, or other secrets into an AI chat. Use CoCalc's supported credential storage, scoped permissions, and minimal access if authentication is required.

## One-time CoCalc agent setup

1. In the existing `Prime-Correlations-210` Codex chat, ask the agent to test *read-only* connectivity with `git ls-remote https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3.git HEAD`. This private repository may require authentication even if outbound networking works. A failed result does not prove the repo is absent.
2. If networking works, configure a **least-privilege** GitHub connection using CoCalc's official credential facilities. Ask approval before any payment or installing software.
3. Clone into a **new** subdirectory (for example `goldbach-research-git`), never over the existing CoCalc project files. Use `git status` before each synchronization.
4. For research tasks, pull the latest `main`, execute reproducible code in SageMath, and save outputs in `results/stageNN/` with scripts, parameters, version, timestamp, and exact assertions.
5. Prefer a **new branch** `cocalc/stageNN-<short-description>` and a pull request for results. Never force-push. Do not silently overwrite the existing baseline.
6. ChatGPT reviews committed results and updates the next mathematical task in `tasks/NEXT_TASK.md`. The CoCalc agent only begins another run after a user action or an explicitly configured scheduler; it does not automatically receive this conversation.

## If CoCalc has no outbound network

Use the fallback: download the research task/script from GitHub in the user's browser and upload it to CoCalc. After execution, download the generated notebook/report and attach them to ChatGPT. ChatGPT can then review and commit verified text/code to GitHub. This is a **human-mediated handoff**, not an automatic integration.

## Mathematical integrity

The author's three-case statement is the primary target. Define H as even N>=4 with N-1 and N/2 composite; count distinct prime pairs p<q. Wheel-210 compatibility is not primality. Four-prime identities alone do not bound the off-diagonal correlation independently. Finite computations do not prove universal coverage.
