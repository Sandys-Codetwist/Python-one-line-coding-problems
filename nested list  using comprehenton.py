def nested_list(x):
	l1=[l2[2] for l2 in x]
	print(l1)
nested_list([[2,3,4,5],[5,6,8,9],[9,8,7,6]])	