# Python Program to sort a linked list
# using bubble sort by swapping nodes
# Original source: https://www.geeksforgeeks.org/bubble-sort-for-linked-list-by-swapping-nodes/

# CODE BEGINS BELOW

# Node class
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to swap nodes x and y in linked list by
	# changing links
	def swapNodes(self, x, y):

		# Nothing to do if x and y are same
		if x == y:
			return

		# Search for x (keep track of prevX and CurrX)
		prevX = None
		currX = self.head
		while currX != None and currX.data != x:
			prevX = currX
			currX = currX.next

		# Search for y (keep track of prevY and currY)
		prevY = None
		currY = self.head
		while currY != None and currY.data != y:
			prevY = currY
			currY = currY.next

		# If either x or y is not present, nothing to do
		if currX == None or currY == None:
			return

		# If x is not head of linked list
		if prevX != None:
			prevX.next = currY
		else: # Else make y as new head
			self.head = currY

		# If y is not head of linked list
		if prevY != None:
			prevY.next = currX
		else: # Else make x as new head
			self.head = currX

		# Swap next pointers
		temp = currX.next
		currX.next = currY.next
		currY.next = temp

	# Function to sort the linked list using bubble sort
	def bubbleSort(self):
		count = 0
		start = self.head
		while start != None:
			count+= 1
			start = start.next

		# Traverse through all nodes of linked list
		for i in range(0, count):

			# Last i elements are already in place
			start = self.head
			while start != None:

				# Swap adjacent nodes
				ptr = start.next
				if ptr != None:
					if start.data > ptr.data:
						self.swapNodes(start.data, ptr.data)

				start = start.next
        
        
# THIS IS WHERE WE STOPPED IN CLASS LAST TIME        
        
	
	# Function to print the linked list
	def printList(self):
		tmp = self.head
		while tmp != None:
			print(tmp.data, end = " -> ")
			tmp = tmp.next
		print("None")


# Driver Code
if __name__ == '__main__':

	arr = [78, 20, 10, 32, 1, 5]

	# Create a linked list from array
	llist = LinkedList()
	llist.head = Node(arr[0])
	start = llist.head
	for i in range(1, len(arr)):
		start.next = Node(arr[i])
		start = start.next

	# Print the list before sorting
	print("Linked list before sorting")
	llist.printList()

	# Sort the list
	llist.bubbleSort()

	# Print the list after sorting
	print("Linked list after sorting")
	llist.printList()
  
  
  # END OF CODE
