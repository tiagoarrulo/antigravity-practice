"""stock-alerts, no-install version: the same change request, Python standard library only.

Nothing to install: no Flask, no openpyxl, no pytest. Run it with:  python3 stock_alerts.py

The two functions below are the open change request (Hugo Leal, IT Product Owner).
All data is fictitious.
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
STOCK_CSV = DATA_DIR / "Store stock - olive oil.csv"
SALES_CSV = DATA_DIR / "Sales export.csv"


def health():
    return {"status": "ok", "data_files": [STOCK_CSV.name, SALES_CSV.name]}


def alerts():
    # TODO (Hugo): list every store and product below its minimum stock.
    raise NotImplementedError("alerts(): change request open")


def totals():
    # TODO (Hugo): total units and sales (EUR incl. VAT) in the sales export.
    raise NotImplementedError("totals(): change request open")


if __name__ == "__main__":
    for name, function in (("health", health), ("totals", totals), ("alerts", alerts)):
        try:
            print(name + ":", json.dumps(function(), indent=2, ensure_ascii=False, default=str))
        except NotImplementedError as open_request:
            print(name + ": not implemented (" + str(open_request) + ")")
