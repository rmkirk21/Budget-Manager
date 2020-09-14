# Main code

from flask import Flask, redirect, url_for, render_template, request, session
from Account_Management import *
from Transaction_Management import *
from Budget_Management import *


app = Flask(__name__)
app.secret_key = "2020"


# create and run website
@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if "login" in request.form:
            session["username"] = request.form["username"]
            session["password"] = request.form["password"]

            # check login info
            if Login(session["username"], session["password"]).CheckLogin():
                return redirect(url_for("home"))
            else:
                # add a failed to login message in future
                return render_template("login.html")
        elif "signup" in request.form:
            return redirect(url_for("signup"))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        username = request.form["username"]
        password = request.form["password"]

        # create account
        if SignUp(fname, lname, username, password).CheckSignUp():
            return redirect(url_for("login"))
        else:
            return render_template("signup.html")
    else:
        return render_template("signup.html")


@app.route("/home", methods=["POST", "GET"])
def home():
    # get users transactions
    session["recent_transactions"] = Transaction(session["username"]).TransactionHistory()

    # transaction options
    if request.method == "POST":
        if "add_transaction" in request.form:
            return redirect(url_for("addTransaction"))
        elif "view_transactions" in request.form:
            return redirect(url_for("viewTransactions"))
        elif "view_previous_months" in request.form:
            return redirect(url_for("previousMonths"))
        elif "edit_budget" in request.form:
            return redirect(url_for("editBudget"))
        else:
            return render_template("home.html")
    else:
        return render_template("home.html")


@app.route("/logout", methods=["POST", "GET"])
def logout():
    if request.method == "POST":
        if "yes_logout" in request.form:
            session.clear()
            return redirect(url_for("login"))
        elif "no_logout" in request.form:
            return redirect(url_for("home"))
        else:
            return render_template("logout.html")
    else:
        return render_template("logout.html")


@app.route("/addTransaction", methods=["POST", "GET"])
def addTransaction():
    if request.method == "POST":
        date = request.form["date"]
        reason = request.form["reason"]
        amount = request.form["amount"]

        # try and add transaction
        if Transaction(session["username"]).AddTransaction(date, reason, amount):
            session["recent_transactions"] = Transaction(session["username"]).TransactionHistory()
            return redirect(url_for("home"))
        else:
            # add a failed to login message in future
            return render_template("addTransaction.html")
    else:
        return render_template("addTransaction.html")


@app.route("/viewTransaction", methods=["POST", "GET"])
def viewTransactions():
    session["recent_transactions"] = Transaction(session["username"]).TransactionHistory()
    return render_template("viewTransactions.html")


@app.route("/previousMonths", methods=["POST", "GET"])
def previousMonths():
    return render_template("previousMonths.html")


@app.route("/editBudget", methods=["POST", "GET"])
def editBudget():
    if request.method == "POST":
        if "add_budgetItem" in request.form:
            return redirect(url_for("addBudgetItem"))
        else:
            session["budget_items"] = Budget(session["username"]).get_budget_items()
            return render_template("editBudget.html")
    else:
        session["budget_items"] = Budget(session["username"]).get_budget_items()
        return render_template("editBudget.html")


@app.route("/addBudgetItem", methods=["POST", "GET"])
def addBudgetItem():
    if request.method == "POST":
        reason = request.form["reason"]
        value = request.form["value"]
        Budget(session["username"]).add_budget_item(reason, value)
        session["budget_items"] = Budget(session["username"]).get_budget_items()
        return redirect(url_for("editBudget"))
    else:
        return render_template("addBudgetItem.html")


if __name__ == "__main__":
    app.run(debug=True)