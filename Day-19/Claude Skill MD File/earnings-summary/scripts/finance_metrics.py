#!/usr/bin/env python3
"""Deterministic financial-ratio calculator for the earnings-summary skill.
Reads one JSON object from STDIN, prints one JSON object to STDOUT."""
import json, sys

def pct_change(new, old):
    if old in (None, 0) or new is None:
        return None
    return round((new - old) / old * 100, 1)

def margin(part, whole):
    if whole in (None, 0) or part is None:
        return None
    return round(part / whole * 100, 1)

def main():
    data = json.load(sys.stdin)
    cur = data.get("current", {})
    revenue, cogs = cur.get("revenue"), cur.get("cogs")
    opex, net_income = cur.get("opex"), cur.get("net_income")

    gross_profit = revenue - cogs if (revenue is not None and cogs is not None) else None
    operating_income = (gross_profit - opex) if (gross_profit is not None and opex is not None) else None

    result = {
        "company": data.get("company"),
        "quarter": data.get("quarter"),
        "revenue": revenue,
        "gross_profit": gross_profit,
        "operating_income": operating_income,
        "net_income": net_income,
        "gross_margin_pct": margin(gross_profit, revenue),
        "operating_margin_pct": margin(operating_income, revenue),
        "net_margin_pct": margin(net_income, revenue),
        "revenue_qoq_pct": pct_change(revenue, data.get("prior_quarter", {}).get("revenue")),
        "revenue_yoy_pct": pct_change(revenue, data.get("year_ago", {}).get("revenue")),
        "net_income_yoy_pct": pct_change(net_income, data.get("year_ago", {}).get("net_income")),
    }
    json.dump(result, sys.stdout, indent=2)

if __name__ == "__main__":
    main()
