from flask import Flask
from flask_migrate import Migrate
from database import db
import logging
from config import BasicConfig
#Routes
from routes.docentes.docentes import appdocente
from routes.papitas.papitas import apppapitas
from routes.errores.errores import apperror
from routes.aguas.aguas import appaguas
from routes.subways.subways import appsubways
from routes.pizzas.pizzas import apppizzas



app = Flask(__name__)
app.register_blueprint(appdocente)
app.register_blueprint(apppapitas)
app.register_blueprint(appaguas)
app.register_blueprint(appsubways)
app.register_blueprint(apppizzas)
app.register_blueprint(apperror)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="debug.log")