#   File: walker.py
#   Author: Nawaf Abdullah
#   Creation Date: 19/Mar/2018
#   Description: Modeling of the random walker problem in 1D, 2D and 3D


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from itertools import count


class Walker:
    _ids = count(0)

    def __init__(self):
        self.id = next(self._ids)
        self.zSwitch = False
        self.x = [0]
        self.y = [0]
        self.z = [0]

    def reset(self):
        """
        Resets the walker's path
        """
        del self.x[:]
        del self.y[:]
        del self.z[:]

    def walk_1D(self, num_steps):
        """
        Calculates the walker path in 1D over time steps
            - In this method, the y-axis (self.y) is used as a time axis
        :param num_steps: number of steps
        :return: the walker path (self.x) vs time (self.y)
        """
        for i in range(num_steps - 1):
            r = random.randint(0, 100)
            if r > 50:
                self.x.append(self.x[i] + 1)
            else:
                self.x.append(self.x[i] - 1)
            self.y.append(self.y[i] + 1)
        self.zSwitch = False
        return self.x, self.y

    def walk_2D(self, num_steps):
        """
        Calculates the walker path in 2D
        :param num_steps: number of steps
        :return: the walker path in 2D: self.x, self.y
        """
        for i in range(num_steps-1):
            r = random.randint(0, 100)
            if r <= 25:
                self.x.append(self.x[i] + 1)
                self.y.append(self.y[i])
            elif 25 < r <= 50:
                self.x.append(self.x[i] - 1)
                self.y.append(self.y[i])
            elif 50 < r <= 75:
                self.y.append(self.y[i] + 1)
                self.x.append(self.x[i])
            else:
                self.y.append(self.y[i] - 1)
                self.x.append(self.x[i])
        self.zSwitch = False
        return self.x, self.y

    def walk_3D(self, num_steps):
        """
        Calculates the walker path in 3D
        :param num_steps: number of steps
        :return: the walker path in 3D: self.x, self.y, self.z
        """
        for i in range(num_steps-1):
            r = random.randint(0, 100)
            if r <= 16.66:
                self.x.append(self.x[i] + 1)
                self.y.append(self.y[i])
                self.z.append(self.z[i])
            elif 16.66 < r <= 33.32:
                self.x.append(self.x[i] - 1)
                self.y.append(self.y[i])
                self.z.append(self.z[i])
            elif 33.32 < r <= 49.98:
                self.y.append(self.y[i] + 1)
                self.x.append(self.x[i])
                self.z.append(self.z[i])
            elif 49.98 < r <= 66.64:
                self.y.append(self.y[i] - 1)
                self.x.append(self.x[i])
                self.z.append(self.z[i])
            elif 66.64 < r < 83.33:
                self.z.append(self.z[i] + 1)
                self.x.append(self.x[i])
                self.y.append(self.y[i])
            else:
                self.z.append(self.z[i] - 1)
                self.x.append(self.x[i])
                self.y.append(self.y[i])
        self.zSwitch = True
        return self.x, self.y, self.z

    def plot(self):
        """

        Plots the walker's path in 2D or 3D
        """
        if self.zSwitch is True:
            ax = plt.axes(projection='3d')
            ax.plot3D(self.x, self.y, self.z, 'gray')
            plt.show()
        else:
            fig1 = plt.figure(1)
            fig1.suptitle("Walker's Path")
            plt.xlabel("x-position")
            plt.ylabel("y-position")
            plt.plot(self.x, self.y)
            plt.show()