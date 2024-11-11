from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def mainpage():
    random_number = random.randint(1, 10)
    return render_template("index.html", rnum=random_number, this_year=datetime.now().year)


@app.route('/guess/<name>/')
def guess(name):
    agify_api = requests.get(f"https://api.agify.io?name={name}")
    age = agify_api.json()["age"]
    genderize_api = requests.get(f"https://api.genderize.io/?name={name}")
    gender = genderize_api.json()["gender"]
    return render_template("guess_page.html", name=name.title(), age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
