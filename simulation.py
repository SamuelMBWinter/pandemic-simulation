import matplotlib.pyplot as plt
import SirPy

pop = SirPy.Population(10000) 
data = pop.update_n_days(100)
Sus = [day[0] for day in data] 
Inf = [day[1] for day in data] 
Rec = [day[2] for day in data] 
Dea = [day[3] for day in data] 
line1 = plt.plot(range(0, 100), Sus, label='Sus')
line2 = plt.plot(range(0, 100), Inf, label='Inf')
line3 = plt.plot(range(0, 100), Rec, label='Rec')
line4 = plt.plot(range(0, 100), Dea, label='Dea')
plt.legend()
plt.show()
