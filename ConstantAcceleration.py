import numpy as np
import math as m

class ConstantAcceleration():

    def __init__(self, displacement=None, initial_velocity=None, final_velocity=None, acceleration=None, time=None, num_intervals=10):

        if time < 0 and time is not None:
            raise ValueError("Time must be greater than or equal to 0 seconds")
        try:
            self._s = np.linspace(0, displacement, num_intervals)
        except:
            self._s = displacement
        self._u = initial_velocity
        try:
            self._v = np.linspace(0, final_velocity, num_intervals)
            self.final_velocity = self._v[-1]
        except:
            self._v = final_velocity
        self._a = acceleration
        try:
            self._t = np.linspace(0, time, num_intervals)
        except:
            self._t = time

    def calculate_displacement(self):

        if self._u is not None and self._v is not None and self._t is not None:
            self._s = ((self._u + self._v) * self._t) / 2
        elif self._v is not None and self._t is not None and self._a is not None and self._t is not None:
            self._s = (self._v * self._t) - (0.5 * self._a * np.power(self._t, 2))
        elif self._u is not None and self._t is not None and self._a is not None and self._t is not None:
            self._s = (self._u + self._t) +(0.5 * self._a + np.power(self._t,2))
        else:
            raise Exception("Unable to calculate the displacement based on input values")

        self.displacement  = self._s[-1]
        return self.displacement

    def calculate_velocity(self):

        if self._u is not None and self._a is not None and self._t is not None:
            self._v = self._u + (self._a * self._t)
        elif self._u is not None and self._a is not None and self._s is not None:
            self._v = np.sqrt(self._u**2 + (2 * self._a * self._s))
        else:
            raise Exception("Unable to calculate the velocity based on input values")

        self.final_velocity = self._v[-1]
        return self.final_velocity

    def calculate_acceleration(self):

        if self._u is not None and self._v is not None and self._t is not None:
            self._a = (self._v - self._u) / self._t
            self.acceleration = self._a[-1]
            return self.acceleration

    def calculate_time(self):

        pass

    def maximum_height(self):

        # Max height when final velocity = 0 m/s
        # s = -u**2/2a

        self._max_height = -np.power(self._u, 2) / (2*self._a)
        print(self._max_height)
    
    def print_velocity(self):
        print(self.final_velocity, " m/s")

    def print_displacement(self):
        print(self.displacement, " m")

class ProjectileMotion(ConstantAcceleration):

    def __init__(self, displacement=None, initial_velocity=None, final_velocity=None, acceleration=None, time=None, angle = 0, num_intervals=10):

        ConstantAcceleration.__init__(self, displacement, initial_velocity, final_velocity, acceleration, time, num_intervals)
        self._angle = angle
        self.resolve_velocity()

    def resolve_velocity(self):

        self._vertical = self._u * m.sin(self._angle)
        self._horizontal = self._u * m.cos(self._angle)

if  __name__ == "__main__":

    import matplotlib.pyplot as plt

    #c = ConstantAcceleration(initial_velocity = 10, acceleration = 10, time=20) 
    #c = ConstantAcceleration(initial_velocity = 10, acceleration=2.5, final_velocity = 50, time=50)
    #vel = c.calculate_velocity()
    #print(vel)
    #disp = c.calculate_displacement()
    #c.print_displacement()
    #print(c._s)
    #c.maximum_height()
    #plt.plot(c._t, c._s)
    #plt.show()

    projectile = ProjectileMotion(initial_velocity = 10, acceleration = 10, angle = 15, time=20)
    print(projectile._vertical, projectile._horizontal)
