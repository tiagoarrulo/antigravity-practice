"""stock-alerts: a demo service for Atlântico Verde (fictitious Mercado Atlântico case).

The service already runs. Hugo Leal (IT Product Owner) has a change request: implement
/alerts and /totals from two files the stores already send:
  - data/Store stock - olive oil.xlsx : stock on hand and minimum stock per store and product
  - data/Sales export.csv             : daily sales per store and product

This file is the starting state. Only /health works; /alerts and /totals answer 501.
All data is fictitious.
"""

import os
from pathlib import Path

from flask import Flask, jsonify

DATA_DIR = Path(os.environ.get("DATA_DIR", Path(__file__).resolve().parent.parent / "data"))
STOCK_XLSX = DATA_DIR / "Store stock - olive oil.xlsx"
SALES_CSV = DATA_DIR / "Sales export.csv"


def create_app():
    app = Flask(__name__)

    @app.route("/health")
    def health():
        return jsonify(status="ok", data_files=[STOCK_XLSX.name, SALES_CSV.name]), 200

    @app.route("/alerts")
    def alerts():
        # TODO (Hugo): list every store and product below its minimum stock.
        return jsonify(error="not implemented"), 501

    @app.route("/totals")
    def totals():
        # TODO (Hugo): total units and sales (EUR incl. VAT) in the sales export.
        return jsonify(error="not implemented"), 501

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
