class Hero:
    def __init__(self, name, gender_id, age, feat, feat_id):
        self.name = name
        self.gender_id = gender_id
        self.age = age
        self.feat = feat
        self.feat_id = feat_id

    def __repr__(self):
        return self.name

    def attributes(self):
        self.strength = 5
        self.perception = 5
        self.endurance = 5
        self.charisma = 5
        self.intelligence = 5
        self.dextery = 5
        self.luck = 5

    def battle_skills(self, health, kick_damage, punch_damage, laser_damage):
        self.health = health
        self.kick_damage = (kick_damage, 'kick')
        self.punch_damage = (punch_damage, 'punch')
        self.laser_damage = (laser_damage, 'laser')
        self.attacks = (self.kick_damage, self.punch_damage, self.laser_damage)


class Enemy:
    def __init__(self, name, health, kick_damage, punch_damage, bottle_damage):
        self.name = name
        self.health = health
        self.kick_damage = (kick_damage, 'kick')
        self.punch_damage = (punch_damage, 'punch')
        self.bottle_damage = (bottle_damage, 'bottle')
        self.attacks = (self.kick_damage, self.punch_damage, self.bottle_damage)

    def __repr__(self):
        return self.name