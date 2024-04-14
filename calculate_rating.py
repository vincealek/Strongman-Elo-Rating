import sys

from competition import *
from athlete import *
from math import sqrt


competitions = getCompetitionList()
athletes = getAthleteList(competitions)

def P(r1, r2) :
	return 1.0/(1.0+10.0**((r2-r1)/400))

def getSeed(competing_athletes, rating) :
	result = 1
	for athlete in competing_athletes :
		result += P(athlete.rating, rating)
	return result

def getRatingtoSeed(competing_athletes, rank) :
	lef = 1
	rig = 20000
	for i in range(100) :
		mid = (lef+rig)/2;
		if(getSeed(competing_athletes, mid) < rank) :
			rig = mid
		else :
			lef = mid
	return lef


def calculate_rating() :
	sorted_competitions = sorted(competitions, key=lambda x: x.date)
	for competition in sorted_competitions :
		if competition.type != "Open" :
			continue
		for result in competition.results :
			
			# find competing athlete
			competing_athletes = []
			for id in result :
				for athlete in athletes :
					if athlete.id == id :
						competing_athletes.append(athlete)
			
			# calculate seed
			seeds = []
			for athlete_1 in competing_athletes :
				seed = 1.0
				for athlete_2 in competing_athletes :
					if(athlete_1 != athlete_2) :
						seed += P(athlete_2.rating, athlete_1.rating)
				seeds.append(seed)

			print(competition.name)
			print(seeds)
			deltas = []
			for i in range(len(competing_athletes)):

				athlete = competing_athletes[i]
				other_athletes = []
				for athlete_2 in competing_athletes :
					if athlete_2 != athlete :
						other_athletes.append(athlete_2)

				
				actual_place = i+1
				seed = seeds[i];
				
				m = (actual_place+seed)/2
				mpr = getRatingtoSeed(other_athletes, m)
				delta = (mpr-athlete.rating)/2
				deltas.append(delta)
			
			new_deltas = []
			for i in range(len(competing_athletes)) :
				athlete = competing_athletes[i]
				delta = deltas[i]
				new_delta = delta-sum(deltas)/len(deltas)
				print(athlete.name + "		" + str(athlete.rating) + "		" + str(new_delta))
				athlete.rating += new_delta
				new_deltas.append(new_delta)
			# print(sum(new_deltas))
			print()

original_stdout = sys.stdout
with open('calculate_2.txt', 'w') as f:
	sys.stdout = f

	calculate_rating()
	sorted_athletes = sorted(athletes, key=lambda x: x.rating, reverse = True)
	for athlete in sorted_athletes :
		print(str(athlete.id) + " " + athlete.name + " " + str(athlete.rating))
    


# for competition in sorted_competitions :
	# print(competition.date, competition.id, competition.name)
# print(sorted_competitions)	
# print(athletes)