from flask import Flask
from flask_restful import Resource, Api
from peewee import *

app = Flask(__name__)
app.config.from_pyfile('database.cfg')
database = MySQLDatabase('abtest', user='root', password='rootpass',
                         host='127.0.0.1', port=3306)


class BaseModel(Model):
    class Meta:
        database = database


class Layer(BaseModel):
    class Meta:
        table_name = 'layer'
    name = CharField()
    status = SmallIntegerField()
    product_id = IntegerField()
    params = TextField()
    create_time = DateTimeField()
    update_time = DateTimeField()

    def foo(self):
        return (Layer.select())


api = Api(app)


class HelloWorld(Resource):
    def get(self):
        ret = Layer.select()
        layers = []
        for entry in ret:
            layers.append(
                {
                    "id": entry.id,
                    "name": entry.name,
                    "status": entry.status,
                    "product_id": entry.product_id,
                    "params": entry.params,
                    # "create_time": entry.create_time,
                    # "update_time": entry.update_time,
                }
            )
        return layers


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
