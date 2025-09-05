from django.shortcuts import render
import joblib
import os

# Load model from 'data/' folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'data', 'house_price_model.pkl')
model = joblib.load(model_path)

def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == 'POST':
        size = float(request.POST['size'])
        bedrooms = int(request.POST['bedrooms'])
        bathrooms = float(request.POST['bathrooms'])

        prediction = model.predict([[size, bedrooms, bathrooms]])
        price = round(prediction[0], 2)

        return render(request, 'home.html', {'result': price})
    return render(request, 'home.html')
