from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
db = 'cookie_orders'

class Cookie_order:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_orders;"
        results = connectToMySQL(db).query_db(query)
        cookie_orders = []
        for order in results:
            cookie_orders.append(cls(order))
        return cookie_orders

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cookie_orders (name, cookie_type, number_of_boxes) VALUES ( %(name)s, %(cookie_type)s, %(number_of_boxes)s );"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one_order(cls, data):
        query = "SELECT * FROM cookie_orders WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def update_order(cls, data):
        query = "UPDATE cookie_orders SET name = %(name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_order(cookie_order):
        is_valid = True
        if len(cookie_order['name']) <= 0 or len(cookie_order['cookie_type']) <= 0 or len(cookie_order['number_of_boxes']) <= 0:
            flash("All fields required")
            is_valid = False
            return is_valid
        if len(cookie_order['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(cookie_order['cookie_type']) < 2:
            flash("Cookie type must be at least 2 characters")
            is_valid = False
        if int(cookie_order['number_of_boxes']) <= 0:
            flash("You must buy at least 1 box of cookies")
            is_valid = False
        return is_valid