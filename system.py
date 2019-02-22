class System:
    """A class to represent a solar system, a collection of celestial bodies
    """

    # Initialize a new instance with an empty list of bodies
    def __init__(self):
        self.bodies = []

    # Instance method to add a body to the system's list of bodies
    def add(self, new_body):
        self.bodies.append(new_body)

    # Instance method to iterate through each body in the system and sum their
    # masses
    def total_mass(self):
        curr_mass = 0
        for num, body in enumerate(self.bodies, 1):
            print(body)
            curr_mass += body.mass
        return curr_mass


class Body:
    """A class to represent a generic celestial body. It has a name and a mass.
    """

    # Initialize a new instance with a name and a mass
    def __init__(self, new_name, new_mass):
        self.name = new_name
        self.mass = new_mass


class Planet(Body):
    """A class to represent a planet, a specific type of celestial body. In
    addition to a name and a mass, they also have the length of their day and
    the length of their year.
    """

    # Initialize a new planet as a body with a name, mass, day length, and year
    # length
    def __init__(self, new_name, new_mass, new_day, new_year):
        super().__init__(new_name, new_mass)
        self.day = new_day
        self.year = new_year


class Star(Body):
    """A class to represent a star, a specific type of celestial body. In
    addition to a name and a mass, they also have a classification type.
    """

    # Initialize a new star as a body with a name, mass, and type
    def __init__(self, new_name, new_mass, new_type):
        super().__init__(new_name, new_mass)
        self.type = new_type


class Moon(Body):
    """A class to represent a moon, a specific type of celestial body. In
    addition to a name and a mass, they also have the duration it takes them to
    orbit their planet, as well as the planet they orbit.
    """

    # Initialize a new moon as a body with a name, mass, month length, and
    # the planet it orbits
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
