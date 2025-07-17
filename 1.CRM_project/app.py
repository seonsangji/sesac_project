from flask import Flask, render_template
from user.user_routes import user_bp
from store.store_routes import store_bp


app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(store_bp, url_prefix="/store")


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)