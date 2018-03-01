from flask import Flask
from flask_restful import Resource, Api
from flask.ext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config.from_pyfile('database.cfg')
mysql.init_app(app)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        connection = mysql.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM layer''')
        ret = cursor.fetchall()
        layers = []
        for entry in ret:
            record = {
                'id': entry[0],
                'name': entry[1],
            }
            layers.append(record)
        return layers


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
