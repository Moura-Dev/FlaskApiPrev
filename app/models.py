from . import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ammount = db.Column(db.Integer())
    data = db.Column(db.DateTime())
    value_total = db.Column(db.Float())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.Float())
    description = db.Column(db.String(100))
    order = db.relationship('Order', backref='product', lazy=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    order = db.relationship('Order', backref='user', lazy=True)
