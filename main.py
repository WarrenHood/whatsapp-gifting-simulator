NUM_PEOPLE = 100000
STARTING_CASH = 1000
JOIN_CASH = 1000
SIMULATION_DAYS = 1000
DAY = 0

people = [STARTING_CASH for i in range(NUM_PEOPLE)]
groups = []


class Group:
    people_indices = []
    last_day = 0
    
    def __init__(self, day, group=[]):
        global groups
        self.people_indices = group
        groups += [self]
        self.last_day = day
    
    def join(self, person):
        global DAY
        if people[person] < JOIN_CASH:
            return

        people[person] -= JOIN_CASH
        people[self.people_indices[0]] += JOIN_CASH
        self.people_indices += [person]

        self.last_day = DAY
        
        if len(self.people_indices) == 11:
            self.split()

    def split(self):
        g1_indices = self.people_indices[1::2]
        g2_indices = self.people_indices[2::2]

        groups.remove(self)
        Group(self.last_day, g1_indices)
        Group(self.last_day, g2_indices)

def recruitNew(person_index):
    global DAY
    for i in range(len(groups)):
        if groups[i].last_day != DAY:
            groups[i].join(person_index)
            return True
    return False

print("Running simulation with initial group of 5 people")
print("Population size: {:d}".format(NUM_PEOPLE))
print("Starting cash per person: {:d}".format(STARTING_CASH))
print("Joining fee: {:d}".format(JOIN_CASH))


#Initial group with 5 people
Group(0, [0,1,2,3,4])

currentPerson = 5

# simulate SIMULATION_DAYS days
for day in range(SIMULATION_DAYS):
    
    while currentPerson < NUM_PEOPLE and recruitNew(currentPerson):
        currentPerson += 1

    DAY += 1


#Analysis
num_gained = 0
num_broke_even = 0
num_lost_out = 0
    
for p in range(len(people)):
    if people[p] < STARTING_CASH:
        num_lost_out += 1
    elif people[p] == STARTING_CASH:
        num_broke_even += 1
    elif people[p] > STARTING_CASH:
        num_gained += 1
    #print("Person {:d} ended up with {:d}".format(p, people[p]))

print("Results after {:d} days:".format(SIMULATION_DAYS))
print("Count of people who lost all their money: {:d}".format(num_lost_out))
print("Count of people who broke even: {:d}".format(num_broke_even))
print("Count of people who gained: {:d}".format(num_gained))
print("Total groups formed in the end: {:d}".format(len(groups)))



        
