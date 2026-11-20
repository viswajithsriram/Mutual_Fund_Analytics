# Mutual Fund Analytics – Data Dictionary

## Project Overview
This project analyses mutual fund data using Python, Pandas, SQLite and SQL.

## 1. dim_fund

| Column | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Unique mutual fund code |
| scheme_name | TEXT | Name of the mutual fund |
| fund_house | TEXT | Mutual fund company |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Direct or Regular plan |
| risk_grade | TEXT | Risk classification |
| launch_date | TEXT | Fund launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | REAL | Fund expense ratio |

| exit_load_pct | REAL | Exit load percentage |
| min_sip_amount | REAL | Minimum SIP investment |
| min_lumpsum_amount | REAL | Minimum lump sum investment |
| fund_manager | TEXT | Name of fund manager |
| sebi_category_code | TEXT | SEBI category code |

## 2. dim_date

| Column | Data Type | Description |
|---|---|---|
| date_id | INTEGER | Unique date identifier |
| date_value | TEXT | Actual date |
| year | INTEGER | Calendar year |
| month | INTEGER | Month number |
| month_name | TEXT | Month name |
| quarter | INTEGER | Financial/calendar quarter |

## 3. fact_nav

| Column | Data Type | Description |
|---|---|---|
| nav_id | INTEGER | Unique NAV record ID |
| amfi_code | INTEGER | Mutual fund code |
| date_id | INTEGER | Date reference |
| nav | REAL | Net Asset Value |

## 4. fact_transactions

| Column | Data Type | Description |
|---|---|---|
| transaction_id | INTEGER | Unique transaction ID |
| investor_id | TEXT | Investor identifier |
| amfi_code | INTEGER | Mutual fund code |
| date_id | INTEGER | Transaction date reference |
| transaction_type | TEXT | SIP, Lumpsum or Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor's state |
| city | TEXT | Investor's city |
| city_tier | TEXT | City classification |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC verification status |

## 5. fact_performance

| Column | Data Type | Description |
|---|---|---|
| performance_id | INTEGER | Unique performance ID |
| amfi_code | INTEGER | Mutual fund code |
| scheme_name | TEXT | Fund name |
| fund_house | TEXT | Fund company |
| category | TEXT | Fund category |
| plan | TEXT | Direct or Regular plan |
| return_1yr_pct | REAL | One-year return |
| return_3yr_pct | REAL | Three-year return |
| return_5yr_pct | REAL | Five-year return |
| benchmark_3yr_pct | REAL | Three-year benchmark return |
| alpha | REAL | Excess return measure |
| beta | REAL | Market risk measure |
| sharpe_ratio | REAL | Risk-adjusted return |
| sortino_ratio | REAL | Downside risk-adjusted return |
| std_dev_ann_pct | REAL | Annualised standard deviation |
| max_drawdown_pct | REAL | Maximum fall in value |
| expense_ratio_pct | REAL | Expense ratio |
| aum_crore | REAL | Assets under management in crore |
| morningstar_rating | INTEGER | Fund rating |
| risk_grade | TEXT | Risk classification |

## 6. fact_aum

| Column | Data Type | Description |
|---|---|---|
| aum_id | INTEGER | Unique AUM record ID |
| date_id | INTEGER | Date reference |
| fund_house | TEXT | Mutual fund company |
| aum_lakh_crore | REAL | AUM in lakh crore |
| aum_crore | REAL | AUM in crore |
| num_schemes | INTEGER | Number of schemes |

## 7. fact_sip

| Column | Data Type | Description |
|---|---|---|
| sip_id | INTEGER | Unique SIP record ID |
| month | TEXT | Month of SIP data |
| sip_inflow_crore | REAL | Monthly SIP inflow |
| active_sip_accounts_crore | REAL | Active SIP accounts |
| new_sip_accounts_lakh | REAL | New SIP accounts |
| sip_aum_lakh_crore | REAL | SIP assets under management |
| yoy_growth_pct | REAL | Year-on-year growth percentage |

## 8. fact_category_inflows

| Column | Data Type | Description |
|---|---|---|
| category_inflow_id | INTEGER | Unique record ID |
| month | TEXT | Month of data |
| category | TEXT | Mutual fund category |
| net_inflow_crore | REAL | Net investment inflow |

## 9. fact_folio_count

| Column | Data Type | Description |
|---|---|---|
| folio_id | INTEGER | Unique folio record ID |
| month | TEXT | Month of data |
| total_folios_crore | REAL | Total folio accounts |
| equity_folios_crore | REAL | Equity folio accounts |
| debt_folios_crore | REAL | Debt folio accounts |
| hybrid_folios_crore | REAL | Hybrid folio accounts |
| others_folios_crore | REAL | Other folio accounts |

## 10. fact_portfolio_holdings

| Column | Data Type | Description |
|---|---|---|
| holding_id | INTEGER | Unique holding record ID |
| amfi_code | INTEGER | Mutual fund code |
| stock_symbol | TEXT | Stock ticker symbol |
| stock_name | TEXT | Company name |
| sector | TEXT | Industry sector |
| weight_pct | REAL | Portfolio weight percentage |
| market_value_cr | REAL | Market value in crore |
| current_price_inr | REAL | Current stock price |
| portfolio_date | TEXT | Portfolio reporting date |

## 11. fact_benchmark_indices

| Column | Data Type | Description |
|---|---|---|
| benchmark_id | INTEGER | Unique benchmark record ID |
| date_id | INTEGER | Date reference |
| index_name | TEXT | Benchmark index name |
| close_value | REAL | Index closing value |

## Data Sources

The datasets used in this project include:

1. Fund Master
2. NAV History
3. Investor Transactions
4. Scheme Performance
5. AUM by Fund House
6. Monthly SIP Inflows
7. Category Inflows
8. Industry Folio Count
9. Portfolio Holdings
10. Benchmark Indices

## Tools and Technologies

- Python
- Pandas
- SQLite
- SQLAlchemy
- SQL

## Project Purpose

To clean, store and analyse mutual fund data and generate useful insights about fund performance, investments, NAV, SIP growth and portfolio holdings.