import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("loan_data.csv")

# Prepare training data
X = data[["CIBIL_Score", "Loan_Amount"]]
y = data["Eligible"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Get user input
print("Loan Eligibility Prediction")
cibil = int(input("Enter CIBIL score: "))
amount = float(input("Enter loan amount in rupees: "))

# Make prediction
input_data = pd.DataFrame(
    [[cibil, amount]],
    columns=["CIBIL_Score", "Loan_Amount"]
)

prediction = model.predict(input_data)

if prediction[0] == 1:
    print("Prediction: Eligible")
else:
    print("Prediction: Not Eligible")

plt.scatter(
    data["CIBIL_Score"],
    data["Loan_Amount"],
    c=data["Eligible"],
    cmap="coolwarm"
)

plt.xlabel("CIBIL Score")
plt.ylabel("Loan Amount (₹)")
plt.title("Loan Eligibility Dataset")
plt.colorbar(label="Eligible (0 = No, 1 = Yes)")
plt.grid(True)
plt.show()
