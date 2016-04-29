from collections import defaultdict
import random
import time

from population import Population
from disaster import Disaster
from person import Person

def sampleDriver():
    # initial inputs
    random.seed(0) #seed the random number generator
    death_dict = defaultdict(list)
    people_born = {k: 0 for k in range(9)}
    people_born[0] = 50 # initial population
    max_sim_time = 500 # max number of iterations
    population = Population()
    disaster = Disaster(population)

    for cur_sim_time in range(max_sim_time):
        print 'current sim time:', cur_sim_time
        start = time.time()

        if random.random() <= 0.01:
            ratio = random.random()/4.0
            disaster.createDisaster(ratio)
            print 'DISASTER killed', ratio, 'in:', time.time() - start
            start = time.time()

        # Adding newborns
        for add_count in range (people_born.get(cur_sim_time % 9, 0)):
            population.add_person(Person(cur_sim_time, population.get_rand_death_time(cur_sim_time), random.random()))
        print 'added', people_born.get(cur_sim_time % 9, 0), 'people in', time.time()-start

        # Removing the dead
        start = time.time()
        population.remove_dead(cur_sim_time)
        print 'removed', len(population.death_dict.get(cur_sim_time, [])), 'people in:', time.time() - start

        # Calculating total kcal
        start = time.time()
        total_kcal = population.kcal_requirements(cur_sim_time)
        print 'completed total kcal in:', time.time() - start

        # Calculating how many newborns to be created in 9 months time
        num_people = population.num_people()
        people_born[cur_sim_time % 9] = random.randint(int(num_people*0.01), int(num_people*0.05))
        print 'total people:', num_people, 'and total kcal:', total_kcal, '\n'

sampleDriver()