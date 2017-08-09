#===========================
# 00 Name generator
#===========================

#TODO: saving to file result JSN, CSV, XML
import random
from collections import Counter

#lists with names nad surnames to create new people
arrNames = ["Paul", "Andy", "Andrew", "Max", "Frank", "Tina", "Derek", "Bob", "Mary", "Simon", "Sandra", "Josh", "Samuel", "Henry", "Hank", "Joey", "July","Anna", "Patrick", "Steve", "Alex", "Agata", "Michael", "Chris", "Daphne", "Jon", "Mark", "Hannah", "Kevin", "James", "George", "Dick", "Robert", "Eliza", "Ron", "Amy", "Asher", "Taylor", "Robin", "Ed", "Victoria", "Bruce", "John", "Casper", "Kate", "Harry", "Rachel", "Monica", "Kelly", "Peter", "Christine", "Sarah", "Natalie", "Matthew", "Jack", "Wilson", "David", "Christian", "Barbara", "Justin", "Thomas"]
arrSurnames = ["Lee", "Grey", "Murray", "Star", "Deep", "Geller", "Young", "Dylan", "Clark", "Baker", "Cross", "Rock", "Jordan", "King", "Wood", "Morgan", "Anders", "Anderson", "Pratt", "Clarkson", "Eastwood", "Obama", "Jonas", "Smith", "Doe", "Curtis", "Roth", "Weber", "Johnson", "Perez", "Morales", "Parker", "Brown", "Black", "Greene", "Ford", "Donald", "Morisson", "Jackson", "Dallas", "Reacher", "Potter"]
arrPLdegrees = ["", "lic.", "inz.", "mgr", "mgr inz.", "dr", "dr inz", "prof.", "dr hab.", "prof. dr hab.", "dr hab. inz."]

#Function return new value with dictionary
def CreatePerson(firstName, lastName, deg):
	return {'fName':firstName, 'lName':lastName, 'deg':deg}

#Counts all people with given name
def CountPeopleByName(arrPersons, name):
	return Counter(per['fName'] for per in arrPersons)[name]

#Counts all people with given surname
def CountPeopleBySurname(arrPersons, surname):
	return len([per for per in arrPersons if per['lName'] == surname])

#Return number of people with given name and surname
def FindThatPerson(arrPersons, name, surname):
	return sum(1 for per in arrPersons if per.get('lName') == surname and per.get('fName') ==name)
#==========================================================================================

arrNames.sort()
arrSurnames.sort()

#print(arrNames)
#print(arrSurnames)
arrPersons = []								#create new empty list

#generate random numer list of person and add to the list
#by using uderscore it mean that I dont need this iterator
for _ in range(random.randrange(0, 300)):
	rnd_IdxdName = random.randrange(0, len(arrNames))					#from 0 to size of array
	rnd_IdxSurname = random.randrange(0, len(arrSurnames))
	rnd_IdxScienceDegree = random.randrange(0, len(arrPLdegrees))

	arrPersons.append(CreatePerson(arrNames[rnd_IdxdName], arrSurnames[rnd_IdxSurname], arrPLdegrees[rnd_IdxScienceDegree]))		#add to list

#sort arrPersons by surname
arrPersons = sorted(arrPersons, key=lambda per: per['lName'])		

#show everyone
for per in arrPersons:
	print(per['deg'], per['fName'], per['lName'])

rnd_IdxdName = random.randrange(0, len(arrNames))
rnd_IdxSurname = random.randrange(0, len(arrSurnames))

#show summary
print("\nThere is", CountPeopleByName(arrPersons, arrNames[rnd_IdxdName]), "people named", arrNames[rnd_IdxdName])
print("There is", CountPeopleBySurname(arrPersons, arrSurnames[rnd_IdxSurname]), "people with", arrSurnames[rnd_IdxSurname], "surname")
print("There is", FindThatPerson(arrPersons, arrNames[rnd_IdxdName], arrSurnames[rnd_IdxSurname]), "people named", arrNames[rnd_IdxdName], arrSurnames[rnd_IdxSurname])

#remove all people
arrPersons.clear() 