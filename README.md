# Antigravity practice pack

Practice material for a hands-on session on the Google Antigravity App.
Everything here is fictitious: the retailer Mercado Atlântico, the product Atlântico Verde,
Hugo Leal, the stores and every figure are invented for the training.

## First, get the project open

1. Click **Code → Download ZIP** on this page and unzip it. You do not need git.
2. Open the Antigravity App (latest release, signed in).
3. Click the **New Project** icon, **Add Folder**, choose the `stock-alerts` folder inside the
   unzipped pack (not the pack's root folder), then **Create**.
4. Check that you see `src/app.py` and `data/` in the project.
5. Start a new conversation.

Then follow [PROMPTS.md](PROMPTS.md): the prompt, the 15-minute try and the two paths.

## What is here

| Folder / file | What it is |
|---|---|
| `stock-alerts/` | A small service that already runs: `/health` works, `/alerts` and `/totals` answer 501 |
| `kit/AGENTS.md` | The rules: what the data means, what is urgent, how to report |
| `kit/tests/test_data_contract.py` | The check: four tests that prove the result |
| `kit/extras/.agents/` | A skill and a hook, for after the break (hidden folder on macOS: Cmd+Shift+.) |
| `path2-starter/` | A starter `AGENTS.md` and a skeleton check for your own made-up case |
| `PROMPTS.md` | Every prompt of the session |

## To run the check yourself

Python 3.11 or later, inside `stock-alerts/`:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt pytest
pytest -q
```

The service has no tests yet: `pytest -q` answers `no tests ran`. With the two kit files in
place it gives `4 failed` before the change is built and `4 passed` after.
