from flask_app.config.mysqlconnection import connectToMySQL
db = 'recipes_br'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.thirty_min = data['thirty_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(db).query_db(query)
        recipes = []
        for recipe in recipes:
            recipe.append(cls(recipe))
        return recipes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, thirty_min, user_id) VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(thirty_min)s, %(user_id)s );"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(recipe_id)s;"
        return connectToMySQL(db).query_db(cls, data)

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, thirty_min = %(thirty_min)s WHERE id = %(recipe_id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
