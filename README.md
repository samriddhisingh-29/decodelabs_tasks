# 💰 Expense Tracker Web Application

A clean, modern, and beginner-friendly single-page Expense Tracker website built using **Python Flask**, **HTML5**, and **CSS3**.

Designed specifically for beginners, this project demonstrates core full-stack web concepts—such as handling HTTP GET & POST requests, server-side data validation, dynamic calculations, and responsive UI design—without the complexity of external databases, logins, or third-party APIs.

---

## 🎯 Project Objective

The primary objective of this project is to provide an easy-to-understand, lightweight web application for tracking daily spending. It helps beginners learn:
- How Flask handles form submissions (`GET` and `POST` methods).
- How to validate user inputs securely on the server.
- How to store state temporarily in memory using a simple Python list.
- How to render dynamic data and flash messages in HTML using Jinja2 templates.
- How to design a clean, responsive interface using modern CSS.

---

## ✨ Features

- **Single-Page Simplicity**: Everything happens on one intuitive screen with no page reloads needed for other views.
- **Add Expenses**: Easily enter an expense amount and an optional description (e.g., *Groceries, Coffee, Books*).
- **Dynamic Total Calculation**: Automatically calculates and displays the total amount spent across all entries in real time.
- **Expense History**: Displays every added expense in an organized list showing the title, timestamp, and amount.
- **Input Validation**: Ensures that the entered amount is a valid positive number greater than 0.
- **User-Friendly Error Alerts**: Shows clean, helpful error messages whenever invalid input is submitted.
- **Clear All Reset**: One-click "Clear All" button with a confirmation prompt to reset all expenses and reset the total spent to `$0.00`.
- **Individual Deletion**: Allows removing individual expense entries.
- **No Database Setup Required**: Stores all records in a straightforward in-memory Python list.
- **Responsive Modern Design**: Looks great on smartphones, tablets, laptops, and desktop screens.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3** | Core backend programming language |
| **Flask** | Lightweight Web Framework for routing & request handling |
| **Jinja2** | Server-side templating engine for rendering dynamic HTML |
| **HTML5** | Semantic structure for the web interface |
| **CSS3** | Modern, responsive styling with CSS variables and Flexbox/Grid |

---

## 📁 Project Structure

```text
expense-tracker/
├── app.py              # Main Flask application with routes and validation logic
├── requirements.txt    # Python dependencies list (Flask)
├── README.md           # Documentation, guide, and usage instructions
├── templates/
│   └── index.html      # Single-page HTML template with Jinja2 syntax
└── static/
    └── style.css       # Clean, modern, and responsive stylesheet
```

---

## 🚀 How to Install and Run

### 1. Prerequisites
Make sure you have **Python 3.8+** installed on your system. You can verify this by running:
```bash
python --version
```

### 2. Navigate to the Project Directory
Open your terminal or command prompt and enter the project folder:
```bash
cd expense-tracker
```

### 3. (Optional but Recommended) Create a Virtual Environment
```bash
# On Windows:
python -m venv venv
venv\Scripts\activate

# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
Install Flask from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 5. Run the Application
Start the Flask development server:
```bash
python app.py
```

### 6. View in Your Browser
Open your favorite web browser and visit:
```
http://127.0.0.1:5000/
```

---

## 💡 Example Usage

1. **Add Your First Expense**:
   - Description: `Morning Coffee`
   - Amount: `4.50`
   - Click **"Add Expense"**.
   - *Result*: The entry appears in your history, and **Total Spent** updates to `$4.50`.

2. **Add Another Expense**:
   - Description: `Groceries`
   - Amount: `32.75`
   - Click **"Add Expense"**.
   - *Result*: **Total Spent** dynamically updates to `$37.25`.

3. **Validation Test (Invalid Input)**:
   - Try submitting with an empty amount, `0`, or negative number like `-15`.
   - *Result*: A clear alert message appears: *"Expense amount must be a positive number greater than 0."* No invalid data is saved.

4. **Reset Expenses**:
   - Click **"Clear All"** at the top right of the expense list.
   - Confirm the prompt to reset your expenses and total back to `$0.00`.

---

## 📝 Beginner Notes

- **Data Persistence**: Because this project uses an in-memory Python list, restarting the Flask server will reset the expense list back to empty. This is intentional to keep the code beginner-friendly and eliminate database configuration headaches.
- **Extending the Project**: When you are ready to learn more advanced topics, you can expand this project by adding SQLite (`sqlite3` or `Flask-SQLAlchemy`), user authentication, or data export (CSV/PDF).

---

## 📄 License
This project is open-source and free to use for educational and personal projects.
