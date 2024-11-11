from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/1f50c799c33727a6cab2").json()
APP_PASS = "pass"
my_email = "email"

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    title = "Contact Me"
    if request.method == 'POST':
        data = request.form
        message_to_send = (f"Name: {data['name']}\n"
                           f"Email: {data['email']}\n"
                           f"Phone: {data['phone']}\n"
                           f"Message: {data['message']}")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=APP_PASS)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:New Message\n\n{message_to_send}"
            )

        title = "Successfully sent your message"

    return render_template("contact.html", title=title)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
