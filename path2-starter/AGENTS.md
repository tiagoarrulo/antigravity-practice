# My case: rules for the agent

These rules apply to every change in this folder. All data here is made up.

## What the data means
1. _Rule 1: a format the agent must not guess. Example: "Dates are dd/mm/yyyy. Any other
   format is an error: raise it, never skip the row."_
2. _Rule 2: what an empty value means. Example: "An empty quantity is unknown, not 0. Report it
   as `missing`."_
3. _Rule 3: what must never happen. Example: "Never drop or filter a row silently. Never edit
   the data file."_

## Before you say you are done
- Run `python check.py`. It must print `OK`.
- Report the figures you computed. Do not claim a number you did not compute.
