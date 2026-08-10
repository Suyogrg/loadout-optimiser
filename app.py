from flask import Flask, render_template, request, json

app = Flask(__name__)

def load_items():
    with open("items.json", "r") as file:
        data = json.load(file)

    return data

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":

        credits = int(request.form["credits"])
        selected_agent = request.form["agent"]

        items = load_items()

        filtered_items = []

        for item in items:
            if item.get("agent") == selected_agent or item.get("agent") == None:
                if item.get("cost") <= credits:
                    filtered_items.append(item)

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