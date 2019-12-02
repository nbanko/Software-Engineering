from flask import Flask

def create_app(config="OOZero.config.TestingConfig"):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_envvar('OOZERO_CONFIG')

    from OOZero.model import db
    db.init_app(app)

    return app
