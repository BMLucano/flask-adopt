"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import (StringField, DecimalField, TextAreaField, BooleanField,
                    SelectField)

from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    """ Form for adding pets. """

    name = StringField("Pet name", validators=[InputRequired()])
    species =  SelectField("Pet name",
                           choices=[
                                ('cat', 'Cat'),
                                ('dog', 'Dog'),
                                ('porcupine', 'Porcupine')])
    photo_url = TextAreaField("Photo URL", validator=[Optional()])
    age = SelectField("Pet age",
                      choices=[
                          ('baby', 'Baby'),
                          ('young', 'Young'),
                          ('adult', 'Adult'),
                          ('senior', 'Senior')])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """ Form for editing info about a pet that exists already. """

    photo_url = TextAreaField("Photo URL", validator=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Avaialble?")