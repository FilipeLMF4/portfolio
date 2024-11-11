from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


# Initialization
class Base(DeclarativeBase):
    pass


app = Flask(__name__)
db = SQLAlchemy(model_class=Base)


class Books(db.Model):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db.init_app(app)

with app.app_context():
    db.create_all()


# Flask
@app.route('/')
def home():
    result = db.session.execute(db.select(Books).order_by(Books.id))
    all_books = result.scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form.to_dict()
        new_book = Books(title=data["title"], author=data["author"], rating=data["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        new_rating = request.form.to_dict()["new_rating"]
        book_id = request.form.to_dict()["id"]
        rating_to_update = db.get_or_404(Books, book_id)
        rating_to_update.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = db.get_or_404(Books, book_id)
    return render_template('edit.html', book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=False)
