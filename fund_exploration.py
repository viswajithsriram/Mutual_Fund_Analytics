import pandas as pd

fund = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund.loc[fund["amfi_code"].astype(str).str.fullmatch(r"\d+"), "amfi_code"].astype(str))
nav_codes = set(nav["amfi_code"].astype(str))

missing_codes = fund_codes - nav_codes

print("Total AMFI Codes:", len(fund_codes))
print("Codes Available in NAV:", len(fund_codes) - len(missing_codes))
print("Missing AMFI Codes:", missing_codes)

if len(missing_codes) == 0:
    print("All AMFI codes are valid!")
else:
    print("Some AMFI codes are missing.")