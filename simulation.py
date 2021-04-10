import random
import numpy as np
import matplotlib.pyplot as plt

class Person:
    def __init__(self, infection_status='s'):
        self.infection_status = infection_status

    def __repr__(self):
        return f'Person("{self.infection_status}")'

class Polulation:
    def __init__(self, N):
        self.people = [Person('s') for i in range(N)] # Generates a list of people
        self.size = len(self.people)
    
    def print_people(self):
        print(self.people)

    def update_day(self):
        to_be_infected = set()
        for person in self.people:
            if person.infection_status == 'i':
                
                contacts = np.floor(self.size * random.random() ** 2)
                
                while contacts > 0:
                    to_be_infected.add(random.randint(0, self.size))
                    contacts -=1

            else:
                pass
        for num in to_be_infected:
            self.people[num].infection_status = 'i'
    
    def update_n_days(self, n):
        for i in range(n):
            self.update_day()


if __name__ == '__main__':
    pop = Polulation(5) 
    spawn = pop.people[0]
    spawn.infection_status = 'i'
    pop.print_people()

    pop.update_day()

    pop.print_people()

