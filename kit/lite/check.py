"""The check for the no-install version: python3 check.py

Copy it next to stock_alerts.py before you build the change. Standard library only.
It is red until alerts() and totals() are built, and green once the rules in AGENTS.md are followed.
The expected figures are the control totals of the fictitious sales export and stock file.
"""

import sys
from decimal import Decimal


def check_totals_match_the_export(sa):
    body = sa.totals()
    assert body["rows"] == 3951, "rows: expected 3951, got %r" % (body["rows"],)
    assert body["units"] == 14267, "units: expected 14267, got %r" % (body["units"],)
    assert Decimal(str(body["sales_eur"])) == Decimal("96542.73"), \
        "sales_eur: expected 96542.73, got %r" % (body["sales_eur"],)


def check_empty_count_is_not_a_stock_out(sa):
    rows = [a for a in sa.alerts() if a["store_code"] == "MA-0215" and str(a["item"]) == "560103"]
    assert len(rows) == 1, "store MA-0215, item 560103: expected 1 line, got %d" % len(rows)
    assert rows[0]["stock"] is None, "stock: expected None, got %r" % (rows[0]["stock"],)
    assert rows[0]["status"] == "count missing", "status: expected 'count missing', got %r" % (rows[0]["status"],)


def check_below_minimum_alerts(sa):
    known = [a for a in sa.alerts() if a["stock"] is not None]
    assert len(known) == 11, "alerts on a known count: expected 11, got %d" % len(known)
    assert all(a["stock"] < a["minimum"] for a in known), "an alert is not below its minimum"


def check_urgent_alerts(sa):
    known = [a for a in sa.alerts() if a["stock"] is not None]
    urgent = [a for a in known if a["status"] == "urgent"]
    assert len(urgent) == 6, "urgent: expected 6, got %d" % len(urgent)
    assert all(a["stock"] * 2 <= a["minimum"] for a in urgent), "an urgent alert is above half its minimum"
    others = [a for a in known if a["status"] != "urgent"]
    assert len(others) == 5, "below minimum: expected 5, got %d" % len(others)
    assert all(a["status"] == "below minimum" for a in others), "a status is neither urgent nor below minimum"


CHECKS = [check_totals_match_the_export, check_empty_count_is_not_a_stock_out,
          check_below_minimum_alerts, check_urgent_alerts]


def main():
    try:
        import stock_alerts as sa
    except ImportError as err:
        print("RED  stock_alerts.py is not next to check.py (%s)" % err)
        print("4 failed")
        return 1
    failed = 0
    for check in CHECKS:
        name = check.__name__[len("check_"):].replace("_", " ")
        try:
            check(sa)
            print("ok   " + name)
        except NotImplementedError as err:
            failed += 1
            print("RED  %s: not built yet (%s)" % (name, err))
        except Exception as err:  # the check must report every failure, never crash
            failed += 1
            print("RED  %s: %s: %s" % (name, type(err).__name__, err))
    passed = len(CHECKS) - failed
    print("%d passed" % passed if not failed else "%d failed, %d passed" % (failed, passed)
          if passed else "%d failed" % failed)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
