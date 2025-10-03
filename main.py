from pyscript import display, document

menu_prices = {
    "carbonara": 150,
    "garlic": 80,
    "salad": 120,
    "tea": 60,
    "water": 40
}

def create_order(event=None):
    name = document.getElementById("custName").value
    addr = document.getElementById("custAddr").value
    num = document.getElementById("custNum").value

    total = 0
    items = []

    for key, price in menu_prices.items():
        checkbox = document.getElementById(key)
        if checkbox.checked:
            items.append(checkbox.value)
            total += price

    message = f"""
    <p><b>Order for:</b> {name}<br>
    <b>Address:</b> {addr}<br>
    <b>Contact number:</b> {num}<br>
    <b>Total:</b> ₱ {total:.2f}</p>
    """

    display(message, target="output")
