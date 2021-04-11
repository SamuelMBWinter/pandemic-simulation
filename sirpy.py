import random
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Random number generator
rng = np.random.default_rng()

class Person:
    def __init__(self, transmission_window, recovery_period, death_rate):
        self.infection_status = 's'
        self.transmission_window = transmission_window
        self.recovery_period = recovery_period
        self.death_rate = death_rate
        self.days_infected = 0
        self.days_recovered = 0 

    def update(self):
        if self.infection_status == 'i':
            if self.days_infected >= self.transmission_window:
                if rng.random() > self.death_rate:
                    self.infection_status = 'r'
                    self.days_infected = 0
                    return 1
                else:
                    self.infection_status = 'd'
                    return 2
            else:
                self.days_infected += 1
                return 0
        
        elif self.infection_status == 'r':
            if self.days_recovered >= self.recovery_period:
                self.infection_status = 's'
                self.days_recovered = 0
                return 3
            else:
                self.days_recovered += 1
                return 0
        else:
            return 0

    def __repr__(self):
        return f'Person("{self.infection_status}")'

class Population:
    def __init__(self,
            size, 
            initial_infections, 
            contact_mean, 
            transmission_chance, 
            transmission_window, 
            recovery_period, 
            death_rate
            ):
        self.people = [
                Person(
                    transmission_window, 
                    recovery_period, 
                    death_rate
                    ) for i in range(size)
                ] 
        
        self.size = len(self.people)
        self.contact_mean = contact_mean
        self.transmission_chance = transmission_chance
        
        ###
        #Fix the beneath code
        ###
        self.people[0].infection_status = 'i'
        self.people[0].update()

        self.susceptible = self.size - initial_infections
        self.infected = initial_infections
        self.recovered = 0
        self.dead = 0

    def print_people(self):
        print(self.people)

    def update_day(self):
        # Works genereates the transmissison events and the people enwly infected
        to_be_infected = set()
        for person in self.people:
            if person.infection_status == 'i':
                contacts = rng.poisson(lam=self.contact_mean)
                while contacts > 0:
                    if rng.random() < self.transmission_chance:
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
            elif state == 3:
                self.susceptible += 1
                self.recovered -= 1
            else:
                pass
        
        return self.susceptible, self.infected, self.recovered, self.dead

    def update_n_days(self, n):
        ls = []
        for i in range(n):
            ls.append(self.update_day())
        return ls

def get_graph(
        days=100,
        size=100, 
        initial_infections=1, 
        contact_mean=0.267, 
        transmission_chance=0.015, 
        transmission_window=7, 
        recovery_period=40, 
        death_rate=0.02
        ):

    pop = Population(
            size,
            initial_infections, 
            contact_mean, 
            transmission_chance, 
            transmission_window, 
            recovery_period, 
            death_rate
            ) 

    data = pop.update_n_days(days)

    days = list(range(1, len(data)+1))

    susceptibles = np.array([day[0] for day in data])
    infections = np.array([day[1] for day in data])
    recoveries = np.array([day[2] for day in data])
    deaths = np.array([day[3] for day in data])

    fig = go.Figure(data=[
        go.Bar(name='Infected', x=days, y=infections, width = 1),
        go.Bar(name='Recovered', x=days, y=recoveries, width = 1),
        go.Bar(name='Suceptible', x=days, y=susceptibles, width = 1),
        go.Bar(name='Deaths', x=days, y=deaths, width = 1),
        ])
   
    fig.update_layout(barmode='stack')
    
    return fig
