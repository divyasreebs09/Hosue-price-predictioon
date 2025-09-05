import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load dataset
csv_path = os.path.join(os.path.dirname(__file__), '_Synthetic House pricing dataset - Sheet1.csv')
df = pd.read_csv(csv_path)

# Features and target
X = df[['House Size (sqft)', 'Bedrooms', 'Bathrooms']]
y = df['Price (USD)']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model to data/ folder
model_path = os.path.join(os.path.dirname(__file__), 'house_price_model.pkl')
joblib.dump(model, model_path)

print("✅ Model trained and saved in 'data/house_price_model.pkl'")
