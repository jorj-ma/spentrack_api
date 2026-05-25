# spentrack_api
A secure and scalable Flask-based REST API powering the **SoenTrack** personal finance management platform.

The API enables users to:
- Register and authenticate accounts
- Manage expenses
- Track monthly budgets
- View financial summaries
- Analyze spending patterns
- Organize expenses by category

Built with a modular architecture using Flask Blueprints, JWT authentication, SQLAlchemy ORM, and database migrations.

---

# Features

## Authentication
- User registration
- Secure login
- JWT-based authentication
- Password hashing with bcrypt

## Expense Management
- Create expenses
- Retrieve all user expenses
- Update expenses
- Delete expenses

## Dashboard Analytics
- Total spending calculations
- Remaining budget tracking
- Recent expense activity
- Category spending breakdowns

## Budget Tracking
- Set monthly budgets
- Update budget limits
- Real-time budget summaries

## Categories
- Pre-seeded expense categories
- Categorized spending analytics

## User Profile Management
- View profile
- Update account information
- Delete account

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Flask | Web framework |
| Flask-SQLAlchemy | ORM/database management |
| Flask-Migrate | Database migrations |
| Flask-JWT-Extended | JWT authentication |
| Flask-Bcrypt | Password hashing |
| Flask-CORS | Cross-origin support |
| SQLAlchemy | ORM query abstraction |

---

# Project Structure

```text
spentrack_api/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── expenses.py
│   │   ├── budgets.py
│   │   ├── dashboard.py
│   │   ├── categories.py
│   │   └── user.py
│   │
│   └── utils/
│
├── migrations/
├── .env
├── requirements.txt
└── run.py
```

---

# Setup Instructions

## Clone Repository

```bash
git clone <repository-url>
cd spentrack_api
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

Activate virtual environment:

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
DATABASE_URL=your_database_path
```

---

# Database Setup

Initialize migrations:

```bash
flask db init
```

Create migration:

```bash
flask db migrate -m "Initial migration"
```

Apply migration:

```bash
flask db upgrade
```

---

# Running The Server

```bash
flask run
```

Server runs on:

```text
http://127.0.0.1:5000
```

---

# API Documentation

# Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Authenticate user |

---

# Expense Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/expenses` | Retrieve all user expenses |
| POST | `/expenses` | Add new expense |
| PUT | `/expenses/<id>` | Update expense |
| DELETE | `/expenses/<id>` | Delete expense |

---

# Budget Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/budgets/summary` | Retrieve budget summary |
| POST | `/budgets` | Set monthly budget |
| PUT | `/budgets/update` | Update budget limit |

---

# Dashboard Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/dashboard/summary` | Retrieve dashboard analytics |

---

# Category Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/categories` | Retrieve all categories |

---

# User Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/profile` | Retrieve user profile |
| PUT | `/profile` | Update user profile |
| DELETE | `/profile` | Delete user account |

---

# Authentication

Protected routes require a JWT token in the request header:

```http
Authorization: Bearer <your_token>
```

---

# Example Login Response

```json
{
  "token": "your-jwt-token",
  "user": {
    "id": 1,
    "name": "George",
    "email": "george@example.com"
  }
}
```

---

# Seed Data

The application includes predefined expense categories such as:
- Housing
- Food and Groceries
- Transportation
- Healthcare
- Entertainment
- Savings
- Utilities
- Education

---

# Error Handling

The API includes:
- Validation error handling
- Database rollback protection
- JWT authentication protection
- Unauthorized access prevention

---

# Future Improvements

- Refresh token support
- Advanced analytics
- Export financial reports
- Recurring expenses
- Notification system
- Multi-currency support
- AI-driven spending insights

---

# Author

## George Anzigale

Backend Developer • Frontend Development • Data Enthusiast

---

# License

This project is licensed under the MIT License.
