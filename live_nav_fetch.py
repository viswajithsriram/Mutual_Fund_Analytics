import requests
import pandas as pd
import os

schemes = {
    "HDFC_Top_100": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

os.makedirs("data/raw", exist_ok=True)

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    response.raise_for_status()

    result = response.json()
    df = pd.DataFrame(result["data"])

    df["scheme_code"] = code
    df.to_csv(f"data/raw/{name}_NAV.csv", index=False)

    print(f"{name}: {df.shape} - Saved successfully!")

print("All NAV data downloaded!")