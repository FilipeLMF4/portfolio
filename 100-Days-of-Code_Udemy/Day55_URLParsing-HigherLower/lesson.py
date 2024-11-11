from flask import Flask


def make_bold(func):
    def wrapper_func_b():
        return f"<b>{func()}</b>"
    return wrapper_func_b


def make_emphasis(func):
    def wrapper_func_em():
        return f"<em>{func()}</em>"
    return wrapper_func_em


def make_underlined(func):
    def wrapper_func_u():
        return f"<u>{func()}</u>"
    return wrapper_func_u


app = Flask(__name__)


@app.route('/')
def hello_world():
    # Rendering HTML Elements
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXBvemNjeTV3ZmN0OTh4azVoam81OGRsaDRmZ3pqYzZrbHJpbDk1cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Od0QRnzwRBYmDU3eEO/giphy-downsized.gif" width=200>')


# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)


# ------------------------------------
# Advanced Python Decorator Functions


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)
