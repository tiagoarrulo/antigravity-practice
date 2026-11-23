"""One check the agent can run: python check.py

Fill in EXPECTED with figures you worked out by hand from your made-up data.
The agent writes app.py with a summary() function that returns the same keys.
The check is red until the figures match.
"""

import sys

# Example: {"rows": 30, "total_units": 412, "below_minimum": 4}
EXPECTED = {}


def main():
    if not EXPECTED:
        print("RED: fill in EXPECTED in check.py with the figures you expect.")
        return 1
    try:
        from app import summary
    except ImportError as err:
        print(f"RED: app.py with a summary() function is missing ({err}).")
        return 1
    actual = summary()
    wrong = {k: (v, actual.get(k)) for k, v in EXPECTED.items() if actual.get(k) != v}
    if wrong:
        for key, (expected, got) in wrong.items():
            print(f"RED: {key}: expected {expected!r}, got {got!r}")
        return 1
    print("OK: " + ", ".join(f"{k}={v!r}" for k, v in EXPECTED.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
