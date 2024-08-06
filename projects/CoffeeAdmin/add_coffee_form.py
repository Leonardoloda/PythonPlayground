from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class AddCoffeeForm(FlaskForm):
    name = StringField('Coffee Name', validators=[DataRequired()])
    location = StringField('Coffee Location', validators=[DataRequired(), URL()])
    open_time = StringField('Coffee Opening Time', validators=[DataRequired()])
    close_time = StringField('Coffee Closing Time', validators=[DataRequired()])

    coffee = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                       validators=[DataRequired()])
    power = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                        validators=[DataRequired()])

    add = SubmitField('Add Coffee')
