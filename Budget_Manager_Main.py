# Main code

from GUI import *
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "2020"


@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]
        return redirect(url_for("home"))
    else:
        return render_template("login.html")


@app.route("/home")
def home():
    user = request.args.get('username')
    return render_template("home.html", username=session["username"])


if __name__ == "__main__":
    app.run(debug=True)






































# Open GUI
# root = Tk()
# root.title("Budget Manager")
# root.geometry("600x500")
# app = GUI(root)
# root.mainloop()