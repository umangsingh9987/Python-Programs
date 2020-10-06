matrix = [
	[1,  2,  3,  4],
	[12, 13, 14, 5],
	[11, 16, 15, 6],
	[10, 9,  8,  7]
]

def spiral_traverse(arr):
	row_start, row_end = 0, len(arr)
	col_start, col_end = 0, len(arr[0])
	res = []

	if row_end - row_start <= 1:
		return arr[row_start]

	if col_end - col_start <= 1:
		return [row[0] for row in arr]

	while row_start < row_end and col_start < col_end:
		for col in range(row_start, row_end):
			res.append(arr[row_start][col])
		res.pop()

		for row in range(col_start, col_end):
			res.append(arr[row][col_end-1])
		res.pop()

		for col in reversed(range(col_start, col_end)):
			res.append(arr[row_end-1][col])
		res.pop()

		for row in reversed(range(row_start, row_end)):
			res.append(arr[row][col_start])
		res.pop()

		row_start += 1
		row_end -= 1
		col_start += 1
		col_end -= 1
	
	return res

if __name__ == "__main__":
	print(spiral_traverse(matrix))
