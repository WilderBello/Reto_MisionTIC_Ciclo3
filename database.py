import sqlite3 
from sqlite3 import Error
from flask import Flask
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)

def sql_connection():
    try:
        con=sqlite3.connect('baseDatos.db')
        return con
    except Error:
        print(Error)

def sql_insert_producto(id,nombre,precio,cantidad):
    strsql="INSERT INTO Producto (Id,Nombre,Precio,Existencia) VALUES(" + id +", '"+ nombre + "', "+precio+", "+cantidad+");"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_signup(id,nombres,apellidos,correo,celular,username,password):
    rol = 'usuario'
    dateCreate = str(datetime.now())
    print(password)
    strsql = f"INSERT INTO Usuarios (Id, Nombres, Apellidos, Celular, Correo, DateCreate, Rol, Username, Password) VALUES({id}, '{nombres}', '{apellidos}', {celular}, '{correo}', '{dateCreate}', '{rol}', '{username}', '{password}');"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_login(username,password):
    strsql = f"SELECT * FROM Usuarios WHERE Username = '{username}'"
    
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    datos = cursor_Obj.fetchall()
    if datos != []:
        if bcrypt.check_password_hash(datos[0][8], password) == True:
            print("login correcto")
            con.close()
            return datos[0]
    else:
        print("Login Failed")
        con.close()
        return False

def sql_select_productos():
    strsql="SELECT * FROM Producto;"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    productos = cursor_Obj.fetchall()
    con.close()
    return productos

def sql_edit_producto(id,cantidad):
    strsql="UPDATE Producto SET Existencia = "+cantidad+" WHERE Id = "+id+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

