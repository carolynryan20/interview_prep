#!/usr/bin/python

import psycopg2
import getpass
#    cd /Accounts/courses/cs257/adalal/web/ryanc2
class datasource:

	def __init__(self):
		pass
	
	""" A method to log into the database for each query """
	def logInToDatabase():
		try:
			connection = psycopg2.connect(database='ryanc2', user='ryanc2', password='fluffy578cow')
			return connection
		except Exception, e:
# 			print 'Connection error: ', e
			return False
		
	#Methods that return all of a specified column 
	'''
    Returns a list of the planet names of each exoplanet in the database
    '''
	def getPlanetName():
		connection = logInToDatabase()
		if not connection:
			return False
		
		else: 
			# Query the database
			planetNameList = []
			try:
				cursor = connection.cursor()
				query = 'SELECT planet_name FROM exoplanets'
				cursor.execute(query)
				for row in cursor.fetchall():
					planetNameList.append(row)

			except Exception, e:
				return False

		connection.close()
		return planetNameList
	
	'''
	Returns a list of the planet masses of each exoplanet in the database
	'''
	def getMass(self):
		connection = logInToDatabase()
		if not connection:
			return False
		
		else: 
			# Query the database
			planetMassList = []
			try:
				cursor = connection.cursor()
				query = 'SELECT mass FROM exoplanets'
				cursor.execute(query)
				for row in cursor.fetchall():
					planetMassList.append(row)

			except Exception, e:
				return False

		connection.close()
		return planetMassList
		
	'''
	Returns a list of the radius of each exoplanet in the database
	'''	
	def getRadius(self):
		connection = logInToDatabase()
		if not connection:
			return False
		
		else: 
			# Query the database
			planetRadiusList = []
			try:
				cursor = connection.cursor()
				query = 'SELECT radius FROM exoplanets'
				cursor.execute(query)
				for row in cursor.fetchall():
					planetRadiusList.append(row)

			except Exception, e:
				return False

		connection.close()
		return planetRadiusList
		
	'''
	Returns a list of the star name of each exoplanet in the database
	'''		
	def getStarName(self):
		connection = logInToDatabase()
		if not connection:
			return False
		
		else: 
			# Query the database
			planet{INSERTHERE}List = []
			try:
				cursor = connection.cursor()
				query = 'SELECT {INSERTHERE} FROM exoplanets'
				cursor.execute(query)
				for row in cursor.fetchall():
					planet{INSERTHERE}List.append(row)

			except Exception, e:
				return False

		connection.close()
		return planet{INSERTHERE}List
		
	'''
	Returns a list of the right ascension (ra) of each exoplanet in the database
	'''	
	def getRightAscension(self):
		return []
	'''
	Returns a list of the declination (dec) of each exoplanet in the database
	'''	
	def getDeclination(self):
		return []


	#Methods that return all rows that match a specified column value
	'''
	Returns all exoplanets with given name
	'''	
	def findPlanetName(self, planetName):
		return []
		
	'''
	Returns all exoplanets with given mass
	'''
	def findMass(self, mass):
		return []
		
	'''
	Returns all exoplanets within given mass range
	'''	
	def findMassRange(self, lowerMass, upperMass):
		
		return []
		
	'''
	Returns all exoplanets with given radius
	'''	
	def findRadius(self, radius):
		
		return []
		
	'''
	Returns all exoplanets within given radius range
	'''
	def findRadiusRange(self, lowerRadius, upperRadius):
		
		return []

	'''
	Returns all exoplanets with given star name
	'''
	def findStarName(self, starName):
		
		return []
	'''
	Returns all exoplanets with given ra
	'''
	def findRightAscension(self, ra):
		
		return[]
	
	'''
	Returns all exoplanets within given ra range
	'''	
	def findRightAscensionRange(self, lowerRA, upperRA):
		
		return []
		
	'''
	Returns all exoplanets with given dec
	'''
	def findDeclination(self, dec):
		
		return[]
		
	'''
	Returns all exoplanets within given dec range
	'''	
	def findDeclinationRange(self, lowerDec, upperDec):
		
		return []
		
		
		
		
		
		
		
		
		
