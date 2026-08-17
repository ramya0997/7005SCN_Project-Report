import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ------------------------------------------
# Load Model & Scaler
# ------------------------------------------

model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_excel("Original File.xlsx", sheet_name="OriginalDataset")

# ------------------------------------------
# Create Label Encoders
# ------------------------------------------

label_encoders = {}

categorical_columns = [
    "product_name",
    "user_age_range",
    "user_gender",
    "Month",
    "packaging_quality",
    "product_discount",
    "location",
    "product_type",
    "sentiment"
]

for col in categorical_columns:
    encoder = LabelEncoder()
    encoder.fit(df[col])
    label_encoders[col] = encoder


# ------------------------------------------
# Prediction Function
# ------------------------------------------

def predict_recommendation(
    product_name,
    user_age_range,
    user_gender,
    month,
    product_rating,
    packaging_quality,
    product_price,
    product_discount,
    spent_time,
    ctr,
    location,
    product_type,
    sentiment,
    user_avg_rating,
    product_avg_rating
):

    try:

        # Encode categorical values

        product_name = label_encoders["product_name"].transform([product_name])[0]
        user_age_range = label_encoders["user_age_range"].transform([user_age_range])[0]
        user_gender = label_encoders["user_gender"].transform([user_gender])[0]
        month = label_encoders["Month"].transform([month])[0]
        packaging_quality = label_encoders["packaging_quality"].transform([packaging_quality])[0]
        product_discount = label_encoders["product_discount"].transform([product_discount])[0]
        location = label_encoders["location"].transform([location])[0]
        product_type = label_encoders["product_type"].transform([product_type])[0]
        sentiment = label_encoders["sentiment"].transform([sentiment])[0]

        # Create DataFrame in SAME order used during training

        input_df = pd.DataFrame([[
            product_name,
            user_age_range,
            user_gender,
            month,
            float(product_rating),
            packaging_quality,
            float(product_price),
            product_discount,
            float(spent_time),
            float(ctr),
            location,
            product_type,
            sentiment,
            float(user_avg_rating),
            float(product_avg_rating)
        ]], columns=[
            "product_name",
            "user_age_range",
            "user_gender",
            "Month",
            "product_rating",
            "packaging_quality",
            "product_price",
            "product_discount",
            "spent_time",
            " CTR (Click-Through Rate)",
            "location",
            "product_type",
            "sentiment",
            "user_avg_rating",
            "product_avg_rating"
        ])

        # Scale numerical features

        numerical_columns = [
            "product_rating",
            "product_price",
            "spent_time",
            " CTR (Click-Through Rate)",
            "user_avg_rating",
            "product_avg_rating"
        ]

        input_df[numerical_columns] = scaler.transform(
            input_df[numerical_columns]
        )

        # Prediction

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        if prediction == 1:
            result = "Recommended"
        else:
            result = "Not Recommended"

        return result, round(probability * 100, 2)

    except Exception as e:
        return f"Error: {str(e)}", 0