from flask import Flask, render_template, request
from item_loader import load_items, get_items

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":

        credits = int(request.form["credits"])
        selected_agent = request.form["agent"]

        items = load_items()
        filtered_items = get_items(items, credits, selected_agent)

        return render_template(
            "index.html",
            credits=credits,
            selected_agent=selected_agent,
            items=filtered_items
        )
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)