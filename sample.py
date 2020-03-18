import tkinter as tk
import numpy as np
import time
import json

from simulate import GameOfLife
from utils import ApplyInitialization
from patterns import patternsDict
from initalizations import initializationsDict as inits

if __name__ == '__main__':

	# Import config from `config.json`/
	with open('config.json') as jsonFile: 
		config = json.load(jsonFile)

	# Load simulation params from config.
	maxGenerations = config['maxGenerations']	# total number of generations
	updateTime = config['updateTime']			# in millSeconds
	numRows = config['numRows'] 				# number of cell-rows in the grid 
	numCols = config['numCols'] 				# number of cell-columns in the grid
	gridHeight = config['gridHeight']			# total height of the grid
	gridWidth = config['gridWidth'] 			# total width of the grid

	# Define root figure
	root = tk.Tk()

	# Select which pattern set to initialize on the grid.
	# Options avaliable in `initalizations.py
	initialization = "StillLife"
	initialization = "Oscillators"
	initialization = "AcornSpread"
	initialization = "EngineSpread"
	initialization = "Guns"
	initialization = "Pulsars"
	initialization = "ShipsSimple"
	initialization = "ShipsCollision"
	initialization = "ShipsDestroyed"	# Latest selected.

	# Get simulation object.
	gameOfLife = GameOfLife(
					initialization,
					root, 
					numRows, 
					numCols,
					gridHeight,
					gridWidth
				)
	# Apply the chosed initialization to the grid.
	ApplyInitialization(inits[initialization], gameOfLife)

	# Run the simulation.
	for generation in range(maxGenerations):
		try:
			gameOfLife.FillGrid()
			gameOfLife.MakeUpdate()
			time.sleep(updateTime/1000)
		except:
			# If window is closed.
			print("Window closed by user.")
			break

	print("Simulation over.")