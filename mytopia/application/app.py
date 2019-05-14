# from flask import Flask, Blueprint
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from mytopia.manage import app
#
#
#
# app.config['SECRET_KEY'] = 'Fianna'
# # mysql://user:password@host:port/dbname
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
#

from flask import Flask, Blueprint
from mytopia.application.blog.views import blog
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from mytopia.application.extensions import db, migrate


app = Flask(__name__)


app.config['SECRET_KEY'] = 'zzw'
# mysql://user:password@host:port/dbname
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
# migrate = Migrate(app, db)
migrate.init_app(app, db)

app.register_blueprint(blog)


@app.route("/")
def index():
    return '<h1>Hello World</h1>'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8787, debug=True)
