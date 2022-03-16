from flask import Flask, redirect, url_for, render_template, request , session

application = Flask(__name__)
application.secret_key ="123456789"

@application.route("/")
def home():
    return render_template("index.html")

@application.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"]=user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@application.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

@application.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    application.run(debug=True)
