from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CreateTODOForm(FlaskForm):
    description = TextAreaField("TODO Description", validators=[DataRequired()])
    submit = SubmitField("Submit")
