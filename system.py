class System:

    def __init__(self):
        self.bodies = []

    def add(self, new_body):
        self.bodies.append(new_body)

    def total_mass(self):
        curr_mass = 0
        for num, body in enumerate(self.bodies, 1):
            print(body)
            curr_mass += body.mass
        return curr_mass


class Body:

    def __init__(self, new_name, new_mass):
        self.name = new_name
        self.mass = new_mass


class Planet(Body):

    def __init__(self, new_name, new_mass, new_day, new_year):
        super().__init__(new_name, new_mass)
        self.day = new_day
        self.year = new_year


class Star(Body):

    def __init__(self, new_name, new_mass, new_type):
        super().__init__(new_name, new_mass)
        self.type = new_type


class Moon(Body):
    pass


thing1 = Body('thing1', 4)
sys1 = System()
sys1.add(thing1)
print(sys1.total_mass())
