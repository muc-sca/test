from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import random
from recources.order import Order, OrderPost
from recources.orders import Orders
from recources.products import Products
from recources.product import Product, ProductPost, ProductPut, ProductDelete
from security import authenticate, identity
import datetime
app = Flask(__name__)
app.secret_key = 'salman'
api = Api(app)
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=63072000)
jwt = JWT(app, authenticate, identity)

api.add_resource(Order, '/order/<int:_id>')
api.add_resource(OrderPost, '/order')
api.add_resource(Orders, '/orders/<int:_id>')
api.add_resource(Products, '/products/<int:_id>')
api.add_resource(ProductPost, '/product')
api.add_resource(Product, '/product/<int:_id>')
api.add_resource(ProductPut, '/product/<int:_id>')
api.add_resource(ProductDelete, '/product/<int:_id>')

app.run(port=5000, debug=True)