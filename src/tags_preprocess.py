import pandas as pd
from countries import country_acronyms, region_country, subregion_country

# Constants
DATA_DIR_RELATIVE_PATH = "../data/"

DATASET_PATH = "en.openfoodfacts.org.products.csv"

# Read columns and drop NaN values
COLUMNS = [
    "product_name",
    "origins_tags",   # Ingredient Origin
    "manufacturing_places_tags", # Manufacturing
    "countries_tags", # Consumption Place
]

df = pd.read_csv(
    DATA_DIR_RELATIVE_PATH+DATASET_PATH,
    usecols=COLUMNS,
    sep="\t",
    on_bad_lines='skip',
    nrows=100,
).dropna(subset=COLUMNS)  # Drop rows with any NaN

# split tags string by comma into a list and
# remove language prefixes (if any) (e.g. 'en', 'fr') for each tag
# and replace every '-' with ' '
df["tags_split"] = df["countries_tags"].apply(
    lambda tags: [
        tag.strip()[3:].replace("-", " ")
        if ":" in tag
        else tag.strip().replace("-", " ")
        for tag in tags.split(',')
    ]
)

# explode dataframe around the list of tags
df_explode_origins = df.explode("tags_split")

# new dataframe contains only rows for which origin tag have not been translated by 'country_acronyms' yet
df_unlisted = df_explode_origins[~df_explode_origins["tags_split"].isin(country_acronyms.get_all_elts())]

# count occurrences of each unlisted tag
df_value = df_unlisted.value_counts("tags_split", dropna=False)

for country, count in df_value.items():
    print(f"{count}\t\t\"{country}\"")