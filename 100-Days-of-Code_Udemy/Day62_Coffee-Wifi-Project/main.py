from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening = StringField('Opening Time eg. 9AM', validators=[DataRequired()])
    closing = StringField('Closing Time eg. 8PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating',
                                choices=[('☕️'*i, '☕️'*i) for i in range(1, 6)]
                                )
    wifi_rating = SelectField('Wifi Strength Rating',
                              choices=[('💪'*i, '💪'*i) if i != 0 else ('✘', '✘') for i in range(6)]
                              )
    power_rating = SelectField('Power Socket Availablity',
                               choices=[('🔌'*i, '🔌'*i) if i != 0 else ('✘', '✘') for i in range(6)]
                               )
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        to_add = (f"\n{form.cafe.data},"
                  f"{form.location.data},"
                  f"{form.opening.data},"
                  f"{form.closing.data},"
                  f"{form.coffee_rating.data},"
                  f"{form.wifi_rating.data},"
                  f"{form.power_rating.data}")

        with open('cafe-data.csv', mode='a', encoding='utf-8') as csv_file:
            csv_file.write(to_add)

        return redirect('add')

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
