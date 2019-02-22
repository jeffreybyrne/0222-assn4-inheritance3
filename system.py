class System:

    bodies = []

    def add(self):
        pass

    def total_mass(self):
        pass


class Body:

    def __init__(self, new_name, new_mass):
        self.name = new_name
        self.mass = new_mass


class Planet(Body):

    def __init__(self, new_name, new_mass, new_day, new_year):
        self.name = new_name
        self.mass = new_mass
        self.day = new_day
        self.year = new_year


class Star(Body):
    pass


class Moon(Body):
    pass
