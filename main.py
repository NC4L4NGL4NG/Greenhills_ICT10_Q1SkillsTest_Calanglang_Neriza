from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Menu data
MENU = {
    "Guitar": 350,
    "Violin": 500,
    "Saxophone": 700,
    "Banjo": 300,
    "Melodica": 250
}

@app.route('/')
def index():
    return render_template('index.html', menu=MENU)

@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')
    contact = data.get('contact')
    selected_items = data.get('items', [])

    total = sum(MENU[item] for item in selected_items)

    return jsonify({
        'name': name,
        'address': address,
        'contact': contact,
        'selected_items': selected_items,
        'total': f"{total:.2f}"
    })

if __name__ == '__main__':
    app.run(debug=True)
