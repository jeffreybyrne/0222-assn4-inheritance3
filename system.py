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

    def __init__(self, new_name, new_mass, new_month, new_planet):
        super().__init__(new_name, new_mass)
        self.month = new_month
        self.planet = new_planet


earth = Planet('earth', 5972000000000000000000000, 24, 365)
sun = Star('the sun', 1989000000000000000000000000000, 'g-type')
moon = Moon('the moon', 73476730900000000000000, 27, earth)
our_solar_system = System()
our_solar_system.add(earth)
our_solar_system.add(sun)
our_solar_system.add(moon)
print(our_solar_system.total_mass())
