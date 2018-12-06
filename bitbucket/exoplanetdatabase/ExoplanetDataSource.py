#!/usr/bin/python

class ExoplanetDataSource:

	def __init__(self):
		pass
		
	#Methods that return all of a specified column 
	def getPlanetName(self):
		'''
        Returns a list of the planet names of each exoplanet in the database
        '''
		return[]
	
	def getMass(self):
		'''
		Returns a list of the planet masses of each exoplanet in the database
		'''
		return []
		
	def getRadius(self):
		'''
		Returns a list of the radius of each exoplanet in the database
		'''
		return []
		
	def getStarName(self):
		'''
		Returns a list of the star name of each exoplanet in the database
		'''
		return []
		
	def getRightAscension(self):
		'''
		Returns a list of the right ascension (ra) of each exoplanet in the database
		'''
		return []
		
	def getDeclination(self):
		'''
		Returns a list of the declination (dec) of each exoplanet in the database
		'''
		return []


	#Methods that return all rows that match a specified column value
	def findPlanetName(self, planetName):
		'''
		Returns all exoplanets with given name
		'''
		return []

	def findMass(self, mass):
		'''
		Returns all exoplanets with given mass
		'''
		return []
	
	def findMassRange(self, lowerMass, upperMass):
		'''
		Returns all exoplanets within given mass range
		'''
		return []
	
	def findRadius(self, radius):
		'''
		Returns all exoplanets with given radius
		'''
		return []

	def findRadiusRange(self, lowerRadius, upperRadius):
		'''
		Returns all exoplanets within given radius range
		'''
		return []

	def findStarName(self, starName):
		'''
		Returns all exoplanets with given star name
		'''
		return []

	def findRightAscension(self, ra):
		'''
		Returns all exoplanets with given ra
		'''
		return[]
		
	def findRightAscensionRange(self, lowerRA, upperRA):
		'''
		Returns all exoplanets within given ra range
		'''
		return []
	
	def findDeclination(self, dec):
		'''
		Returns all exoplanets with given dec
		'''
		return[]
		
	def findDeclinationRange(self, lowerDec, upperDec):
		'''
		Returns all exoplanets within given dec range
		'''
		return []
