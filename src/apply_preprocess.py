import pandas as pd
from countries import country_acronyms as acronyms
from typing import Optional

DATA_DIR_RELATIVE_PATH = "../data/"
DATASET_PATH = DATA_DIR_RELATIVE_PATH + "en.openfoodfacts.org.products.csv"


def read_csv_and_drop_na(nrows: Optional[int] = None) -> pd.DataFrame:
    COLUMNS = [
        "product_name",
        "origins_tags",  # Ingredient Origin
        "manufacturing_places_tags",  # Manufacturing
        "countries_tags",  # Consumption Place
        "pnns_groups_2", # Product most precise classification (e.g. "Meat" or "Fruits")
    ]

    return pd.read_csv(
        DATASET_PATH,
        usecols=COLUMNS,
        sep="\t",
        on_bad_lines="skip",
        nrows=nrows,
    ).dropna(
        subset=COLUMNS
    )  # Drop rows with any NaN


def split_and_remove_prefix_and_dashes(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Split tags in the given column and remove the two-letter prefix (if present)
    for each tag. Also replace all dashes by spaces.
    """

    df_ = df.copy()

    df_[f"{col}_std"] = df_[col].apply(
        lambda tags: [
            (
                tag.strip()[3:].replace("-", " ")
                if ":" in tag
                else tag.strip().replace("-", " ")
            )
            for tag in tags.split(",")
        ]
    )
    return df_


def alternative_to_standard(df: pd.DataFrame, col: str):
    """Create a new column `{col}_str` which contains the list of tags with their
    standard version (as defined in countries.py) or prefixed by 'NF:' if they
    does not have a standard version.
    """

    df_ = df.copy()

    df_[f"{col}_std"] = df_[f"{col}_std"].apply(
        lambda tags: [acronyms.get_group(tag, f"NF:{tag}") for tag in tags]
    )
    return df_


def filter_out_rows_without_standard(
    df: pd.DataFrame, columns: list[str]
) -> pd.DataFrame:
    """Filter out all rows in the dataframe which have at least one
    element in one of its `columns` prefixed by "NF:".
    This "NF:" prefixed means "Not Found" and is introduced by
    `alternative_to_standard()`.
    """

    df_ = df.copy()

    mask = ~df_[columns].apply(
        lambda row: any(
            any(str(val).startswith("NF:") for val in col_list) for col_list in row
        ),
        axis=1,
    )
    filtered_df = df_[mask]
    return filtered_df


def main():
    df = read_csv_and_drop_na(nrows=None)

    # remove rows where pnns_groups_2 is either 'unknown' or 'EMB 43089A'
    df = df[~df.isin(["unknown", "EMB 43089A"]).any(axis=1)]

    columns_to_work = ["origins_tags", "manufacturing_places_tags", "countries_tags"]
    for col in columns_to_work:
        # split origins tags in a list, and remove prefix (if any) for each tag in the list
        df = split_and_remove_prefix_and_dashes(df, col)

        # replace every alternative names with it's standard name as defined in country_acronyms
        df = alternative_to_standard(df, col)

    # filter out rows containing "NF:"
    # Create a mask that checks ALL specified columns
    columns_filtered = [col + "_std" for col in columns_to_work]
    filtered_df = filter_out_rows_without_standard(df, columns_filtered)

    # print(filtered_df.head())
    # print(filtered_df.shape)

    # filtered_df.to_csv(
    #     DATA_DIR_RELATIVE_PATH + "cleaned_data_v2.csv",
    #     sep=",",
    #     columns=[
    #         "product_name",
    #         "origins_tags_std",
    #         "manufacturing_places_tags_std",
    #         "countries_tags_std",
    #     ],
    #     index=False,
    # )

    filtered_df[["product_name", "origins_tags_std", "manufacturing_places_tags_std", "countries_tags_std", "pnns_groups_2"]].to_json(
        DATA_DIR_RELATIVE_PATH + "cleaned_data_v2.json",
        orient="records",
        indent=4,
    )

    # def count_tags(tags_l):
    #     if not isinstance(tags_l, list):
    #         return 0
    #     tags = [tag.strip() for tag in tags_l if tag.strip()]
    #     return len(tags)

    # ddf = df[
    #     (df["countries_tags_std"].apply(count_tags) > 1)
    #     | (df["origins_tags_std"].apply(count_tags) > 1)
    #     | (df["manufacturing_places_tags_std"].apply(count_tags) > 1)
    # ]

    return filtered_df


if __name__ == "__main__":
    main()
