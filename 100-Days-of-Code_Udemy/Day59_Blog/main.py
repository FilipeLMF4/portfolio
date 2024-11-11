from flask import Flask, render_template
import requests

app = Flask(__name__)
all_posts = requests.get('https://api.npoint.io/1f50c799c33727a6cab2').json()


@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<post_id>')
def post(post_id):
    post_content = ""
    for p in all_posts:
        if str(p['id']) == post_id:
            post_content = p

    return render_template('post.html', post=post_content)


if __name__ == "__main__":
    app.run(debug=True)
