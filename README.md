# Antigravity practice pack

Practice material for a hands-on session on the Google Antigravity App: a small service with one
open change request, and every prompt of the session.

Everything here is fictitious: the retailer Mercado Atlântico, the product Atlântico Verde,
Hugo Leal, the stores and every figure are invented for the training. Use it freely.

## Start here

1. Click **Code → Download ZIP** on this page and unzip it. You do not need git.
2. Open the Antigravity App (latest release, signed in).
3. Click the **New Project** icon, **Add Folder**, choose the `stock-alerts` folder inside the
   unzipped pack (not the pack's root folder), then **Create**.
4. Start a new conversation.
5. Follow [PROMPTS.md](PROMPTS.md): every step and every prompt is there to copy.

**Cannot install Python packages?** The `stock-alerts` project needs three of them (Flask,
openpyxl and pytest). If your laptop has Python 3 but does not let you install packages, choose
the `stock-alerts-lite` folder in step 3 instead, and follow
["Your turn, with nothing to install"](PROMPTS.md#your-turn-with-nothing-to-install).
It is the same exercise with the same figures, and it runs with Python 3 alone.

## The case

Mercado Atlântico launches an own-brand olive oil, Atlântico Verde. Hugo Leal, the IT Product
Owner, asks for one change to a service that already runs: list every store and product below
its minimum stock, and total the sales.

In the session you first watch that request run on its own. Then you run it yourself, with the
same words, after adding two small files: the team's rules and a check the agent can run.

## What is in the pack

| Folder or file | What it is |
|---|---|
| `PROMPTS.md` | The session, step by step, with every prompt |
| `stock-alerts/` | The project you open: a small service with two things still to build |
| `kit/` | The two files you copy into the project: the team's rules (`AGENTS.md`) and a check |
| `stock-alerts-lite/` and `kit/lite/` | The same exercise with no packages to install: Python 3 is enough |
| `kit/extras/` | For after the break: a skill and a hook |
| `path2-starter/` | For after the break: a starter for a case of your own |

## What you should see

After "Your turn", with the two files in place:

| What | Value |
|---|---|
| The check, before the agent builds | `4 failed` |
| The check, after | `4 passed` |
| Totals | 14,267 units, €96,542.73 |
| Alerts | 6 urgent, 5 below minimum, 1 count missing |

The wording of the agent's answer will differ from your neighbour's. The figures should not.

## If something does not work

| What you see | What to do |
|---|---|
| The agent cannot find `src/app.py` or `data/` | You added the pack's root folder. Remove the project and add the `stock-alerts` folder |
| `pip install` is blocked or fails | Use `stock-alerts-lite`: see "Cannot install Python packages?" above. It needs Python 3 only |
| `kit/extras/` looks empty | It holds a hidden folder, `.agents`. Cmd+Shift+. shows it in macOS Finder; View → Show → Hidden items in Windows Explorer |
| `python3` is not found (common on Windows) | Use `python` or `py` instead |
| Still `4 failed` after the build | Ask the agent to read the failure, fix the cause and run the check again, without changing the check |
| The totals do not match | Do not accept an explanation: ask the agent to show the rows that cause the gap |

## Two rules while you practise

- **Made-up data only.** No real files, no customer data, no credentials.
- **Leave `data/` as it is.** The check compares the result with those two files.

## More detail

<details>
<summary>What each file is</summary>

**The project you open: `stock-alerts/`**

| File | What it holds |
|---|---|
| `stock-alerts/README.md` | The service in one page: its three endpoints, Hugo's change request, how to run and test it |
| `stock-alerts/src/app.py` | The service itself. `/health` works; `/alerts` and `/totals` are marked `TODO` and answer 501. This is the file the agent changes |
| `stock-alerts/data/Sales export.csv` | Daily sales per store and product, as the stores send them |
| `stock-alerts/data/Store stock - olive oil.xlsx` | Stock on hand and minimum stock per store and product |
| `stock-alerts/requirements.txt` | The two libraries the service needs: Flask and openpyxl |
| `stock-alerts/tests/conftest.py` | Test set-up only. The service has no tests yet: `pytest -q` answers `no tests ran` |

**The two files you copy in: `kit/`**

| File | What it holds | Where it goes |
|---|---|---|
| `kit/AGENTS.md` | The team's rules, in plain text: what the data means, which alerts are urgent, how to answer Hugo, what to run before saying "done" | The root of `stock-alerts/` |
| `kit/tests/test_data_contract.py` | The check: four tests on the result (the totals, the store with no count, the alerts below minimum, the urgent ones) | `stock-alerts/tests/` |

**With nothing to install: `stock-alerts-lite/` and `kit/lite/`**

| File | What it holds | Where it goes |
|---|---|---|
| `stock-alerts-lite/stock_alerts.py` | Two functions, `alerts()` and `totals()`, still not implemented. This is the file the agent changes | Stays |
| `stock-alerts-lite/data/` | The same sales export, and the stock file as CSV instead of Excel | Stays |
| `kit/lite/AGENTS.md` | The same rules, for this version | The root of `stock-alerts-lite/` |
| `kit/lite/check.py` | The same four checks, run with `python3 check.py` | The root of `stock-alerts-lite/` |

**For after the break: `kit/extras/.agents/` and `path2-starter/`**

| File | What it holds |
|---|---|
| `kit/extras/.agents/skills/load-sales-csv/SKILL.md` | A skill: a six-step checklist the agent loads when a task touches the sales file |
| `kit/extras/.agents/hooks.json` and `hooks/run_tests.py` | A hook: it runs the tests after each edit and before the agent stops |
| `path2-starter/AGENTS.md` | Three rules to fill in for your own made-up case |
| `path2-starter/check.py` | A small check: you write the figures you expect, it stays red until the agent's result matches |

</details>

<details>
<summary>Run the check yourself (Python)</summary>

Python 3.11 or later, inside `stock-alerts/`:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt pytest
pytest -q
```

Without the two kit files it answers `no tests ran`. If `pytest` is not found, activate the
environment first. If the agent wants to install packages and cannot, install them yourself with
the lines above, then tell the agent they are already installed.

With `stock-alerts-lite` none of this is needed: `python3 check.py` runs with Python 3 alone.

</details>

## To take with you

The same two things work in any project of yours: a short `AGENTS.md` that says what only your
team knows, and one check the agent can run. `path2-starter/` is the smallest version of both.

Docs: [getting started](https://antigravity.google/docs/getting-started) ·
[rules](https://antigravity.google/docs/rules) · [skills](https://antigravity.google/docs/skills) ·
[hooks](https://antigravity.google/docs/hooks) · [permissions](https://antigravity.google/docs/permissions/)
