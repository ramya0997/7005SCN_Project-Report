import pandas as pd

# ------------------------------------------
# Load Dataset
# ------------------------------------------

DATASET_PATH = "Original File.xlsx"

try:
    df = pd.read_excel(DATASET_PATH, sheet_name="OriginalDataset")
except Exception as e:
    print(f"Dataset Loading Error: {e}")
    df = pd.DataFrame()


# ------------------------------------------
# Get Dropdown Values
# ------------------------------------------

def get_product_names():
    return sorted(df["product_name"].dropna().unique().tolist())


def get_age_ranges():
    return sorted(df["user_age_range"].dropna().unique().tolist())


def get_genders():
    return sorted(df["user_gender"].dropna().unique().tolist())


def get_months():
    return sorted(df["Month"].dropna().unique().tolist())


def get_packaging_quality():
    return sorted(df["packaging_quality"].dropna().unique().tolist())


def get_product_discount():
    return sorted(df["product_discount"].dropna().unique().tolist())


def get_locations():
    return sorted(df["location"].dropna().unique().tolist())


def get_product_types():
    return sorted(df["product_type"].dropna().unique().tolist())


def get_sentiments():
    return sorted(df["sentiment"].dropna().unique().tolist())


# ------------------------------------------
# Numeric Defaults
# ------------------------------------------

def get_default_product_rating():
    return round(df["product_rating"].mean(), 2)


def get_default_product_price():
    return round(df["product_price"].mean(), 2)


def get_default_spent_time():
    return round(df["spent_time"].mean(), 2)


def get_default_ctr():
    return round(df[" CTR (Click-Through Rate)"].mean(), 2)


def get_default_user_avg_rating():
    return round(df["user_avg_rating"].mean(), 2)


def get_default_product_avg_rating():
    return round(df["product_avg_rating"].mean(), 2)


# ------------------------------------------
# Recommend Similar Product
# ------------------------------------------

def get_similar_product(product_type):

    products = df[df["product_type"] == product_type]

    if products.empty:
        return None

    product = (
        products
        .sort_values(
            by=["product_avg_rating", "product_price"],
            ascending=[False, True]
        )
        .iloc[0]
    )

    return {
        "Product Name": product["product_name"],
        "Product Type": product["product_type"],
        "Price": product["product_price"],
        "Average Rating": product["product_avg_rating"],
        "Packaging": product["packaging_quality"],
        "Discount": product["product_discount"]
    }


# ------------------------------------------
# Get Dataset Information
# ------------------------------------------

def get_dataset_info():

    return {

        "Total Products": df["product_name"].nunique(),

        "Total Users": df["user_id"].nunique(),

        "Total Reviews": len(df),

        "Product Types": df["product_type"].nunique(),

        "Locations": df["location"].nunique()

    }