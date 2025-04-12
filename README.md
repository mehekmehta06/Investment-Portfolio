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
- **APIs**: Third-party Financial APIs (e.g., Alpha Vantage / Finnhub / yFinance)
- **Payments**: Razorpay API
- **Testing**: Postman
- **Version Control**: Git + GitHub

---

## 📁 Project Structure

```bash
investment-portfolio/
│
├── core/                  # Django project settings
├── portfolio/             # Portfolio app (models, serializers, views, urls)
├── users/                 # User management and auth
├── payments/              # Razorpay integration logic
├── requirements.txt       # Python dependencies
├── manage.py              # Django CLI
└── README.md              # This file
