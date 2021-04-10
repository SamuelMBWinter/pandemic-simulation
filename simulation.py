import random
import numpy as np
import matplotlib.pyplot as plt

## Defining constats for the simulation
T = 0.01    # Transmission chance
C = 0.267   # Mean number of contacts
I = 1       # Initial number of infected people
D = 10      # infectious days

# Random number generator
rng = np.random.default_rng()

class Person:
    def __init__(self, infection_status='s'):
        self.infection_status = infection_status
        self.days_infected = 0
    
    def update(self):
        if self.infection_status == 'i':
            if self.days_infected >=D:
                self.infection_status = 'r'
                self.days_infected = 0
                return 1
            else:
                self.days_infected += 1
                return 0
        else:
            return 0

    def __repr__(self):
        return f'Person("{self.infection_status}")'

class Polulation:
    def __init__(self, N):
        self.people = [Person('s') for i in range(N)] # Generates a list of people
        self.size = len(self.people)

        self.people[0].infection_status = 'i'
        self.people[0].update()

        self.susceptible = self.size - I
        self.infected = I
        self.recovered = 0
    
    def print_people(self):
        print(self.people)

    def update_day(self):
        # Works genereates the transmissison events and the people enwly infected
        to_be_infected = set()
        for person in self.people:
            if person.infection_status == 'i':
                contacts = rng.poisson(lam=C)
                while contacts > 0:
                    if rng.random() < T:
                        to_be_infected.add(rng.integers(0, self.size-1))
                        contacts -=1
                    else:
                        pass
            else:
                pass
        
        for num in to_be_infected:
            if self.people[num].infection_status == 's':
                self.people[num].infection_status = 'i'
                self.infected += 1
                self.susceptible -= 1
            else:
                pass
        
        for person in self.people:
            if person.update():
                self.recovered += 1
                self.infected -= 1
            else:
                pass
        
        return self.susceptible, self.infected, self.recovered

    def update_n_days(self, n):
        ls = []
        for i in range(n):
            ls.append(self.update_day())
        return ls
    

if __name__ == '__main__':
    pop = Polulation(10000) 
    data = pop.update_n_days(100)
    Sus = [day[0] for day in data] 
    Inf = [day[1] for day in data] 
    Rec = [day[2] for day in data] 
    plt.plot(range(0, 100), Sus)
    plt.plot(range(0, 100), Inf)
    plt.plot(range(0, 100), Rec)
    plt.show()
