from flask import Flask, render_template
from user.user_routes import user_bp
from store.store_routes import store_bp
from item.item_routes import item_bp
from order.order_routes import order_bp
from orderitem.orderitem_routes import orderitem_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(store_bp, url_prefix="/store")
app.register_blueprint(item_bp, url_prefix="/item")
app.register_blueprint(order_bp, url_prefix="/order")
app.register_blueprint(orderitem_bp, url_prefix="/orderitem")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def start():
    return render_template('admin/add.html')

if __name__ == "__main__":
    app.run(debug=True)