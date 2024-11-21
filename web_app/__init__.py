from flask import Flask
from web_app.routes.home_routes import home_routes

app = Flask(__name__)
app.register_blueprint(home_routes)

if __name__ == "__main__":
    app.run(debug=True)

