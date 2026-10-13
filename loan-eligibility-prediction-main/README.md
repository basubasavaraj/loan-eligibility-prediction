Loan Eligibility Prediction Using Logistic Regression

1. Project Overview

This project uses Machine Learning to predict loan eligibility based on a person's CIBIL score and required loan amount.

2. Objective

To build a Logistic Regression classification model that predicts whether an applicant is eligible or not eligible for a loan.

3. Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Logistic Regression

4. Dataset

The "loan_data.csv" file contains the following columns:

- "CIBIL_Score": Applicant's credit score
- "Loan_Amount": Required loan amount in rupees
- "Eligible": Target label (1 = eligible, 0 = not eligible)

The included dataset is synthetic sample data created for educational purposes.

5. Project Files

- "loan_prediction.py" — trains the model, predicts eligibility, and plots the data.
- "loan_data.csv" — sample dataset.
- "requirements.txt" — required Python libraries.
- "README.md" — project documentation.

6. Installation

Install Python, then open a terminal in the project folder and run:

pip install -r requirements.txt

7. Execution

Run the program with:

python loan_prediction.py

Enter the CIBIL score and loan amount when prompted. The program displays a prediction and plots the sample applicants.

8. Visualization

- X-axis: CIBIL score
- Y-axis: Loan amount required
- Green points: Eligible sample applicants
- Red points: Ineligible sample applicants

9. Limitation

This is an educational demonstration using a small synthetic dataset. Predictions are not suitable for real loan approval decisions.
