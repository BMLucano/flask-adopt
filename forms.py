"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import (StringField, DecimalField, TextAreaField, BooleanField,
                    SelectField)   # ^^^^^ Get rid of unused imports!

from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    """ Form for adding pets. """

    name = StringField("Pet name", validators=[InputRequired()])
    species =  SelectField("Pet name",
                           choices=[
                                ('cat', 'Cat'),
                                ('dog', 'Dog'),
                                ('porcupine', 'Porcupine')])
                                # ^^^ Needs a validator for max length!
    photo_url = TextAreaField("Photo URL", validators=[Optional()])
    # (Could be string or textarea) ^^^ , also, wtforms url validator here.
    age = SelectField("Pet age",
                      choices=[
                          ('baby', 'Baby'),
                          ('young', 'Young'),
                          ('adult', 'Adult'),
                          ('senior', 'Senior')])
    notes = TextAreaField("Notes", validators=[Optional()])  # Optional default

class EditPetForm(FlaskForm):
    """ Form for editing info about a pet that exists already. """

    photo_url = TextAreaField("Photo URL", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Avaialble?")

    # Fix the indentation in this file as well TODO:
    # If you have to press tab repeatedly, something is wrong with spacing.