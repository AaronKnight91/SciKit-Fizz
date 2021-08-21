import numpy as np

class ConstantAcceleration():

    def __init__(self, displacement=0, initial_velocity=0, final_velocity=0, acceleration=0, time=0, num_intervals=10):

        if time < 0:
            raise ValueError("Time must be greater than or equal to 0 seconds")
        self._s = np.linspace(0, displacement, num_intervals)
        self._u = initial_velocity
        self._v = [final_velocity]
        self._a = acceleration
        self._t = np.linspace(0, time, num_intervals)

        self.final_velocity = self._v[-1]

    # v = u + at
    # x = (u + v)t/2
    # x = ut + 0.5at**2
    # v**2 = u**2 + 2ax
    # x = vt - 0.5at**2

    def calculate_velocity(self):

        self._v = self._u + (self._a * self._t)
        self.final_velocity = self._v[-1]
        return self.final_velocity

    def calculate_displacement(self):

        self._s = ((self._u + self._v) * self._t) / 2


if  __name__ == "__main__":

    c = ConstantAcceleration(initial_velocity = 10, acceleration = 5, time = 12.3)
    vel = c.calculate_velocity()
    print(vel)
    
