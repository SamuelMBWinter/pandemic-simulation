import random
import numpy as np
import matplotlib.pyplot as plt

## Defining constats for the simulation
T = 0.01    # Transmission chance
C = 0.267   # Mean number of contacts
I = 1       # Initial number of infected people
D = 10      # infectious days

death_rate = 0.02 

# Random number generator
rng = np.random.default_rng()

class Person:
    def __init__(self, infection_status='s'):
        self.infection_status = infection_status
        self.days_infected = 0
    
    def update(self):
        if self.infection_status == 'i':
            if self.days_infected >=D:
                if rng.random() > death_rate:
                    self.infection_status = 'r'
                    self.days_infected = 0
                    return 1
                else:
                    self.infection_status = 'd'
                    return 2
            else:
                self.days_infected += 1
                return 0
        else:
            return 0

    def __repr__(self):
        return f'Person("{self.infection_status}")'

class Population:
    def __init__(self, N):
        self.people = [Person('s') for i in range(N)] # Generates a list of people
        self.size = len(self.people)

        self.people[0].infection_status = 'i'
        self.people[0].update()

        self.susceptible = self.size - I
        self.infected = I
        self.recovered = 0
        self.dead = 0

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
            state = person.update()
            if state == 1:
                self.recovered += 1
                self.infected -= 1
            elif state == 2:
                self.dead += 1
                self.infected -=1
            else:
                pass
        
        return self.susceptible, self.infected, self.recovered, self.dead

    def update_n_days(self, n):
        ls = []
        for i in range(n):
            ls.append(self.update_day())
        return ls
