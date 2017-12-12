from db import db


class ItemModel(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String())
    category = db.Column(db.String())
    is_featured = db.Column(db.Boolean())
    price = db.Column(db.Float(precision=2))
    image_URL = db.Column(db.String())

    def __init__(self, name, description, category, is_featured, price, image_URL):
        self.name = name
        self.description = description
        self.category = category
        self.is_featured = is_featured
        self.price = price
        self.image_URL = image_URL

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # SELECT * FROM items WHERE name=name LIMIT 1
        return ItemModel.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
