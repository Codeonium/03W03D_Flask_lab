from flask import render_template

from app import app
from app.models.order import order
from app.models.order_list import orders


@app.route('/order')
def index():
    return render_template(
        'base.html', 
        title = "Dildos 'r' us", 
        orders = orders
    )

@app.route('/order/find-by-index/<index>')
def find_by_index(index):
    for order in orders:
        if order[0] == index:
            return f"{str(order.customer_name)} ordered {str(order.quantity)} of{str(order.item_name)} for personal reasons, on {str(order.order_date)}"

    return "User not found (try 1 or 2)"

    return render_template(
        'order.html',
        title = "Dildos 'r' us",
        orders = orders
    )

@app.route('/order/find-by-name/<name>')
def find_by_name(name):
    for order in orders:
        if order.customer_name == name:
            return f"{str(order.customer_name)} ordered {str(order.quantity)} of {str(order.item_name)} for personal reasons, on {str(order.order_date)}"

    return "Keyboard not found (press any key to continue)"

    return render_template(
        'order.html',
        title = "Dildos 'r' us",
        orders = orders
    )
