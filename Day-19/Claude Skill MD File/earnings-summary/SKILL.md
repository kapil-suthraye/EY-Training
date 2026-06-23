---
name: earnings-summary
description: Turn raw quarterly financial figures into a standardized internal investor-update memo. Use this whenever the user provides quarterly numbers (revenue, COGS, opex, net income) for one or more periods and asks for an earnings summary, results memo, quarterly review, or investor update. Always compute the ratios with the bundled script and follow the house format and disclaimer rules.
---

# Earnings Summary Memo

This skill produces a consistent **internal investor-update memo** from raw quarterly
figures. It exists so every analyst produces the same structure, the same ratios,
and the same mandatory disclaimer, without re-explaining house style each time.

## When to use

Use this skill when the user supplies quarterly financials and wants a written
summary. Do NOT give buy/sell/hold recommendations or price targets — this skill
only *summarizes provided numbers*.

## Workflow (follow in order)

1. **Compute the metrics deterministically.** Do not do the arithmetic yourself.
   Run the bundled script with the user's figures as JSON on standard input:

       run_skill_script(script="finance_metrics.py", args_json=<the user's numbers as JSON>)

   The script returns margins (gross / operating / net) and growth rates
   (quarter-over-quarter and year-over-year). Using code guarantees the numbers
   are correct and identical every run.

2. **Load the house style.** Read `references/style_guide.md` to get the exact
   section order, tone, rounding rules, and the mandatory disclaimer text.

3. **Write the memo** using ONLY the values returned by the script, following the
   section order from the style guide. Round exactly as the style guide says.

4. **Append the mandatory disclaimer** verbatim from the style guide. Never omit it.

## Expected input shape

    {
      "company": "Acme Corp",
      "quarter": "Q2 FY2026",
      "current":       {"revenue": 0, "cogs": 0, "opex": 0, "net_income": 0},
      "prior_quarter": {"revenue": 0, "net_income": 0},
      "year_ago":      {"revenue": 0, "net_income": 0}
    }

`prior_quarter` and `year_ago` are optional — if a period is missing, the script
omits the related growth figure and the memo simply does not mention it.
