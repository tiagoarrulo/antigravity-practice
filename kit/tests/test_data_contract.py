"""Data contract for the stock-alerts service. Copy into tests/ before you build the change.

It fails until /alerts and /totals are built, and passes once the rules in AGENTS.md are followed.
The expected figures are the control totals of the fictitious sales export and stock file.
"""

from decimal import Decimal


def test_totals_match_the_export(client):
    body = client.get("/totals").get_json()
    assert body["rows"] == 3951
    assert body["units"] == 14267
    assert Decimal(str(body["sales_eur"])) == Decimal("96542.73")


def test_empty_count_is_not_a_stock_out(client):
    alerts = client.get("/alerts").get_json()["alerts"]
    sintra = [a for a in alerts if a["store_code"] == "MA-0215" and str(a["item"]) == "560103"]
    assert len(sintra) == 1
    assert sintra[0]["stock"] is None
    assert sintra[0]["status"] == "count missing"


def test_below_minimum_alerts(client):
    alerts = client.get("/alerts").get_json()["alerts"]
    known = [a for a in alerts if a["stock"] is not None]
    assert len(known) == 11
    assert all(a["stock"] < a["minimum"] for a in known)


def test_urgent_alerts(client):
    alerts = client.get("/alerts").get_json()["alerts"]
    known = [a for a in alerts if a["stock"] is not None]
    urgent = [a for a in known if a["status"] == "urgent"]
    assert len(urgent) == 6
    assert all(a["stock"] * 2 <= a["minimum"] for a in urgent)
    others = [a for a in known if a["status"] != "urgent"]
    assert len(others) == 5
    assert all(a["status"] == "below minimum" for a in others)
