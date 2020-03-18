from patterns import patternsDict

def ApplyInitialization(initName, gameOfLifeObject):
	"""
	Applies the initialization - `initName` from
	`initalizations.py` to the simulation object  
	`gameOfLifeObject`.

	Used for initializing the grid before beggining
	the simulation.
	"""
	
	for patternName in initName:
		gameOfLifeObject.DrawPattern(
			patternsDict[patternName[0]], 
			offsetRow = patternName[1], 
			offsetCol = patternName[2]
		)