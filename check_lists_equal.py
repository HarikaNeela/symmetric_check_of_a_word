Using list.sort() and == operator
The list.sort() method sorts the two lists and the == operator compares the two lists item by item which means they have equal data items at equal positions. This checks if the list contains equal data item values but it does not take into account the order of elements in the list. This means that the list [1,2,3] will be equal to the list [2,1,3] according to this method of comparison.

Example
 Live Demo

def compareList(l1,l2):
   l1.sort()
   l2.sort()
   if(l1==l2):
      return "Equal"
   else:
      return "Non equal"
l1=[1,2,3]
l2=[2,1,3]
print("First comparison",compareList(l1,l2))
l3=[1,2,3]
l4=[1,2,4]
print("Second comparison",compareList(l3,l4))
Output
First comparison Equal
Second comparison Non equal
