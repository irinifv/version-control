# this is the "web_app/routes/home_routes.py" file.

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/") 
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")
@home_routes.route("/about")
def about():
    print("ABOUT...")
    #return "About Me"
    return render_template("about.html")
@home_routes.route("/hello")
def hello_world():
    print("HELLO...")
    # if the request contains url params,
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    # access "name" key if present, otherwise use default value
    name = url_params.get("name") or "World"
    message = f"Hello, {name}!"
    #return message
    return render_template("hello.html", message=message, x=5)
@home_routes.route("/test")
def test():
    return "Test route works!"