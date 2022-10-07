from usuario_app import app
from usuario_app.controllers import usuarios


if __name__=="__main__":
    app.run(debug=True)
    app.secret_key = "secreto"