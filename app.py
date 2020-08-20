from flask import Flask, render_template, request
from flask_restful import Api
from resources.file import Files, File

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)


@app.before_first_request
def create_db():
    database.create_all()


@app.route("/")
def index():
    return render_template("index.html")


api.add_resource(Files, "/files")
api.add_resource(File, "/files/<string:id>")


if __name__ == "__main__":
    from sql_achemy import database

    database.init_app(app)

    app.run(debug=True)

