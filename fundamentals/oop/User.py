class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print(f"{self.first_name} is already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print(f"{self.first_name} doesn't have enough points to spend.")
        else:
            self.gold_card_points -= amount
        return self

brad = User("Brad", "Meier", "bmeier0689@gmail.com", 33)
grace = User("Grace", "Bellamy", "graceiscool@gmail.com", 28)
reina = User("Reina", "Jimbo", "reinaisrad@gmail.com", 25)

brad.enroll().spend_points(50).display_info()
grace.enroll().spend_points(80).display_info()

brad.enroll()

reina.spend_points(40)