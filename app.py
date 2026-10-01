"""
Simple Beginner-Friendly Expense Tracker Web Application
Built with Python Flask, HTML, and CSS.

This application stores expenses in session / an in-memory Python list.
No database or external services required.
"""

import importlib.util
import os
import pkgutil
import re
import sys
import threading
import webbrowser
from datetime import datetime

# --------------------------------------------------------------------------
# Python 3.14+ Compatibility Shim
# In Python 3.14, pkgutil.get_loader was removed. This ensures Flask runs smoothly.
# --------------------------------------------------------------------------
if not hasattr(pkgutil, "get_loader"):
    def _get_loader(name):
        spec = importlib.util.find_spec(name)
        return spec.loader if spec else None
    pkgutil.get_loader = _get_loader

from flask import Flask, flash, redirect, render_template, request, session, url_for

# Initialize the Flask application
# Passing instance_path explicitly avoids Flask calling auto_find_instance_path()
app = Flask(__name__, instance_path=os.path.abspath(os.path.dirname(__file__)))

# Secret key required by Flask for session management and flash messages
app.secret_key = "beginner-friendly-expense-tracker-secret-key-12345"

# In-memory data store as fallback
memory_expenses = []


def get_expenses():
    """
    Returns current expenses from Flask session (with fallback to in-memory list).
    Using session ensures each browser preserves its own data across reloads.
    """
    if "expenses" in session and isinstance(session["expenses"], list):
        return session["expenses"]
    return memory_expenses


def save_expenses(expenses_list):
    """Saves updated expenses list into session and memory."""
    session["expenses"] = expenses_list
    session.modified = True
    global memory_expenses
    memory_expenses = expenses_list


def calculate_total(expenses_list):
    """Calculates total expenses dynamically."""
    return round(sum(item["amount"] for item in expenses_list), 2)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route:
    - GET: Renders the single-page Expense Tracker with current expenses and total.
    - POST: Allows adding an expense directly from the root route.
    """
    if request.method == "POST":
        return handle_add_expense()

    current_expenses = get_expenses()
    total_spent = calculate_total(current_expenses)

    return render_template(
        "index.html",
        expenses=current_expenses,
        total_spent=total_spent
    )


@app.route("/add", methods=["GET", "POST"])
def add_expense():
    """
    Explicit route to add a new expense item.
    """
    if request.method == "GET":
        return redirect(url_for("index"))

    return handle_add_expense()


def handle_add_expense():
    """
    Validates expense input and appends the new expense.
    """
    current_expenses = list(get_expenses())

    # Extract form inputs and strip whitespace
    raw_amount = request.form.get("amount", "").strip()
    title = (request.form.get("title") or request.form.get("description") or "").strip()

    # Sanitize currency symbols and commas (e.g., "$25.50" -> "25.50")
    cleaned_amount = re.sub(r"^[^\d.]+", "", raw_amount).replace(",", "").strip()

    # 1. Validation: Check for empty input
    if not cleaned_amount:
        flash("Please enter an expense amount.", "error")
        return redirect(url_for("index"))

    # 2. Validation: Validate that amount is a valid positive number
    try:
        amount = float(cleaned_amount)
        if amount <= 0:
            flash("Expense amount must be a positive number greater than 0.", "error")
            return redirect(url_for("index"))
    except ValueError:
        flash("Invalid amount entered. Please enter a valid numerical value (e.g., 25.50).", "error")
        return redirect(url_for("index"))

    # Fallback title if user leaves title blank
    if not title:
        title = f"Expense #{len(current_expenses) + 1}"

    # Formatted timestamp for display
    current_time = datetime.now().strftime("%b %d, %Y - %I:%M %p")

    # Create new expense record
    new_expense = {
        "id": int(datetime.now().timestamp() * 1000),  # Unique timestamp ID
        "title": title,
        "amount": round(amount, 2),
        "date": current_time
    }

    # Append to list and save
    current_expenses.append(new_expense)
    save_expenses(current_expenses)

    flash(f"Successfully added '{title}' (${amount:.2f})!", "success")
    return redirect(url_for("index"))


@app.route("/clear", methods=["GET", "POST"])
def clear_expenses():
    """
    Route to reset all expenses and total spent back to zero.
    """
    save_expenses([])
    flash("All expenses have been cleared successfully.", "info")
    return redirect(url_for("index"))


@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    """
    Route to delete a single expense item by its unique ID.
    """
    current_expenses = [item for item in get_expenses() if item["id"] != expense_id]
    save_expenses(current_expenses)
    flash("Expense deleted.", "info")
    return redirect(url_for("index"))


def open_browser():
    """Automatically opens the website in the user's default browser."""
    try:
        webbrowser.open_new("http://127.0.0.1:5000")
    except Exception:
        pass


if __name__ == "__main__":
    # Clean ASCII banner (safe on all Windows consoles without UnicodeEncodeError)
    print("\n" + "=" * 60)
    print("EXPENSE TRACKER IS LIVE AND RUNNING!")
    print("Website URL: http://127.0.0.1:5000")
    print("Opening your web browser automatically...")
    print("   (If it doesn't open, visit: http://127.0.0.1:5000)")
    print("To stop the server at any time, press CTRL+C")
    print("=" * 60 + "\n")

    # Automatically launch browser after 1.2 seconds so server is ready
    threading.Timer(1.2, open_browser).start()

    # Run Flask server (use_reloader=False prevents restarting or opening browser twice)
    app.run(debug=True, host="127.0.0.1", port=5000, use_reloader=False)
