from flask_wtf import FlaskForm

# Form field imports
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    IntegerField,
    DecimalField,
    SubmitField
)

# Validator imports
from wtforms.validators import DataRequired


class PropertyForm(FlaskForm):
    property_title = StringField('Property Title', validators=[DataRequired()])

    description = TextAreaField(
        'Description', validators=[DataRequired()],
        render_kw={"rows": 8, "cols": 50})

    no_rooms = IntegerField('No. of Rooms', validators=[DataRequired()])

    no_bathrooms = IntegerField(
        'No. of Bathrooms', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])

    property_type = SelectField('Property Type',
                                choices=[
                                    ('house', 'House'),
                                    ('apartment', 'Apartment')
                                ])

    location = StringField(validators=[DataRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'JPG and PNG Images only!')
    ])

    submit = SubmitField("Add Property")
