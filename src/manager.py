import os
import pandas as pd

CLEAN_URL = "clean_url.csv"
FINAL_DATA = "final_data.csv"

def save_category_links_to_csv(category_links: list[str], *,  csv_file: str = CLEAN_URL):
    df_new = pd.DataFrame({
        "url": category_links
    })

    if os.path.exists(csv_file):
        df_existing = pd.read_csv(csv_file)
        df_merged = pd.concat([df_existing, df_new], ignore_index=True).drop_duplicates()
    else:
        df_merged = df_new

    df_merged = df_merged.dropna(axis=0, how='all')

    df_merged.to_csv(csv_file, index=False)
    print(f"[DATA_MANAGER] Données sauvegardées dans '{csv_file}' avec {len(df_merged)} lignes.")


def load_csv_column_as_list(column_name: str, *,  csv_file: str = CLEAN_URL) -> list[str]:
    if not os.path.exists(csv_file):
        print(f"[DATA_MANAGER] Fichier '{csv_file}' introuvable.")
        return []
    df = pd.read_csv(csv_file)
    if column_name not in df.columns:
        print(f"[DATA_MANAGER] Colonne '{column_name}' non trouvée dans '{csv_file}'.")
        return []
    return df[column_name].dropna().tolist()


def save_vendor_data_to_csv(vendor_data: dict, *, csv_file: str = FINAL_DATA):
    df_new = pd.DataFrame([vendor_data])
    if os.path.exists(csv_file):
        df_existing = pd.read_csv(csv_file)
        df_merged = pd.concat([df_existing, df_new], ignore_index=True).drop_duplicates()
    else:
        df_merged = df_new

    # df_merged = df_merged.dropna(axis=0, how='all')
    # df_merged = df_merged.dropna(axis=1, how='all')

    df_merged.to_csv(csv_file, index=False)
    print(f"[DATA_MANAGER] Données du vendeur sauvegardées dans '{csv_file}' avec {len(df_merged)} lignes.")
