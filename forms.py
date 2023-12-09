"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import (StringField, DecimalField, TextAreaField, BooleanField,
                    SelectField)

from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """ Form for adding pets. """

    name = StringField("Pet name", validators=[InputRequired()])
    species =  SelectField("Pet name",
                           choices=[
                                ('cat', 'Cat'),
                                ('dog', 'Dog'),
                                ('porcupine', 'Porcupine')])
    photo_url = TextAreaField("Photo URL", validators=[Optional(), URL()])
    age = SelectField("Pet age",
                      choices=[
                          ('baby', 'Baby'),
                          ('young', 'Young'),
                          ('adult', 'Adult'),
                          ('senior', 'Senior')])
    notes = TextAreaField("Notes", validators=[Optional()])