from flask import Flask, render_template, url_for, redirect
from cupcake import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("display-cakes.csv"))

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html", cupcakes = get_cupcakes("display-cakes.csv"))

@app.route("/cupcake_individual")
def inidividual_cupcakes():
    return render_template("individual-cupcake.html", cupcakes = get_cupcakes("display-cakes.csv"))

@app.route("/order")
def order_cupcakes():
    return render_template("order.html", cupcakes = get_cupcakes("orders.csv"))

@app.route("/add_cupcake/<name>")
def add_a_cupcake(name):
    cupcake = find_cupcake("display-cakes.csv", name)
    print(cupcake)
    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home")) 
    else:
        return "Sorry cupcake not found."


if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")

