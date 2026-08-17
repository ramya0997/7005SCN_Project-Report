# Machine Learning-Based Product Recommendation System

## 1. Project Overview

The **Machine Learning-Based Product Recommendation System** is a Python desktop application that predicts whether a beauty product should be recommended to a customer.

The system uses customer, product, behavioural and review-related information as input features. A trained machine learning model processes these inputs and returns:

- **Recommended** or **Not Recommended**
- Prediction confidence
- A suitable similar product when the prediction is positive

The application provides a graphical user interface (GUI) built with **Tkinter**.

---

## 2. Project Objectives

The main objectives of the project are:

1. Predict product recommendation outcomes using machine learning.
2. Analyse customer and product characteristics.
3. Use customer review sentiment as a recommendation feature.
4. Provide an easy-to-use desktop GUI for prediction.
5. Display a suitable product recommendation based on product type.
6. Support evidence-based product selection.

---

## 3. Main Features

### Prediction
The application predicts whether the selected product is recommended based on the supplied customer and product information.

### Customer and Product Inputs

The system accepts:

- Product Name
- Product Type
- User Age Range
- User Gender
- Month
- Packaging Quality
- Product Discount
- Location
- Sentiment
- Product Rating
- Product Price
- Spent Time
- Click-Through Rate (CTR)
- User Average Rating
- Product Average Rating

### Recommendation Panel

When the prediction is **Recommended**, the application can display details of a similar/high-rated product, including:

- Product Name
- Product Type
- Price
- Packaging Quality
- Average Rating
- Discount

### Additional GUI Functions

The application includes:

- Predict Recommendation
- Clear
- About
- Exit

---

## 4. System Architecture

The project follows a simple machine-learning application architecture:

```text
User
  |
  v
Tkinter GUI (gui.py)
  |
  v
Input Validation
  |
  v
Prediction Module (predictor.py)
  |
  +--> Label Encoding
  |
  +--> Numerical Feature Scaling
  |
  +--> Trained ML Model (best_model.pkl)
  |
  v
Recommendation Result
  |
  +--> Recommended / Not Recommended
  |
  +--> Confidence
  |
  +--> Similar Product
```

---

## 5. Project Files

| File | Description |
|---|---|
| `main.py` | Starts the desktop application. |
| `gui.py` | Contains the Tkinter graphical user interface. |
| `predictor.py` | Loads the trained model and performs predictions. |
| `utils.py` | Loads the dataset and provides dropdown values, defaults and product recommendation functions. |
| `about.py` | Displays the project information window. |
| `best_model.pkl` | Trained machine learning model. |
| `scaler.pkl` | Saved numerical feature scaler used during prediction. |
| `Original File.xlsx` | Main dataset used by the application. |
| `requirements.txt` | Python package dependencies. |

---

## 6. Technologies Used

### Programming Language
- Python

### GUI
- Tkinter
- ttk

### Data Processing
- Pandas
- NumPy
- OpenPyXL

### Machine Learning
- Scikit-learn
- Joblib

### Visualisation / Supporting Libraries
- Matplotlib
- Seaborn
- Pillow

---

## 7. Machine Learning Process

The prediction process is implemented in `predictor.py`.

### Step 1: Load the Model

The saved model is loaded from:

```text
best_model.pkl
```

### Step 2: Load the Scaler

The saved scaler is loaded from:

```text
scaler.pkl
```

### Step 3: Load the Dataset

The application reads:

```text
Original File.xlsx
```

and uses the `OriginalDataset` worksheet.

### Step 4: Encode Categorical Features

Categorical variables are converted into numerical values using `LabelEncoder`.

The categorical variables include:

- Product name
- User age range
- User gender
- Month
- Packaging quality
- Product discount
- Location
- Product type
- Sentiment

### Step 5: Scale Numerical Features

The following numerical features are scaled using the saved scaler:

- Product rating
- Product price
- Spent time
- CTR
- User average rating
- Product average rating

### Step 6: Generate Prediction

The trained model generates a binary prediction:

```text
1 = Recommended
0 = Not Recommended
```

The application also obtains the probability of the positive class and displays it as prediction confidence.

---

## 8. Dataset

The application expects the following dataset file:

```text
Original File.xlsx
```

The required worksheet is:

```text
OriginalDataset
```

The application uses customer/product information including product characteristics, ratings, price, behaviour, sentiment, location and recommendation-related variables.

The project information window describes the dataset as a beauty product review dataset containing customer reviews, beauty products and users.

---

## 9. Requirements

Recommended Python version:

```text
Python 3.10+
```

Install the dependencies using:

```bash
pip install -r requirements.txt
```

The supplied `requirements.txt` contains the required package versions.

---

## 10. Installation

### Step 1: Extract the Project

Extract the project folder to a suitable location.

### Step 2: Open a Terminal

Open Command Prompt, PowerShell or the terminal in your IDE.

Navigate to the project folder:

```bash
cd "MACHINE LEARNING-BASED PRODUCT RECOMMENDATION SYSTEM"
```

### Step 3: Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

### Step 4: Check Required Files

Make sure these files are located in the same project directory:

```text
main.py
gui.py
predictor.py
utils.py
about.py
best_model.pkl
scaler.pkl
Original File.xlsx
requirements.txt
```

### Step 5: Run the Application

Run:

```bash
python main.py
```

The Tkinter application window should open.

---

## 11. How to Use the Application

1. Start the application using `python main.py`.
2. Select the required categorical values from the dropdown menus.
3. Check or modify the numerical values.
4. Click **Predict Recommendation**.
5. The system validates the entered information.
6. The trained machine learning model generates a prediction.
7. The application displays:
   - Recommendation Status
   - Confidence percentage
8. If the result is **Recommended**, the recommendation panel displays a suitable product.
9. Use **Clear** to reset the input fields.
10. Use **About** to view project information.
11. Use **Exit** to close the application.

---

## 12. Use Case Summary

### Primary Actor

**Customer/User**

### Main Use Cases

- Open Product Recommendation System
- Enter Customer Information
- Enter Product Information
- Predict Recommendation
- View Recommendation Result
- View Confidence
- View Similar Product
- Clear Inputs
- View About Information
- Exit Application

### Basic Use Case Flow

```text
Customer/User
     |
     v
Open Application
     |
     v
Enter/Select Product & Customer Information
     |
     v
Validate Inputs
     |
     v
Predict Recommendation
     |
     v
View Result and Confidence
     |
     +---- Recommended ----> View Similar Product
     |
     +---- Not Recommended -> Display Result
```

---

## 13. Error Handling

The application includes validation for:

- Missing dropdown selections
- Missing numerical values
- Invalid numerical values
- Missing dataset
- Dataset loading errors
- Prediction errors

If the dataset cannot be loaded, the application displays a dataset error message.

---

## 14. Troubleshooting

### Dataset Error

If you receive a dataset loading error, check that:

```text
Original File.xlsx
```

exists in the same directory as `main.py`.

Also confirm that the Excel workbook contains:

```text
OriginalDataset
```

as the worksheet name.

### Model Loading Error

If `best_model.pkl` cannot be loaded, check that the file exists in the project directory.

### Scaler Loading Error

If `scaler.pkl` cannot be loaded, ensure that the saved scaler is present in the project directory.

### Module Not Found Error

Install the dependencies again:

```bash
pip install -r requirements.txt
```

### Windows Python Command Issue

If `python` is not recognised, try:

```bash
py main.py
```

---

## 15. Running from Visual Studio / IDE

If using an IDE such as Visual Studio or another Python-compatible IDE:

1. Open the project folder.
2. Select the Python interpreter/environment.
3. Install packages from `requirements.txt`.
4. Make sure the working directory is the project folder.
5. Run `main.py`.

The working directory is important because the application loads the dataset, model and scaler using relative file paths.

---

## 16. Expected Output

After valid inputs are supplied, the application displays a result similar to:

```text
Recommendation Status

Recommended

Confidence: XX.XX%
```

If the prediction is positive, the recommended product panel can display:

```text
Product Name
Product Type
Price
Packaging Quality
Average Rating
Discount
```

---

## 17. Important Notes

- Do not rename `Original File.xlsx` unless the file paths in the Python code are also updated.
- Do not rename the `OriginalDataset` worksheet without updating the Python code.
- Keep `best_model.pkl` and `scaler.pkl` in the project directory.
- The saved scaler should correspond to the numerical features used when the model was trained.
- The application is designed as a desktop machine learning prototype and requires Python to run.

---

## 18. Academic Project

**Project Title:**  
Machine Learning-Based Product Recommendation System Using Customer Reviews and Machine Learning

**Application Type:**  
Python Desktop Application

**Academic Year:**  
2026

**Purpose:**  
Academic / Master's Dissertation Project

---

## 19. License

This project is intended for academic and educational use. Any dataset, third-party library or external resource included with the project remains subject to its respective licence and usage terms.
