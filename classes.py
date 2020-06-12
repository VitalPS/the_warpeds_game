class Hero:
    def __init__(self, name, gender_id, age, feat_id):
        self.name = name
        self.gender_id = gender_id
        self.age = age
        self.feat_id = feat_id

    def attributes(self):
        self.strength = 5
        self.perception = 5
        self.endurance = 5
        self.charisma = 5
        self.intelligence = 5
        self.agility = 5
        self.luck = 5


x1 = Hero
