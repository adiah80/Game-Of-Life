import tkinter as tk
import numpy as np
import time

class GameOfLife:
	def __init__(self, gridName, root, numRows, numCols, gridHeight, gridWidth):

		self.gridName = gridName	# Name to display
		self.root = root			# Root window
		self.numRows = numRows		# Number of cells in a row
		self.numCols = numCols		# Number of cells in a column
		self.generationNo = 0		# Generation number
		self.totalCells = 0			# Number of alive cells

		# Make label
		self.labelText = tk.StringVar()		# Label text that is updated
		self.label = tk.Label(
			self.root, 
			textvariable=self.labelText, 
			relief="raised",
			font = ("Times New Roman", 20),
			justify = "left",
			width = 40,
		)
		self.label.pack()

		# Make Canvas
		self.root.title("Conway's Game of Life")
		self.c = tk.Canvas(self.root, height=gridHeight, width=gridWidth, bg='white')
		self.c.pack(fill=tk.BOTH, expand=True)
		self.c.bind('<Configure>', self.MakeGrid)		# Calls MakeGrid		

		# Initialize numpy grid to keep track of cell states.
		self.isAlive = np.zeros([self.numRows, self.numCols])

	def MakeGrid(self, event=None):
		"""
		Makes horizontal and vertical lines on the canvas.
		# Refer : https://stackoverflow.com/a/34011751
		"""

		self.c.delete('grid_line') 				# Remove previous frids	
		curWidth = self.c.winfo_width() 		# Get width of canvas
		curHeight = self.c.winfo_height() 		# Get height of canvas
		cellWidth = curWidth // self.numCols	# Get width for one cell
		cellHeight = curHeight // self.numRows	# Get height for one cell

		# Creates all vertical lines
		for i in range(0, cellWidth * self.numCols, cellWidth):
			self.c.create_line([(i, 0), (i, curHeight)], tag='grid_line')	

		# Creates all horizontal lines
		for i in range(0, cellHeight*self.numRows, cellHeight):
			self.c.create_line([(0, i), (curWidth, i)], tag='grid_line')


	def FillGrid(self):
		"""
		Fills the 'alive' cells with black sqaures on the grid,
		using the `isAlive` matrix.
		"""

		# Refer : https://stackoverflow.com/a/49216638
		self.c.update()

		curWidth = self.c.winfo_width() 	
		curHeight = self.c.winfo_height() 
		cellWidth = curWidth // self.numCols
		cellHeight = curHeight // self.numRows

		# Delete previous coloured cells
		self.c.delete('cells')

		# For each cell, if alive, fill the corressponding grid cell.
		for cRow in range(self.numRows):
			for cCol in range(self.numCols):
				if(self.isAlive[cRow][cCol]):
					top = (cCol * cellWidth, cRow * cellHeight)
					bottom = ((cCol+1) * cellWidth, (cRow+1) *cellHeight)
					self.c.create_rectangle([top, bottom], fill="black", tag='cells')			
	
	def DrawPattern(self, pattern, offsetRow, offsetCol):
		"""
		Draw a pattern on the (empty) grid.
		`pattern` contains a list of cell coordinates 
		which represent the cells to fill. 
		"""

		for [row,col] in pattern:
			nRow = row + offsetRow
			nCol = col + offsetCol
			self.isAlive[nRow][nCol] = 1
			self.totalCells += 1

	def GetNeighbourSum(self, curRow, curCol):
		"""
		Get the number of alive neighbours for the cell
		at cordinates : [curRow, curCol].
		"""
		
		sum = 0;
		dRow = [-1,-1,-1, 0 , 0, 1, 1, 1]
		dCol = [-1, 0, 1, -1, 1,-1, 0, 1]

		for idx in range(8):
			newRow = curRow + dRow[idx]
			newCol = curCol + dCol[idx]

			if(newRow < 0 or newRow >= self.numRows): continue
			if(newCol < 0 or newCol >= self.numCols): continue
			sum += self.isAlive[newRow][newCol]

		return sum

	def MakeUpdate(self):
		"""
		Update the grid and the window label.
		"""

		isAliveUpdated = np.array(self.isAlive)
		oldCellCount = self.totalCells

		# Update the cells
		for cRow in range(self.numRows):
			for cCol in range(self.numCols):
				numNeigh = self.GetNeighbourSum(cRow, cCol)

				# Toggle alive cell
				if(self.isAlive[cRow][cCol] and (numNeigh<2) or (numNeigh>3)):
					isAliveUpdated[cRow][cCol] = 0

				# Toggle dead cell
				if(not self.isAlive[cRow][cCol] and numNeigh == 3):
					isAliveUpdated[cRow][cCol] = 1
					self.totalCells += 1

		self.isAlive = isAliveUpdated
		self.generationNo += 1

		# Text to display on label	
		displayText = \
			"GRID TYPE : {:s} \nGENERATION : {:d} \nNEW CELLS GENERATED : {:d} \nTOTAL CELLS GENERATED: {:d}" \
			.format(self.gridName, self.generationNo, self.totalCells-oldCellCount, self.totalCells)	
		
		# Update the label
		self.labelText.set(displayText)
		self.root.update_idletasks()		

