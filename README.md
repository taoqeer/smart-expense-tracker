# Smart Expense Tracker

This is an expense tracker app that allows you to track your expenses and income. Its backend is built using Flask and
the frontend will be built using Angular.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User Authentication (Sign up, Login, Logout)
- Expense Logging (Manual entry and CSV upload)
- Expense Categorization
- Analytics Dashboard (Charts and Insights)
- Budgeting with Alerts
- Report Generation (PDF/Excel)
- Bank Account Integration (e.g., Plaid)
- Responsive Design

## Tech Stack

- **Frontend:** Angular
- **Backend:** Flask (Python)
- **Database:** PostgreSQL (for production) or SQLite (for development)
- **ORM:** SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)
- **APIs:** Plaid for bank integration
- **Visualization:** Chart.js or D3.js
- **Deployment:** Docker, AWS/Azure/Heroku

## Project Structure

```
smart-expense-tracker/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── expenses.py
│   │   └── utils/
│   ├── migrations/
│   ├── config.py
│   ├── requirements.txt
│   └── run.py
└── frontend/
    ├── src/
    │   ├── app/
    │   ├── assets/
    │   ├── environments/
    │   ├── index.html
    │   ├── main.ts
    │   └── styles.css
    ├── angular.json
    ├── package.json
    └── tsconfig.json
```

## Setup Instructions

### Backend

1. **Install Python 3.12+** if not already installed.
2. **Create a Virtual Environment:**
   ```bash
   cd backend
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Initialize the Database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```
5. **Run the Backend Server:**
   ```bash
   python run.py
   ```

### Frontend

1. **Install Node.js and npm** if not already installed.
2. **Install Angular CLI:**
   ```bash
   npm install -g @angular/cli
   ```
3. **Navigate to the frontend directory and install dependencies:**
   ```bash
   cd frontend
   npm install
   ```
4. **Run the Frontend Server:**
   ```bash
   ng serve
   ```

## Usage

1. **Register a new user** via the `/api/auth/register` endpoint.
2. **Login** to obtain a JWT token via the `/api/auth/login` endpoint.
3. **Use the JWT token** to authenticate requests to the expense management endpoints.

## API Endpoints

### User Authentication

- **Register**: `POST /api/auth/register`
- **Login**: `POST /api/auth/login`

### Expense Management

- **Get Expenses**: `GET /api/expenses`
- **Add Expense**: `POST /api/expenses`
- **Upload Expenses (CSV)**: `POST /api/expenses/upload`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
