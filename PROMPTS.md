# Google Antigravity: prompt pack

Everything in this pack is fictitious: Atlântico Verde, Mercado Atlântico, Hugo Leal, the
stores and every figure are invented for the training. Use it freely.

## What is in the pack

| Folder / file | What it is | When you use it |
|---|---|---|
| `stock-alerts/` | The stock-alerts service as it runs today: `/health` works, `/alerts` and `/totals` answer 501. Two data files and a README; no tests yet | Your turn, Path 1 |
| `kit/AGENTS.md`, `kit/tests/test_data_contract.py` | The two files of the fix: the rules and the check | Your turn |
| `kit/extras/.agents/` | A skill and a hook | Path 1 |
| `path2-starter/` | A starter `AGENTS.md` and a skeleton check | Path 2 |
| `stock-alerts-lite/`, `kit/lite/` | The same case with nothing to install: Python 3 only | Your turn, if you cannot install packages |
| `PROMPTS.md` | This file | All session |

## Set up

### First, get the project open

1. **Antigravity App, latest release**, signed in: Use Business Account → Continue with Google
   Cloud → in Select Billing Model choose Subscription and pick your licence.
   Nothing to pick? Ask your IT team; it is a licence or setup question.
2. **Download ZIP** of this pack and unzip it.
3. In the App, click the **New Project** icon, **Add Folder**, choose the `stock-alerts` folder
   (not the pack's root folder), then **Create**.
4. Check that you see `src/app.py` and `data/` in the project.
5. Settings: **Planning mode**, plan review on **Request review**, terminal commands on ask-first.
6. Start a **new conversation** (Local mode).
7. First prompt, to check the agent reads the project:

> What does this project do, and what is missing?

### Python (so you can run the check yourself)

Python 3.11 or later, then in `stock-alerts/`:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt pytest
pytest -q
```

`pytest -q` answers `no tests ran`: the service has no tests yet.

Without Python you can still follow: review the plan and the diff instead of running the service.

**Cannot install packages at all?** Use the no-install version: see "Your turn, with nothing to
install" below. It needs Python 3 and nothing else.

**No network in the sandbox:** if the agent wants to `pip install`, it will ask. Install the
dependencies yourself first.

## The prompt

### P1 · Hugo's change request

Use the same words every time.

> Hugo, the IT Product Owner, has a change request for the stock-alerts service. The service
> already runs; `GET /alerts` and `GET /totals` still answer 501. Using the two files in `data/`,
> implement `GET /alerts` (every store and product below its minimum stock) and `GET /totals`
> (total units and sales in EUR in the export). Run it and show me the result.

## Your turn · 30 min

After the break. Path 1 starts with the two files below, then adds one thing Hugo would ask
next. Path 2, a case of your own, is further down.

### Add two files. Same prompt.

1. From `kit/`: `AGENTS.md` into `stock-alerts/`, and `test_data_contract.py` into
   `stock-alerts/tests/`.
2. Run `pytest -q`: `4 failed`. That is expected: nothing is built yet.
3. Start a **new conversation** and paste **P1** word for word.
4. Read the plan: does it use the rules? Approve it, then let it build.
5. Check: `pytest -q` gives `4 passed`. `/totals`: **14,267 units**, **€96,542.73**.
   `/alerts`: **6 urgent**, **5 below minimum**, **1 count missing**.

The answer is now one you can check: the rules say what the data means and what the team
decided (what is urgent, how to report); the test proves the result.

### Your turn, with nothing to install

For a laptop where `pip install` is not possible. Same case, same figures, Python 3 only.

1. In the App: **New Project**, **Add Folder**, choose `stock-alerts-lite` (not the pack's root
   folder), **Create**.
2. From `kit/lite/`: copy `AGENTS.md` and `check.py` into `stock-alerts-lite/`.
3. Run `python3 check.py` (Windows: `python check.py` or `py check.py`): `4 failed`. That is
   expected: nothing is built yet.
4. Start a **new conversation** and paste the prompt below.
5. Check: `python3 check.py` ends with `4 passed`. Totals: **14,267 units**, **€96,542.73**.
   Alerts: **6 urgent**, **5 below minimum**, **1 count missing**.

> Hugo, the IT Product Owner, has a change request for the stock-alerts service. In
> `stock_alerts.py` the functions `alerts()` and `totals()` are still not implemented. Using the
> two files in `data/`, implement `alerts()` (every store and product below its minimum stock) and
> `totals()` (total units and sales in EUR in the export). Use only the Python standard library.
> Run it and show me the result.

From here: Path 2 needs nothing installed. Path 1 (1a to 1e) is written for the full
`stock-alerts/` service.

## Then · pick your path

Plan first (Planning mode, Request review) and give the agent one check it can run.
Note one thing you had to correct: three or four of you will show what you made.

### Path 1 · Build on Hugo's service

Start from a green `stock-alerts/` (after the two files above). The contract test stays green.

> **1a. Alerts for one store.** Add a `store` filter to `GET /alerts` (for example
> `/alerts?store=MA-0215`) that returns only that store's alerts. Add a test for it. Keep every
> existing test green.

> **1b. A CSV for the store team.** Add `GET /alerts.csv`: the same alerts as a file the store
> team can open in Excel (`;` separator, decimal comma, UTF-8 with BOM). Add a test that reads
> the file back.

> **1c. A small page.** Add an HTML page at `/` that lists the alerts per store, with "count
> missing" shown apart from real stock-outs. No JavaScript framework. Keep the tests green.

**1d. Add the skill.** Copy the `.agents` folder from `kit/extras/` to the root of
`stock-alerts/` (the name starts with a dot: macOS Finder hides it, Cmd+Shift+. shows it). Then:

> Read `.agents/skills/load-sales-csv/SKILL.md`. Recompute the totals following it and show me
> the output of each check.

**1e. Add the hook.** With the `.agents` folder in place:

> Explain what each hook in `.agents/hooks.json` does and when it runs. Then make a small change
> to `src/app.py` and show me `.agents/last-test-run.txt` after the edit.

The hook runs the tests with the project's `.venv` when there is one. Without pytest it holds
nothing back: it writes the reason to `.agents/last-test-run.txt` and lets the agent finish.

The hook calls `python3`. If only `python` or `py` is on your path (common on Windows), change
`python3` in the two `command` lines of `.agents/hooks.json`. The hook is not tested on Windows:
if `.agents/last-test-run.txt` does not appear, run `pytest -q` yourself.

### Path 2 · Mock a case from your week

Made-up data only: no real files, no customer data, no secrets, tokens or `.env` files.

1. Create a **new empty folder** and copy the two files from `path2-starter/` into it.
2. Open the folder as a new project in the App.
3. Fill in the three rules in `AGENTS.md` and the expected numbers in `check.py`.
4. Paste the prompt below, with your own case.

> I want to mock this case from my week: _one or two sentences_. Create a small made-up data
> file for it (20 to 50 rows, invented values), then write `app.py` with a `summary()` function
> that returns the figures `check.py` expects. Follow `AGENTS.md`. Run `python check.py` and show
> me the output.

Three ideas if you need one:

- **A weekly export to clean:** a CSV with two date formats and a decimal comma; total it per week.
- **A threshold report:** items with a quantity and a minimum; list what is below the minimum
  and what has no value at all.
- **Two files to reconcile:** the same ids in two files; report what is in one and not the other.

After the first miss:

> Add one or two lines to `AGENTS.md` so you don't repeat _the miss_. Show me the rule.

## Four habits, every time

### Say it, check it, review it, write it down

1. **Say the job:** what it is for, which files, what "done" looks like.
2. **Give it a check:** a test, a command, the numbers you expect. Ask for evidence, not "done".
3. **Review the plan:** Planning mode, Request review. Comment before it builds.
4. **Write it down:** a miss twice becomes a rule in `AGENTS.md`; a check that repeats becomes a skill.

Docs: [getting started](https://antigravity.google/docs/getting-started) ·
[enterprise sign-in](https://antigravity.google/docs/enterprise/) ·
[rules](https://antigravity.google/docs/rules) · [skills](https://antigravity.google/docs/skills) ·
[hooks](https://antigravity.google/docs/hooks) · [permissions](https://antigravity.google/docs/permissions/) ·
[sandbox](https://antigravity.google/docs/sandbox/)
