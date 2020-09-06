from flask import Blueprint, jsonify, request
from . import db
from .models import Product, User, Order

main = Blueprint('main', __name__)


@main.route('/User/')
def Users():
    consultar = User.query.all()

    us = []

    for u in consultar:
        us.append({'id': u.id, 'name': u.name, 'lastname': u.lastname})

    return jsonify(us), 200


@main.route('/User/', methods=['POST'])
def Add_User():
    user_data = request.get_json()

    new_user = User(name=user_data['name'], lastname=user_data['lastname'])

    db.session.add(new_user)
    db.session.commit()

    return 'Done, User Added!', 201


@main.route('/User/<cod>/', methods=['PUT', 'PATCH'])
def Update_User(cod):
    query = User.query.filter(User.id == cod)
    query.update(request.json)
    db.session.commit()

    return 'Done', 201


@main.route('/User/<cod>/', methods=['DELETE'])
def Del_User(cod):
    User.query.filter(User.id == cod).delete()
    db.session.commit()

    return 'Done', 201


################################ PRODUTOS ################################


@main.route('/Product/')
def Products():
    consultar = Product.query.all()

    pd = []

    for p in consultar:
        pd.append({'id': p.id, 'title': p.title, 'price': p.price, 'description': p.description})

    return jsonify(pd)


@main.route('/Product/', methods=['POST'])
def Add_Product():
    prod_data = request.get_json()

    new_product = Product(title=prod_data['title'], price=prod_data['price'], description=prod_data['description'])

    db.session.add(new_product)
    db.session.commit()

    return 'Done, Product Added!', 201


@main.route('/Product/<cod>/', methods=['PUT', 'PATCH'])
def Update_Product(cod):
    query = Product.query.filter(Product.id == cod)
    query.update(request.json)
    db.session.commit()

    return 'Done, Product Update!', 201


@main.route('/Product/<cod>/', methods=['DELETE'])
def Del_Product(cod):
    Product.query.filter(Product.id == cod).delete()
    db.session.commit()

    return 'Done, Product Deleted!', 201

########################## Order ################################


@main.route('/Orders/')
def Orders():
    consultar = Order.query.all()

    od = []

    for o in consultar:
        od.append({'order_id': o.id, 'ammount': o.ammount, 'data': o.data, 'value_total': o.value_total, 'user_id': o.user_id, 'product_id': o.product_id})

    return jsonify(od)


@main.route('/Orders/', methods=['POST'])
def Add_Orders():
    order_data = request.get_json()

    new_order = Order(ammount=order_data['ammount'], data=order_data['data'], value_total=order_data['value_total'], user_id=order_data['user_id'], product_id=order_data["product_id"])

    db.session.add(new_order)
    db.session.commit()

    return 'Done, Order Added!', 201




@main.route('/Orders/<cod>/', methods=['DELETE'])
def Del_Order(cod):
    Order.query.filter(Order.id == cod).delete()
    db.session.commit()

    return 'Done, Order Deleted!', 201

