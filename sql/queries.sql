-- 1. Top 5 Mutual Funds by AUM

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month

SELECT
    d.year,
    d.month,
    ROUND(AVG(n.nav), 2) AS average_nav
FROM fact_nav n
JOIN dim_date d
    ON n.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

-- 3. SIP Year-on-Year Growth

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM fact_sip
ORDER BY month;

-- 4. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio Below 1%

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;

-- 6. Top 5 Funds by 3-Year Returns

SELECT
    scheme_name,
    fund_house,
    return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- 7. Total AUM by Fund House

SELECT
    fund_house,
    ROUND(SUM(aum_crore), 2) AS total_aum_crore
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum_crore DESC;

-- 8. Category-wise Net Inflows

SELECT
    category,
    ROUND(SUM(net_inflow_crore), 2) AS total_net_inflow
FROM fact_category_inflows
GROUP BY category
ORDER BY total_net_inflow DESC;

-- 9. Portfolio Holdings by Sector

SELECT
    sector,
    COUNT(*) AS total_stocks,
    ROUND(SUM(market_value_cr), 2) AS total_market_value
FROM fact_portfolio_holdings
GROUP BY sector
ORDER BY total_market_value DESC;

-- 10. Latest Benchmark Index Values

SELECT
    b.index_name,
    d.date_value,
    b.close_value
FROM fact_benchmark_indices b
JOIN dim_date d
    ON b.date_id = d.date_id
WHERE b.date_id = (
    SELECT MAX(date_id)
    FROM fact_benchmark_indices
)
ORDER BY b.index_name;