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
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]

        # check login info
        if Login(session["username"], session["password"]).CheckLogin():
            return redirect(url_for("home"))
        else:
            # add a failed to login message in future
            return render_template("login.html")
    else:
        return render_template("login.html")


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
        else:
            return render_template("home.html")
    else:
        return render_template("home.html")


@app.route("/addTransaction", methods=["POST", "GET"])
def addTransaction():
    if request.method == "POST":
        date = request.form["date"]
        reason = request.form["reason"]
        amount = request.form["amount"]

        # try and add transaction
        if Transaction(session["username"]).AddTransaction(date, reason, amount):
            return redirect(url_for("home"))
        else:
            # add a failed to login message in future
            return render_template("addTransaction.html")
    else:
        return render_template("addTransaction.html")


@app.route("/viewTransaction", methods=["POST", "GET"])
def viewTransactions():
    return render_template("viewTransactions.html")



if __name__ == "__main__":
    app.run(debug=True)