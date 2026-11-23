# stock-alerts service: data conventions

These rules apply to every change in this workspace. The data is fictitious.

## Sales export (`data/Sales export.csv`)
- Separator `;`, UTF-8 with BOM (open with `utf-8-sig`), decimal comma in `Sales EUR incl. VAT`.
- `Date` is mixed: mostly `dd/mm/yyyy`, but 7 Lisbon stores send ISO `yyyy-mm-dd`. Parse both.
  A date in any other format is an error: raise it, never skip the row.
- Never drop, skip or silently filter a row. If a row cannot be parsed, fail loudly.
- Money is `Decimal`, never `float`.

## Store stock (`data/Store stock - olive oil.xlsx`)
- The header is the row whose first cell is `Store code` (row 4 today); do not hard-code the row number.
- An empty `Stock on hand` means the store has not sent its count. It is unknown, not 0.
  Report it as `count missing`; never raise a stock-out for it.
- Below minimum means `stock < minimum` on a known count.

## Priorities
- An alert is `urgent` when the known stock is at or below half the minimum (`stock * 2 <= minimum`).
- The other alerts below minimum stay `below minimum`.
- List `urgent` alerts first, biggest shortfall (`minimum - stock`) first.

## How to answer Hugo
Hugo is the IT Product Owner, not a developer. Answer in this order, with no implementation detail:
1. **Checks:** the last line of `pytest -q`.
2. **Control totals:** rows, units, EUR.
3. **Needs a decision:** every store with a missing count.
4. **Alerts:** one table, `urgent` first, then `below minimum`.

## Before you say you are done
- Run `pytest -q`. All tests must pass.
- Report the control totals from the export: rows, units and EUR, recomputed from the raw CSV
  (if the `load-sales-csv` skill is installed, follow it). Do not claim a total you did not compute.
- Never edit files in `data/` and never invent a reason for a mismatch: show the numbers.
