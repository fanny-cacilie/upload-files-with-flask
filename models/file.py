from sql_achemy import database


class FileModel(database.Model):

    __tablename__ = "files"

    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(80))
    data = database.Column(database.LargeBinary)

    @classmethod
    def find_file(cls, id):
        file = cls.query.filter_by(id=id).first()
        if file:
            return file
        return None

    def save_file(self):
        database.session.add(self)
        database.session.commit()

    def delete_file(self):
        database.session.delete(self)
        database.session.commit()
