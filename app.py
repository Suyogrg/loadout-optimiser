from flask import Flask, render_template, request
from item_loader import load_items
from loadout_service import get_agents, generate

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    items = load_items()
    agents = get_agents(items)

    if request.method == "POST":
        credits = int(request.form["credits"])
        agent = request.form["agent"]
        weights = {"offensive": 0.25, "defensive": 0.25, "utility": 0.25, "versatility": 0.25}
        loadout = generate(items, agent, credits, weights)
        
        return render_template("result.html", loadout=loadout, agent=agent, credits=credits)
    
    else:
        return render_template("index.html", agents=agents)

if __name__ == "__main__":
    app.run(debug=False)