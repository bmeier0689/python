from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
db = 'log_and_reg'
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?P<password>((?=\S*[A-Z])(?=\S*[a-z])(?=\S*\d)(?=\S*[\!\"\§\$\%\&\/\(\)\=\?\+\*\#\'\^\°\,\;\.\:\<\>\ä\ö\ü\Ä\Ö\Ü\ß\?\|\@\~\´\`\\])\S{8,}))+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dob = data['dob']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, dob, email, password) VALUES ( %(first_name)s, %(last_name)s, %(dob)s, %(email)s, %(password)s );"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def check_email(cls, email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, {'email': email})
        if len(results) == 0:
            return False
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) <= 0 or len(user['last_name']) <= 0 or len(user['dob']) <= 0 or len(['email']) <= 0 or len(user['password']) <= 0:
            flash("All fields required")
            is_valid = False
            return is_valid
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters")
        if not NAME_REGEX.match(user['first_name']):
            flash("Invalid First Name")
            is_valid = False
        if not NAME_REGEX.match(user['last_name']):
            flash("Invalid Last Name")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address")
            is_valid = False
        if not PASSWORD_REGEX.match(user['password']):
            flash("Please input a valid password")
            is_valid = False
        return is_valid