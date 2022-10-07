
from usuario_app.models.usuario import Usuarios
from usuario_app import app
from flask import render_template, redirect, request, session 


@app.route('/')
def raiz():
    usuarios = Usuarios.get_all()
    return render_template("index2.html", todos_usuarios=usuarios)
    #*! En lugar de devolver una cadena, 
    #*! devolveremos el resultado del método render_template
    #*!pasando el nombre de nuestro archivo HTML

@app.route('/usuario')
def formulario():
    return render_template("index.html")

@app.route('/users/new', methods=['POST'])
def enviar():
    print(request.form)
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    #*! Pasamos el diccionario de datos al método save de la clase
    id_usuario = Usuarios.save(data)
    #*!No olvides redirigir después de guardar en la base de datos
    return redirect(f'/user/{id_usuario}')

@app.route('/user/<int:id>') #*!mostrar informacion del usuario
def show_usuario(id):
    data = {
        "id":id
    }
    user = Usuarios.get_one(data)
    print(user)
    todos_usuarios = Usuarios.get_all()
    return render_template("show.html", todos_usuarios=todos_usuarios, user=user)

@app.route('/user/destroy/<int:id>')
def elimina(id):
    data = {
        "id":id
    }
    user = Usuarios.eliminar(data)
    print(user)
    todos_usuarios = Usuarios.get_all()
    return render_template("index2.html", todos_usuarios=todos_usuarios, user=user)

"""@app.route('/user/edit/<int:id>')
def editar(id):
    data = {
        "id":id
    }
    un_usuario = Usuarios.get_one(data)
    return render_template("editar.html", un_usuario=un_usuario)

@app.route('/user/edit/<int:id>', methods=['POST'])
def editar_usuario(id):
    data = {
        "id":id,
        "fname":request.form['fname'],
        "lname":request.form['lname'],
        "email": request.form['email']
    }
    user = Usuarios.actualizar(data)
    print(user)
    return redirect("/")"""

#GET Y POST EN LA MISMA RUTA EN LA MISMA FUNCION
@app.route('/user/edit/<int:id>', methods=['POST', 'GET'])
def editar_usuario(id):
    if request.method == "GET":
        data = {
        "id":id
        }
        un_usuario = Usuarios.get_one(data)
        return render_template("editar.html", un_usuario=un_usuario)
    # SI ES QUE EL METODO DE CONSULTA NO FUE GET, ENTONCES NOS QUEDA POST
    else:
        data = {
            "id":id,
            "fname":request.form['fname'],
            "lname":request.form['lname'],
            "email": request.form['email']
        }
        user = Usuarios.actualizar(data)
        print(user)
        return redirect("/")

@app.route('/clearsession')
def limpiar_session():
    session.clear()
    return redirect('/')

