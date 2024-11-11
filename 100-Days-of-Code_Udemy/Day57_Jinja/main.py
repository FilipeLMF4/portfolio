from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
posts = Post()


@app.route('/')
def home():
    return render_template("index.html", posts=posts.all_posts)


@app.route('/post/<blog_id>')
def blog_post(blog_id):
    for p in posts.all_posts:
        if str(p["id"]) == blog_id:
            title = p["title"]
            subtitle = p["subtitle"]
            body = p["body"]
            return render_template("post.html", post_title=title, post_subtitle=subtitle, post_body=body)
    return '<h1>Sorry, that blog post does not exist!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
