

# 🏡 House Price Prediction

A Django-based web application that predicts house prices based on user inputs such as size, number of bedrooms, and number of bathrooms.

## 📂 Project Structure

* **Project name**: `houseprice`
* **App name**: `predictor`
* **Model file**: `data/house_price_model.pkl`
* **Main view**: `views.py` (uses joblib to load the trained model)
* **Template**: `home.html`

## ⚙️ Features

* User-friendly form to enter house details.
* Predicts price instantly using a trained ML model.
* Simple Django app with modular code structure.

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/houseprice.git
cd houseprice
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate    # On Windows
source venv/bin/activate   # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, create one with:

```bash
pip freeze > requirements.txt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

Now open 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## 📊 Example Usage

* Input:

  * Size: `1200`
  * Bedrooms: `3`
  * Bathrooms: `2`
* Output:

  * Predicted Price: `250000.00`

## 📌 Tech Stack

* **Backend**: Django
* **Model**: Scikit-learn (loaded via joblib)
* **Frontend**: HTML (Django Templates)
