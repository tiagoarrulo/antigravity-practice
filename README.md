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

**Cannot install Python packages?** Open `stock-alerts-lite` instead of `stock-alerts`: the same
case with Python 3 and nothing else. The steps are below, under
[If you cannot install Python packages](#if-you-cannot-install-python-packages-stock-alerts-lite-and-kitlite).

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

### If you cannot install Python packages: `stock-alerts-lite/` and `kit/lite/`

The same case and the same figures, with Python 3 and nothing else: no Flask, no openpyxl, no
pytest, no virtual environment. Use it when `pip install` is blocked or fails on your laptop.
The session itself runs on `stock-alerts`; this version is the way in when that one cannot be
set up.

What changes:

| | `stock-alerts` | `stock-alerts-lite` |
|---|---|---|
| What the agent builds | `GET /alerts` and `GET /totals` in `src/app.py` | `alerts()` and `totals()` in `stock_alerts.py` |
| Stock file | Excel workbook | CSV, same layout |
| Files you copy in | `kit/AGENTS.md`, `kit/tests/test_data_contract.py` | `kit/lite/AGENTS.md`, `kit/lite/check.py` |
| The check | `pytest -q` | `python3 check.py` |
| You need | Python 3.11 or later, Flask, openpyxl, pytest | Python 3.9 or later |

What each file is:

| File | What it holds | Where it goes |
|---|---|---|
| `stock-alerts-lite/README.md` | This version in one page | Stays |
| `stock-alerts-lite/stock_alerts.py` | Two functions, `alerts()` and `totals()`, still not implemented. This is the file the agent changes | Stays |
| `stock-alerts-lite/data/` | The same sales export, and the stock file as CSV instead of Excel | Stays |
| `kit/lite/AGENTS.md` | The same rules, for this version | The root of `stock-alerts-lite/` |
| `kit/lite/check.py` | The same four checks, run with `python3 check.py` | The root of `stock-alerts-lite/` |

Step by step:

1. Check that Python 3 answers: `python3 --version` (Windows: `python --version` or
   `py --version`).
2. In the App: **New Project**, **Add Folder**, choose the `stock-alerts-lite` folder (not the
   pack's root folder), **Create**.
3. Copy `AGENTS.md` and `check.py` from `kit/lite/` into `stock-alerts-lite/`. Drag them in
   Finder or Explorer, or from the pack's root folder:

   ```bash
   cp kit/lite/AGENTS.md kit/lite/check.py stock-alerts-lite/
   ```

   Windows: `copy kit\lite\AGENTS.md stock-alerts-lite\` and
   `copy kit\lite\check.py stock-alerts-lite\`.
4. Inside `stock-alerts-lite/`, run the check before anything is built:

   ```bash
   python3 check.py
   ```

   It prints four `RED` lines and ends with `4 failed`. That is expected.
5. Start a **new conversation** and paste this prompt, word for word:

   > Hugo, the IT Product Owner, has a change request for the stock-alerts service. In
   > `stock_alerts.py` the functions `alerts()` and `totals()` are still not implemented. Using
   > the two files in `data/`, implement `alerts()` (every store and product below its minimum
   > stock) and `totals()` (total units and sales in EUR in the export). Use only the Python
   > standard library. Run it and show me the result.

6. Read the plan, approve it, let it build. Then run `python3 check.py` again: four `ok` lines,
   ending with `4 passed`. `python3 stock_alerts.py` prints the totals and the alerts.

The figures are the same as in the full version: 14,267 units, €96,542.73, 6 urgent, 5 below
minimum, 1 count missing. After the break, Path 2 needs nothing installed either; Path 1 is
written for the full `stock-alerts` service.

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
| `python3 check.py` (no-install version) | `4 failed` before the change is built, `4 passed` after |
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
| `pip install` is blocked or fails | Use the no-install version: open `stock-alerts-lite` and follow "Your turn, with nothing to install" in `PROMPTS.md` |
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
