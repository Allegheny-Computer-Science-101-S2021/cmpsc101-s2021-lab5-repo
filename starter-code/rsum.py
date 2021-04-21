import random
def generate(ls,size):
	'''
        Data is prepared by inserting random values 
        between 1 and 100. Data items may be assumed to 
        be repeated. 
        Please refer to lab spec for the problem definiton.
    '''
	maximum = 100; 
	for i in range(0,size):
		ls.insert(i,random.randint(1,maximum))


def sum(ls,n):
	res = 0
	# add your logic here 
	return res
ls = []
size = int(input("Enter the no of items:")) # number of items provided by the user
generate(ls,size)
print(ls)
print(f"sum:{sum(ls,len(ls))}")
