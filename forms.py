from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Usuarios(FlaskForm):
    Id = StringField('Id', validators=[DataRequired()])
    Nombres = StringField('Nombres', validators=[DataRequired()])
    Apellidos = StringField('Apellidos', validators=[DataRequired()])
    Celular = StringField('Celular', validators=[DataRequired()])
    Correo = StringField('Correo', validators=[DataRequired()])
    Username = StringField('Username', validators=[DataRequired()])
    Password = StringField('Password', validators=[DataRequired()])
    iniciar = SubmitField('Iniciar Sesión')
    enviar = SubmitField('Registrarse')