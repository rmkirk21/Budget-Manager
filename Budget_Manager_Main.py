# Main code

from GUI import *
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return redirect(url_for("home"))
    else:
        return render_template("login.html")


@app.route("/home")
def home():
    user = request.args.get('username')
    return render_template("home.html", username=user)


if __name__ == "__main__":
    app.run(debug=True)






































# Open GUI
# root = Tk()
# root.title("Budget Manager")
# root.geometry("600x500")
# app = GUI(root)
# root.mainloop()