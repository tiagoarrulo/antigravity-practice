# stock-alerts

Internal service for the Atlântico Verde launch at Mercado Atlântico (fictitious case: every
store, product and figure is invented). It reads the two files the stores already send and
answers the store-operations team.

| Endpoint | Status | What it answers |
|---|---|---|
| `GET /health` | runs | `{"status": "ok", "data_files": [...]}` |
| `GET /alerts` | **501, change request open** | every store and product below its minimum stock |
| `GET /totals` | **501, change request open** | total units and sales in EUR in the sales export |

**Change request (Hugo Leal, IT Product Owner):** implement `/alerts` and `/totals` from the two
files in `data/`. Nothing else in the service changes.

## Data
- `data/Store stock - olive oil.xlsx`: stock on hand and minimum stock per store and product.
- `data/Sales export.csv`: daily sales per store and product.

## Run and test
```bash
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt pytest
pytest -q                # "no tests ran": the service has no tests yet
python src/app.py        # http://localhost:8080/health
```
