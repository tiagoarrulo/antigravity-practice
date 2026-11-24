# stock-alerts, no-install version

The same case as `stock-alerts/`, for a laptop where you cannot install Python packages.
It needs Python 3 and nothing else: no Flask, no openpyxl, no pytest.
Everything is fictitious: every store, product and figure is invented.

| Function in `stock_alerts.py` | Status | What it answers |
|---|---|---|
| `health()` | runs | `{"status": "ok", "data_files": [...]}` |
| `alerts()` | **not implemented, change request open** | every store and product below its minimum stock |
| `totals()` | **not implemented, change request open** | total units and sales in EUR in the sales export |

**Change request (Hugo Leal, IT Product Owner):** implement `alerts()` and `totals()` from the two
files in `data/`. Nothing else changes.

## Data
- `data/Store stock - olive oil.csv`: stock on hand and minimum stock per store and product.
- `data/Sales export.csv`: daily sales per store and product.

## Run
```bash
python3 stock_alerts.py        # Windows: python stock_alerts.py  (or: py stock_alerts.py)
```
There is no check yet. The check is `kit/lite/check.py` in the pack: see `PROMPTS.md`.
