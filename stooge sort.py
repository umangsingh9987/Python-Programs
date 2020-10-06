
#https://m.facebook.com/story.php?story_fbid=348161766403412&id=100036287730638&ref=bookmarks

#subscribed by Ananda Krishnan Nair 
# Python program to implement stooge sort

def stoogesort(arr, l, h):
	if l >= h:
		return

	# If first element is smaller
	# than last,swap them
	if arr[l]>arr[h]:
		t = arr[l]
		arr[l] = arr[h]
		arr[h] = t

	# If there are more than 2 elements in
	# the array
	if h-l+1 > 2:
		t = (int)((h-l+1)/3)

		# Recursively sort first 2/3 elements
		stoogesort(arr, l, (h-t))

		# Recursively sort last 2/3 elements
		stoogesort(arr, l+t, (h))

		# Recursively sort first 2/3 elements
		# again to confirm
		stoogesort(arr, l, (h-t))


# deriver 
arr = [2, 4, 5, 3, 1]
n = len(arr)

stoogesort(arr, 0, n-1)

for i in range(0, n):
	print(arr[i], end = \' \')

