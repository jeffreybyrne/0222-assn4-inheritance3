class System:
    """A class to represent a solar system, a collection of celestial bodies
    """
    list_of_systems = []

    # Initialize a new instance with an empty list of bodies
    def __init__(self):
        self.bodies = []
        System.list_of_systems.append(self)

    # Instance method to add a body to the system's list of bodies
    def add(self, new_body):
        if new_body not in self.bodies:
            # Add the body if it's not already in the list
            self.bodies.append(new_body)
        else:
            return "The body {} is already in the list.".format(new_body.name)

    # Instance method to iterate through each body in the system and sum their
    # masses
    def total_mass(self):
        curr_mass = 0
        for num, body in enumerate(self.bodies, 1):
            # print(body)
            curr_mass += body.mass
        return curr_mass

    @classmethod
    def total_galactic_mass(cls):
        temp_sum = 0
        for num in range(0, len(cls.list_of_systems)):
            temp_sum += cls.list_of_systems[num].total_mass()
        return temp_sum


class Body:
    """A class to represent a generic celestial body. It has a name and a mass.
    """

    # Initialize a new instance with a name and a mass
    def __init__(self, new_name, new_mass):
        self.name = new_name
        self.mass = new_mass

    # Instead of adding a class method to each child class, this works for all
    # of them, since they inherit the method from the parent, but when calling
    # it on a specific Planet, Star, or Moon the class of that object will be
    # be used for comparison.
    @classmethod
    def all(cls, system):
        # Define an empty list to start with
        curr_list_bodies = []
        # For each item in the list of bodies of the system
        for num in range(0, len(system.bodies)):
            # If the type of the body in the list at the current position
            # matches the class that it's being called on, add it to the list
            if isinstance(system.bodies[num], cls):
                curr_list_bodies.append(system.bodies[num])
        # Return the list of bodies
        return curr_list_bodies


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
earth2 = Planet('earth', 5972000000000000000000000, 24, 365)
sun = Star('the sun', 1989000000000000000000000000000, 'g-type')
moon = Moon('the moon', 73476730900000000000000, 27, earth)
moon2 = Moon('the moon', 73476730900000000000000, 27, earth)
our_solar_system = System()
our_solar_system.add(earth)
our_solar_system.add(earth2)
our_solar_system.add(sun)
our_solar_system.add(moon)
print(our_solar_system)
print(our_solar_system.add(moon))
print(our_solar_system.total_mass())
print(earth.all(our_solar_system))
print(moon.all(our_solar_system))

al_star = Star('proxima centauri', 244600000000000000000000000000, 'm5')
al_planet = Planet('alpha centauri a', 2188000000000000000000000000000, 8, 500)
al_moon = Moon('alpha moon', 2357698090000000000000, 13, al_planet)
alpha_centauri = System()
alpha_centauri.add(al_star)
alpha_centauri.add(al_planet)
alpha_centauri.add(al_moon)
print(System.total_galactic_mass())
