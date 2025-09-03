import os
import pandas as pd
from config import settings

CATEGORY_LINKS_FILE = settings.CATEGORY_LINKS_FILE
VENDOR_DATA_OUTPUT_FILE = settings.VENDOR_DATA_OUTPUT_FILE
LIVRABLE_FILE = settings.LIVRABLE_FILE
FILES_TO_MERGE = settings.FILES_TO_MERGE

def save_category_links_to_csv(category_links: list[str], *,  csv_file: str = CATEGORY_LINKS_FILE):
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


def load_csv_column_as_list(column_name: str, *,  csv_file: str = CATEGORY_LINKS_FILE) -> list[str]:
    if not os.path.exists(csv_file):
        print(f"[DATA_MANAGER] Fichier '{csv_file}' introuvable.")
        return []
    df = pd.read_csv(csv_file)
    if column_name not in df.columns:
        print(f"[DATA_MANAGER] Colonne '{column_name}' non trouvée dans '{csv_file}'.")
        return []
    return df[column_name].dropna().tolist()


def save_vendor_data_to_csv(vendor_data: dict, *, csv_file: str = VENDOR_DATA_OUTPUT_FILE):
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


def split_csv_into_three_files(*, csv_file: str = CATEGORY_LINKS_FILE) -> list[str]:
    output_files = [f"{os.path.splitext(csv_file)[0]}_part{i+1}.csv" for i in range(3)]

    if all(os.path.exists(f) for f in output_files):
        print(f"[DATA_MANAGER] Les fichiers existent déjà : {output_files}")
        return output_files

    if not os.path.exists(csv_file):
        print(f"[DATA_MANAGER] Fichier source '{csv_file}' introuvable.")
        return []

    df = pd.read_csv(csv_file)
    total_rows = len(df)
    if total_rows == 0:
        print(f"[DATA_MANAGER] Fichier source '{csv_file}' vide, rien à diviser.")
        return []

    base_chunk_size = total_rows // 3
    remainder = total_rows % 3

    start = 0
    for i in range(3):
        end = start + base_chunk_size + (1 if i < remainder else 0)
        df_chunk = df.iloc[start:end]
        df_chunk.to_csv(output_files[i], index=False)
        print(f"[DATA_MANAGER] Fichier créé : '{output_files[i]}' ({len(df_chunk)} lignes)")
        start = end

    return output_files


def merge_three_csv_files(file_list: list[str] = FILES_TO_MERGE, output_file: str = LIVRABLE_FILE):
    for f in file_list:
        if not os.path.exists(f):
            print(f"[DATA_MANAGER] Fichier '{f}' introuvable, fusion annulée.")
            return ""

    dfs = [pd.read_csv(f) for f in file_list]
    df_merged = pd.concat(dfs, ignore_index=True)

    df_merged = df_merged.drop_duplicates()

    df_merged = df_merged.dropna(axis=0, how='all')

    df_merged.to_csv(output_file, index=False)
    print(f"[DATA_MANAGER] Fichiers fusionnés et sauvegardés dans '{output_file}' avec {len(df_merged)} lignes.")

    return output_file
