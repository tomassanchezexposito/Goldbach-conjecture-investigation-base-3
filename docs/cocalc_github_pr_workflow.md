# CoCalc to GitHub handoff — Git and Pull Requests

**Do not confuse GitHub CLI with Git connectivity.** The CoCalc image may not contain the `gh` command. This does **not** prevent Git SSH authentication, `git fetch`, `git commit` or `git push`.

## Verified workflow

1. Use the existing dedicated SSH deploy identity; never display or copy its private key or modify credentials merely to create a PR.
2. Work on the research task's dedicated branch only. Keep `main` unchanged. Confirm `git status` is clean before and after work.
3. Create verified code/reports and commit them. Push with the configured dedicated SSH identity, with `IdentitiesOnly=yes` if the SSH agent is not selecting it.
4. After a successful push, verify remote head SHA using `git ls-remote origin refs/heads/<branch>`; report both the commit SHA and URL of the pushed branch.
5. **If `gh` is unavailable:** do **not** install `gh`, request a personal access token, use an unauthenticated GitHub REST API for private repo management, or describe the PR step as a failed publication. Provide a comparison URL in the final response, for example `https://github.com/tomassanchezexposito/Goldbach-conjecture-investigation-base-3/compare/<base>...<head>?expand=1`.
6. The separately connected GitHub integration in ChatGPT can create or update draft pull requests. The CoCalc agent need not perform that action. An existing PR may already track the branch and automatically show later pushed commits; check before requesting a new one.
7. Do not merge to `main`, force-push, delete history or change repository permissions without specific approval.

## Authentication distinctions

- SSH deployment keys authorize Git operations for the configured repository.
- The `gh` CLI is a distinct program, and its usual API authentication is distinct from the SSH key used by Git.
- An unauthenticated REST request can return HTTP 404 for a private issue, even when the Git SSH clone/push works.
- Report these conditions independently and precisely.

## Scientific integration

Every handoff must include: branch, commit SHA, exact test commands and outputs, proof classifications, new counterexamples/invalid steps, and first unresolved arithmetic estimate. Do not call an exact counting identity a universal existence theorem. All repository content is English.
