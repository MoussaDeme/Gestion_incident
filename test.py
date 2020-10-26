from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)

@app.route("/<name>")
def user(name):
    return "Hello "+name
@app.route("/admin")
def admin():
	return redirect(url_for("home"))
# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
	return render_template("index.html", content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ea sequi, itaque magnam inventore exercitationem sunt corporis dolorem blanditiis ab. Esse totam vel rem. Est alias impedit sit iste atque perspiciatis.")
if __name__ == "__main__":
    app.run()

