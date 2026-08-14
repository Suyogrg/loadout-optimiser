from flask import Flask, render_template, request
from item_loader import load_items
from loadout_service import get_agents, generate

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    items = load_items()
    agents = get_agents(items)

    if request.method == "POST":
        errors = []

        try:
            credits = int(request.form.get("credits"))
            if credits < 0:
                errors.append("Credits cannot be negative.")
            if credits > 9000:
                errors.append("Credits cannot be over 9,000.")
        except ValueError:
            errors.append("Invalid credits.")

        agent = request.form.get("agent")
        if not agent or agent not in agents:
            errors.append("Invalid agent.")

        weights = {
            "offensive": int(request.form.get("offensive"))/100,
            "defensive": int(request.form.get("defensive"))/100,
            "utility": int(request.form.get("utility"))/100,
            "versatility": int(request.form.get("versatility"))/100
        }
        if sum(weights.values()) != 1:
            errors.append("Weights must add up to 100%.")

        if errors:
            return render_template("index.html", agents=agents, errors=errors)

        loadout = generate(items, agent, credits, weights)

        return render_template("result.html", loadout=loadout, agent=agent, credits=credits)
    
    else:
        return render_template("index.html", agents=agents)

if __name__ == "__main__":
    app.run(debug=False)