import matplotlib.pyplot as plt
import SirPy

pop = SirPy.Population(10000) 
data = pop.update_n_days(100)
Sus = [day[0] for day in data] 
Inf = [day[1] for day in data] 
Rec = [day[2] for day in data] 
plt.plot(range(0, 100), Sus)
plt.plot(range(0, 100), Inf)
plt.plot(range(0, 100), Rec)
plt.show()
