# importar la función que devolverá una instancia de una conexión
from usuario_app.config.mysqlconnection import connectToMySQL


class Usuarios:
    db_name="usuarios"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
    
    def full_name(self):
        return f"{self.nombre} {self.apellido}"
# ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls): #*!obtener toda la informacion de la base de datos
        query = "SELECT * FROM usuario;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(cls.db_name).query_db(query)
        # crear una lista vacía
        usuarios = []
        print(usuarios)
        # Iterar sobre los resultados de la base de datos
        for x in results:
            usuarios.append(cls(x))
        #retornamos una lista de objetos
        return usuarios
    
    #*METODOS DE CREACION (CREATE)
    @classmethod
    def save(cls, data): #*!guardar informacion en la base de datos
        query = "INSERT INTO usuario (nombre, apellido, email) VALUES ( %(fname)s, %(lname)s, %(email)s );"
        #*!data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL(cls.db_name).query_db( query, data )
    
    @classmethod
    def get_one(cls,data): #*!metodo para obtener un usuario mediante su id
        query  = "SELECT * FROM usuario WHERE id = %(id)s";
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])

    @classmethod
    def actualizar(cls,data): #*!metodo para actualizar informacion de la bd
        query = "UPDATE usuario SET nombre=%(fname)s, apellido=%(lname)s, email=%(email)s, update_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def eliminar(cls,data): #*!metodo para eliminar informacion de la bd
        query  = "DELETE FROM usuario WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)