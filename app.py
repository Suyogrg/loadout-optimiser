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

        if errors:
            return render_template("index.html", agents=agents, errors=errors)

        weights = {"offensive": 0.25, "defensive": 0.25, "utility": 0.25, "versatility": 0.25}
        loadout = generate(items, agent, credits, weights)

        return render_template("result.html", loadout=loadout, agent=agent, credits=credits)
    
    else:
        return render_template("index.html", agents=agents)

if __name__ == "__main__":
    app.run(debug=False)