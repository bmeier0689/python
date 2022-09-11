from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model
db = 'recipes_br'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.thirty_min = data['thirty_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes LEFT JOIN users on recipes.user_id = users.id;"
        results = connectToMySQL(db).query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            recipe.user = user_model.User(user_data)
            recipes.append(recipe)
        return recipes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date, thirty_min, user_id) VALUES ( %(name)s, %(description)s, %(instructions)s, %(date)s, %(thirty_min)s, %(user_id)s );"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, thirty_min = %(thirty_min)s WHERE id = %(recipe_id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, recipe)
        if len(recipe['name']) <= 3:
            flash("Name must be longer", "recipe")
            is_valid = False
        if len(recipe['description']) <= 3:
            flash("Please provide a description!", "recipe")
            is_valid = False
        if len(recipe['instructions']) <= 3:
            flash("Must provide some instructions!", "recipe")
            is_valid = False
        return is_valid
