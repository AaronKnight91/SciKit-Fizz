
class Newtonian():

    def __init__(self, mass=0, acceleration=0):

        self._mass = mass
        self._acceleration = acceleration

    def calculate_force(self):

        self._force = self._mass * self._acceleration
