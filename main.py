from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from decouple import config
from flask_sqlalchemy import SQLAlchemy

from db import db

from resources.routes import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@localhost:{config("DB_PORT")}/{config("DB_NAME")}'

db.init_app(app)
app.config.from_object("config.DevelopmentConfig")

api = Api(app)
migrate = Migrate(app, db)


[api.add_resource(*route_data) for route_data in routes]


if __name__ == "__main__":
    app.run()

