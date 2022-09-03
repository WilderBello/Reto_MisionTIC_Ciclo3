from contextlib import redirect_stderr
from flask import request, Flask,flash, render_template, jsonify, url_for,session,make_response,g,redirect
import database as bd
# from forms import Producto
from forms import Usuarios
from settings.config import configuracion
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

app = Flask(__name__)
app.config.from_object(configuracion)

@app.route('/main')
def main():
    return render_template('main.html',titulo="Marriot - Wuxi Moaye City ")

@app.route('/initial')
@app.route('/')
def inicio():
    return render_template('initial.html',titulo="Marriot - Wuxi Moaye City ")

@app.route('/details')
def detalleHabitacion():
    return render_template('details.html',titulo="Habitación x")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = Usuarios()
        return render_template('login.html',form=form,titulo="Ingresar") 
    elif request.method == 'POST':
        Username = request.form["Username"]
        Password = request.form["Password"]
        dataUser = bd.sql_login(Username,Password)
        if dataUser != False:
            session['user'] = dataUser[0]
            session['username'] = dataUser[7]
            session['rol'] = dataUser[6]
            flash('Usuario logueado correctamente')
            return redirect(url_for('inicio'))
        else:
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('login')) 
            
@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('username', None)
    session.pop('rol', None)
    return redirect(url_for('inicio'))
    
@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method =='GET':
        form = Usuarios()
        return render_template('signup.html',form=form,titulo="Registrate")
    elif request.method == 'POST':
        Id = request.form["Id"]
        Nombres = request.form["Nombres"]
        Apellidos = request.form["Apellidos"]
        Celular = request.form["Celular"]
        Correo = request.form["Correo"]
        Username = request.form["Username"]
        Password = request.form["Password"]
        pw_hash = bcrypt.generate_password_hash(Password).decode('utf-8')
        bd.sql_signup(Id,Nombres,Apellidos,Correo,Celular,Username,pw_hash)
        flash(f'Usuario {Nombres} registrado con exito!')
        return render_template('initial.html',titulo="Registro de nuevo usuario")

@app.route('/admin-details',methods=['GET'])
def admindetails():
    if session['rol'] == 'admin':
        return render_template('details_admin.html',titulo="Habitación y")
    else:
        flash('Usted no tiene permisos para acceder a esta página')
        return redirect(url_for('inicio'))

@app.route('/superadmin-details',methods=['GET'])
def superadmindetails():
    if session['rol'] == 'superadmin':
        return render_template('details_superadmin.html',titulo="Habitación z")
    else:
        flash('Usted no tiene permisos para acceder a esta página')
        return redirect(url_for('inicio'))

@app.route('/profile')
def profile():
    form=Usuarios()
    return render_template('edit-profile.html',form=form, titulo="Editar perfil")

if __name__ == '__main__':
    app.run(debug=True)
    