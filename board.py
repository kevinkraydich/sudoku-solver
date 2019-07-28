class Board:
	def __init__(self, input_board = []):
		if input_board:
			self.board = input_board.copy()
		else:
			self.reset()

	def reset(self):
		self.board = [['.' for _ in range(9)] for _ in range(9)]

	def print(self):
		for r in range(9):
			for c in range(9):
				print(self.board[r][c], end=' ')
			print()

	def solve(self):
		row, col = self.find_first_empty()

		if (row, col) == (-1, -1):
			return True

		for i in map(str, range(1, 10)):
			if self.is_move_valid(row, col, i):
				self.board[row][col] = i
				if self.solve():
					return True
				self.board[row][col] = '.'

	def is_valid(self):
		row = [set() for _ in range(9)]
		col = [set() for _ in range(9)]
		box = [[set() for _ in range(3)] for _ in range(3)]

		for r in range(9):
			for c in range(9):
				if not self.board[r][c].isdigit():
					continue

				x = r // 3
				y = c // 3
				num = self.board[r][c]

				if (num in row[r]) or (num in col[c]) or (num in box[x][y]):
					return False
				else:
					row[r].add(num)
					col[c].add(num)
					box[x][y].add(num)
		return True

	def is_move_valid(self, row, col, ch):
		row_valid = all(self.board[row][_] != ch for _ in range(9))
		col_valid = all(self.board[_][col] != ch for _ in range(9))
		box_valid = all(self.board[r][c] != ch for r in self.box_range(row) for c in self.box_range(col))
		return row_valid and col_valid and box_valid

	def find_first_empty(self):
		for r in range(9):
			for c in range(9):
				if self.board[r][c] == '.':
					return r, c
		return -1, -1

	def box_range(self, x):
		x -= x % 3
		return range(x, x + 3)