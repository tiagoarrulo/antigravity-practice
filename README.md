# Antigravity practice pack

Practice material for a hands-on session on the Google Antigravity App. It holds a small service
with one open change request, the two files that make the agent's answer checkable, and every
prompt of the session.

Everything here is fictitious: the retailer Mercado Atlântico, the product Atlântico Verde,
Hugo Leal, the stores and every figure are invented for the training. Use it freely.

## Start here

1. Click **Code → Download ZIP** on this page and unzip it. You do not need git.
2. Open the Antigravity App (latest release, signed in).
3. Click the **New Project** icon, **Add Folder**, choose the `stock-alerts` folder inside the
   unzipped pack (not the pack's root folder), then **Create**.
4. Check that you see `src/app.py` and `data/` in the project.
5. Start a new conversation.

Then follow [PROMPTS.md](PROMPTS.md): the prompt, the 15-minute try and the two paths.

## The case

Mercado Atlântico launches an own-brand olive oil, Atlântico Verde. Hugo Leal, the IT Product
Owner, asks for one change to a service that already runs: list every store and product below
its minimum stock, and total the sales in the export.

In the session you first watch that request run on its own. Then you run it yourself, with the
same words, after adding two small files: the team's rules and a check the agent can run.

## What each file is

### To read

| File | What it holds |
|---|---|
| `README.md` | This guide: how to start, what each file is, what to do when something fails |
| [`PROMPTS.md`](PROMPTS.md) | The session, step by step: set-up, the prompt (P1), the 15-minute try, the two paths and the four habits to keep. Every prompt is there to copy |

### The project you open: `stock-alerts/`

| File | What it holds |
|---|---|
| `stock-alerts/README.md` | The service in one page: its three endpoints, Hugo's change request, how to run and test it |
| `stock-alerts/src/app.py` | The service itself. `/health` works; `/alerts` and `/totals` are marked `TODO` and answer 501. This is the file the agent changes |
| `stock-alerts/data/Sales export.csv` | Daily sales per store and product, as the stores send them |
| `stock-alerts/data/Store stock - olive oil.xlsx` | Stock on hand and minimum stock per store and product |
| `stock-alerts/requirements.txt` | The two libraries the service needs: Flask and openpyxl |
| `stock-alerts/tests/conftest.py` | Test set-up only. The service has no tests yet: `pytest -q` answers `no tests ran` |

### The two files of the fix: `kit/`

| File | What it holds | Where it goes |
|---|---|---|
| `kit/AGENTS.md` | The team's rules, in plain text: what the data means, which alerts are urgent, how to answer Hugo, what to run before saying "done" | The root of `stock-alerts/` |
| `kit/tests/test_data_contract.py` | The check: four tests on the result (the totals, the store with no count, the alerts below minimum, the urgent ones) | `stock-alerts/tests/` |

### For after the break: `kit/extras/.agents/`

The folder name starts with a dot, so it is hidden: Cmd+Shift+. shows it in macOS Finder, and
View → Show → Hidden items in Windows Explorer.

| File | What it holds |
|---|---|
| `skills/load-sales-csv/SKILL.md` | A skill: a six-step checklist the agent loads when a task touches the sales file |
| `hooks.json` and `hooks/run_tests.py` | A hook: it runs the tests after each edit and before the agent stops |

### For a case of your own: `path2-starter/`

| File | What it holds |
|---|---|
| `path2-starter/AGENTS.md` | Three rules to fill in for your own made-up case |
| `path2-starter/check.py` | A small check: you write the figures you expect, it stays red until the agent's result matches |

## How the session uses it

| Step | Time | What you do | What you use |
|---|---|---|---|
| Get the project open | 3 min | Add `stock-alerts` as a project and ask what it does | `stock-alerts/` |
| Your turn | 15 min | Copy the two files, paste the same prompt, go from `4 failed` to `4 passed` | `kit/AGENTS.md`, `kit/tests/test_data_contract.py`, P1 in `PROMPTS.md` |
| Pick your path | 30 min | Path 1: add one thing to Hugo's service. Path 2: mock a small case from your week | Path 1: `PROMPTS.md`, `kit/extras/`. Path 2: `path2-starter/` |

## The figures to expect

After "Your turn", with the two files in place:

| What | Value |
|---|---|
| `pytest -q` | `4 failed` before the change is built, `4 passed` after |
| `/totals` | 14,267 units, €96,542.73 |
| `/alerts` | 6 urgent, 5 below minimum, 1 count missing |

Output varies between runs: the wording of the agent's answer will differ from your neighbour's.
The figures should not.

## To run the check yourself

Python 3.11 or later, inside `stock-alerts/`:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt pytest
pytest -q
```

Without the two kit files it answers `no tests ran`. Without Python you can still follow:
review the plan and the changes instead of running the check.

## If something does not work

| What you see | What to do |
|---|---|
| The agent cannot find `src/app.py` or `data/` | You added the pack's root folder. Remove the project and add the `stock-alerts` folder |
| `kit/extras/` looks empty | `.agents` is a hidden folder: see "For after the break" above |
| `pytest: command not found` | Activate the environment first (`source .venv/bin/activate`), or set it up with the lines above |
| `python3` is not found (common on Windows) | Use `python` or `py` instead |
| The agent wants to install packages and cannot | Install them yourself with the lines above, then tell the agent they are already installed |
| Still `4 failed` after the build | Ask the agent to read the failure, fix the cause and run the tests again, without changing the tests |
| The totals do not match | Do not accept an explanation: ask the agent to show the rows that cause the gap |

## Two rules while you practise

- **Made-up data only.** No real files, no customer data, no credentials.
- **Leave `data/` as it is.** The check compares the result with those two files.

## To take with you

The same two things work in any project of yours: a short `AGENTS.md` that says what only your
team knows, and one check the agent can run. `path2-starter/` is the smallest version of both.

Docs: [getting started](https://antigravity.google/docs/getting-started) ·
[rules](https://antigravity.google/docs/rules) · [skills](https://antigravity.google/docs/skills) ·
[hooks](https://antigravity.google/docs/hooks) · [permissions](https://antigravity.google/docs/permissions/)
