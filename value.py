def calculate(item, weights):
    return (
        item.offensive * weights["offensive"] + item.defensive * weights["defensive"] 
        + item.utility * weights["utility"]+ item.versatility * weights["versatility"]
    )
