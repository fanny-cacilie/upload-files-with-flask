from flask import request
from flask_restful import Resource, reqparse
from models.file import FileModel
from sql_achemy import database


class Files(Resource):
    def get(self):
        return {
            "files": [
                {"id": file.id, "name": file.name} for file in FileModel.query.all()
            ]
        }

    def post(self):
        file = request.files["inputFile"]
        new_file = FileModel(name=file.filename, data=file.read())
        try:
            new_file.save_file()
        except:
            return (
                {"message": "An internal error ocurred while trying to save file."},
                500,
            )

        return "Saved " + file.filename + " to the database."


class File(Resource):
    def get(self, id):
        file = FileModel.find_file(id)
        if file:
            return (
                {"id": file.id, "name": file.name, "created_at": file.created_at},
                200,
            )
        return {"message": "File not found."}, 404

    def delete(self, id):
        file = FileModel.find_file(id)
        if file:
            try:
                file.delete_file()
            except:
                return {"message": "An error ocurred while trying to delete file."}
            return {"message": "File deleted."}, 200
        return {"message": "File not found"}, 404
