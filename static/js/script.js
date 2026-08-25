const sliders = {
    offensive: document.getElementById("offensive"),
    defensive: document.getElementById("defensive"),
    utility: document.getElementById("utility"),
    versatility: document.getElementById("versatility")
};

const values = {
    offensive: document.getElementById("offensive-value"),
    defensive: document.getElementById("defensive-value"),
    utility: document.getElementById("utility-value"),
    versatility: document.getElementById("versatility-value")
};

const totalDisplay = document.getElementById("weight-total");

function updateWeights() {
    let total = 0;
    for (const name in sliders) {
        const value = Number(sliders[name].value);
        values[name].textContent = `${value}%`;
        total += value;
    }
    totalDisplay.textContent = `${total}%`;
}

for (const name in sliders) {
    sliders[name].addEventListener("input", updateWeights);
}

updateWeights();