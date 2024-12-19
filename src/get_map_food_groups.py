import pandas as pd
import json


DATA_DIR_RELATIVE_PATH = "../data/"
DATASET_PATH = DATA_DIR_RELATIVE_PATH + "en.openfoodfacts.org.products.csv"


def main():
    COLS = [
        "pnns_groups_1",
        "pnns_groups_2",
    ]

    df = pd.read_csv(
            DATASET_PATH,
            sep="\t",
            usecols=COLS,
    ).dropna(subset=COLS)

    # Drop rows where any column contains "unknown" or something else that
    # does not make sense (e.g. "EMB 43089A")
    df = df[~df.isin(["unknown", "EMB 43089A"]).any(axis=1)]

    mapping: dict[str, list[str]] = {
        k: v.tolist()
        for k, v in df.groupby('pnns_groups_1')['pnns_groups_2'].unique().to_dict().items()
    }

    # write mapping group1 to group2
    with open(DATA_DIR_RELATIVE_PATH + "group1_to_group2.json", "w") as g1_to_g2_file:
        json.dump(
            mapping,
            g1_to_g2_file,
            indent=4,
            sort_keys=True,
        )

    # get inverse mapping
    inverse_mapping = {}
    for group1, group2_list in mapping.items():
        for group2 in group2_list:
            if group2 not in inverse_mapping:
                inverse_mapping[group2] = group1

    # write mapping group2 to group1
    with open(DATA_DIR_RELATIVE_PATH + "group2_to_group1.json", "w") as g2_to_g1_file:
        json.dump(
            inverse_mapping,
            g2_to_g1_file,
            indent=4,
            sort_keys=True,
        )

if __name__ == "__main__":
    main()
