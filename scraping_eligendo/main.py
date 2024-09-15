import requests
import pandas as pd
from province import province

headers = {
    "Referer": "https://elezioni.interno.gov.it/"
}

def main():
    df = get_data()

    df[
        [
            "pref_silvia", 
            "pref_marcello", 
            "dati_presenti"
        ]
    ] = df.apply(lambda row: fill_row(row["codice"], row.name, len(df)), axis=1, result_type='expand')
    
    df.to_csv("../dati/insieme_with_votes.csv", index=False)

def get_data() -> pd.DataFrame:
    df = pd.read_csv("../dati/insieme.csv")
    df = df[df["desc_prov"].isin(province)].reset_index(drop=True)
    return df

def get_votes_from_json(data: dict, candidate_surname: str) -> int:
    return [x for x in data["cand"] if x["cogn"] == candidate_surname][0]["voti"]

def fill_row(codice: int, row_index: int, total_rows: int):
    codice_provincia_comune = str(codice)[-7:]
    provincia = codice_provincia_comune[:3]
    comune = codice_provincia_comune[-4:]

    url = f"https://eleapi.interno.gov.it/siel/PX/prefeEI/DE/20240609/TE/01/PR/{provincia}/CM/{comune}/AG/0008"

    try:
        output = requests.get(url, headers=headers).json()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return (0, 0, 0)

    preferenze_silvia = get_votes_from_json(output, "PANINI")
    preferenze_marcello = get_votes_from_json(output, "SALTARELLI")

    print(f"{row_index + 1}/{total_rows}, comune: {codice}, preferenze Silvia: {preferenze_silvia}, preferenze Marcello {preferenze_marcello}")

    return (preferenze_silvia, preferenze_marcello, 1)

if __name__ == "__main__":
    main()
