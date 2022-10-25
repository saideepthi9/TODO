class Node:
	def __init__(self):	
		self.data = 0
		self.next = None
		self.prev = None
		
# Function to find number of connected
# components using a  linked list
# and a reference array
def func_connComp(head_ref, refArr, n):
	
	# Base case when the doubly
	# linked list is empty
	if (head_ref == None):
		return 0;

	# Initialise connectedComponents to zero
	connectedComponents = 0;

	# Initialise an unordered set
	refSet = set()

	# Push the first element of the
	# refArr in the refSet and
	# set the connectedComponents to 1
	refSet.add(refArr[0]);
	connectedComponents += 1

	# Loop over all the elements of the refArr
	for i in range(1, n):

		# add each reference node to the refSet
		refSet.add(refArr[i]);

		# If the reference node is the head of the linked list
		if (refArr[i].prev == None):

			# when next sibling of the head node is
			# not in the refSet
			if (refArr[i].next not in refSet):
				connectedComponents += 1

		# If the reference node is the
		# last node of the linked list'''
		elif (refArr[i].next == None):

			# when previous sibling of the
			# node is not in the refSet
			if (refArr[i].next not in refSet):
				connectedComponents += 1
			
		# the case when both previous and
		# next siblings of the current node
		# are in the refSet
		elif (refArr[i].prev in refSet
			and refArr[i].next in refSet):
			connectedComponents -= 1
			
		# the case when previous and next
		# siblings of the current node
		# are not in the refSet'''
		elif (refArr[i].prev not in refSet
			and refArr[i].next not in refSet):
			connectedComponents += 1
		
	return connectedComponents;

# Function to add a node at the
# beginning of the  Linked List
def push(head_ref, new_data):

	''' allocate node '''
	new_node = Node()
	current_node = new_node;
	
	''' put in the data '''
	new_node.data = new_data;

	''' since we are adding at the beginning,
	prev is always None '''
	new_node.prev = None;

	''' link the old list off the new node '''
	new_node.next = (head_ref);

	''' change prev of head node to new node '''
	if ((head_ref) != None):
		(head_ref).prev = new_node;

	''' move the head to point to the new node '''
	(head_ref) = new_node;
	return current_node, head_ref;

# Function to print nodes in a given
#  linked list
def printList(node):
	while (node != None):
		print(node.data, end = ' ');
		node = node.next;
		
# Driver code
if __name__=='__main__':

	# Start with the empty list
	head = None;

	# Let us create a linked list to test
	# the functions so as to find number
	# of Connected Components Created a
	#  linked list: 1 <. 7 <. 10 <. 5 <. 4 <. 2
	ref_to_nodeN2, head = push(head, 2);
	ref_to_nodeN4, head = push(head, 4)
	ref_to_nodeN5, head = push(head, 5)
	ref_to_nodeN10, head = push(head, 10)
	ref_to_nodeN7, head = push(head, 7)
	ref_to_nodeN1, head = push(head, 1)
	refArr = [ref_to_nodeN5, ref_to_nodeN2, ref_to_nodeN7, ref_to_nodeN1]

	# This function will return the number
	# of connected components of  linked list
	connectedComponents = func_connComp(head, refArr, 4);
	print("Total number of connected components are ", connectedComponents)

