class Person:
    def __init__(self, infection_status='s'):
        self.infection_status = infection_status

    def __repr__(self):
        return f'Person("{self.infection_status}")'

class Polulation:
    def __init__(self, N):
        self.people = [Person('s')] * N

    def print_people(self):
        print(self.people)

    def 
pop = Polulation(5)
pop.print_people()
