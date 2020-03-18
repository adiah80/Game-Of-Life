import tkinter as tk
import numpy as np
import time
import json

from simulate import GameOfLife
from utils import ApplyInitialization
from patterns import patternsDict
from initalizations import initializationsDict as inits

if __name__ == '__main__':

	# Import config from `config.json`
	with open('config.json') as jsonFile: 
		config = json.load(jsonFile)

	### Handle Inputs ###
	print("========================================================================")
	print("NOTE : Simply press 'Enter' for defaults.\n")

	maxGenerations = \
		int(input("(1) Enter number of generations to simulate [Default is 10000] : ") \
			or config['maxGenerations'])

	updateTime = \
		int(input("(2) Enter time (is ms) between updates [Default is 10ms] : ") \
			or config['updateTime'])

	initializationChoices = [
		"StillLife",
		"Oscillators",
		"AcornSpread",
		"EngineSpread",
		"Guns",
		"Pulsars",
		"ShipsSimple",
		"ShipsCollision",
		"ShipsDestroyed",
	]

	print("\nInitialization choices : ")
	for idx, initializationName in enumerate(initializationChoices):
		print("\t[{:d}] {:s}".format(idx, initializationName))

	initChoice = \
		int(input("\n(3) Choose the Initialization index to simulate [Default is '8'] : ") or 8)
	initialization = initializationChoices[initChoice]

	print("\nLoading simulation...")

	# Load simulation params from config and user input.
	maxGenerations = maxGenerations				# total number of generations
	updateTime = updateTime						# in millSeconds
	numRows = config['numRows'] 				# number of cell-rows in the grid 
	numCols = config['numCols'] 				# number of cell-columns in the grid
	gridHeight = config['gridHeight']			# total height of the grid
	gridWidth = config['gridWidth'] 			# total width of the grid

	# Define root window.
	root = tk.Tk()
	
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
	print("========================================================================")