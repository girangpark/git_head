from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4, 6]

class Scattering:

    def Avg(self, data):
        avg = mean(data)
        return avg

    def var_sd(self, data):
        avg = self.Avg(data)
        diff = [(d - avg)**2 for d in data]
        var = sum(diff)/(len(data)-1)
        sd = sqrt(var)
        return var, sd

s = Scattering()

v, s = s.var_sd(x)
print(v)
print(s)

