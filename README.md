# 💼 Investment Portfolio Management System

A secure and scalable backend system for managing investment portfolios, built using Django Rest Framework (DRF). This project supports real-time portfolio tracking, user authentication, financial data integration, and paid membership via Razorpay.

---

## 🚀 Features

- 🔐 **Token-Based Authentication**: Ensures secure access to user-specific portfolio data.
- 📊 **Dynamic Portfolio Management**: Users can create, update, and monitor their investment portfolios.
- 🌐 **Real-Time Market Data**: Integrated third-party APIs to fetch up-to-date financial data.
- 💳 **Paid Memberships with Razorpay**: Seamless payment integration for premium features.
- 🧪 **API Testing**: Fully tested using Postman collections.

---

## 🛠️ Tech Stack

- **Backend**: Django Rest Framework (DRF)
- **Database**: SQLite
- **Auth**: Token-based Authentication (DRF’s TokenAuth)
- **APIs**: Third-party Financial APIs 
- **Payments**: Razorpay API
- **Testing**: Postman
- **Version Control**: Git + GitHub

---

## 🏗️ Project Structure

```plaintext
finance/
│
├── finance/                 # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── portfolioapp/            # Core portfolio app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── forms.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│
├── db.sqlite3               # SQLite database
└── manage.py                # Django management script

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mehekmehta06/investment-portfolio.git
cd investment-portfolio-api

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Requirements

```bash
pip install -r requirements.txt

### 4. Apply Migrations

```bash
python manage.py migrate

### 5. Run the Server

```bash
python manage.py runserver
