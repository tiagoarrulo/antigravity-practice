---
name: load-sales-csv
description: Checklist for loading or changing code that reads the store sales export (data/Sales export.csv). Use whenever you parse, aggregate or report on sales rows, units or EUR totals, and before you report any total.
---

# Load the sales CSV: checklist

Work through every step and show the output of each check in your walkthrough.

1. **Open it right.** `encoding="utf-8-sig"`, `delimiter=";"`, `newline=""`.
2. **Count the raw rows** with the standard library before your own parser runs:
   `python3 -c "import csv; print(sum(1 for _ in csv.DictReader(open('data/Sales export.csv', encoding='utf-8-sig'), delimiter=';')))"`
   Expected: **3,951**. Your loader must return the same number. Fewer rows means something was skipped.
3. **Dates.** Count the formats you found (`dd/mm/yyyy` and `yyyy-mm-dd`). Both must parse.
   Expected: 2,800 dd/mm/yyyy and 1,151 ISO (stores MA-0211 to MA-0217). Any other format: stop and report it.
4. **Numbers.** `Units` is an integer. `Sales EUR incl. VAT` uses a decimal comma: parse it as `Decimal`.
5. **Control totals.** Total units **14,267** and sales **EUR 96,542.73**.
   If yours differ, do not explain the gap: find the rows that cause it and show them.
6. **Prove it.** Run `pytest -q` and paste the summary line.
