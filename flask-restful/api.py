from flask import Flask
from flask_restful import Resource, Api
from flask.ext.mysql import MySQL
from peewee import *

# mysql = MySQL()
app = Flask(__name__)
app.config.from_pyfile('database.cfg')
# mysql.init_app(app)
database = MySQLDatabase('another', user='root', password='rootpass',
                         host='127.0.0.1', port=3306)


class BaseModel(Model):
    class Meta:
        database = database


class Layer(BaseModel):
    class Meta:
        table_name = 'user'
    name = CharField()

    def foo(self):
        return (Layer.select())


api = Api(app)


class HelloWorld(Resource):
    def get(self):
        # connection = mysql.connect()
        # cursor = connection.cursor()
        # cursor.execute('''SELECT id, name FROM layer''')
        # ret = cursor.fetchall()
        # ret = Layer.get(Layer.id == 1).foo()
        ret = Layer.select()
        layers = []
        for entry in ret:
            print(dir(entry))
            layers.append({entry.id: entry.name})
        return layers


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
