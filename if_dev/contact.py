from flask_wtf import FlaskForm
from wtforms import (StringField, EmailField, TelField, SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Email, Regexp

class ContactForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Regexp(r"[a-zA-z]+")])
    email = EmailField("Correo", validators=[DataRequired(), Email()], render_kw={"required": ""})
    phone = TelField("Telefono", validators=[DataRequired()])
    message = TextAreaField("Mensaje", validators=[DataRequired()], render_kw={"style": "height: 10rem"})
    submit = SubmitField("Enviar", render_kw={"class": "btn btn-primary btn-lg"})