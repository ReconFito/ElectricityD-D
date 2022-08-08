
from flask_wtf import FlaskForm
from wtforms import (EmailField, 
                    PasswordField,
                    SubmitField)
from wtforms.validators import DataRequired, Email

class LoginEmpleado(FlaskForm):
    email = EmailField("Correo", 
                        validators=[DataRequired("* Este campo es obligatorio"),
                                    Email("* Introduce un correo valido")], 
                        render_kw={"placeholder": "name@example"})

    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Ingresar")