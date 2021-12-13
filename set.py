colours={"red","green"}
print(colours)

#insert to set
colours.add("yellow")
print(colours)

#copy sets (shallow copy)
colour_bkp = colours.copy()
print(colour_bkp)

#clear sets
colours.clear()
print(colours)


x={"a","b","c","d","e"}
y={"b","c"}
z={"c","d"}
print(x.difference(y))
print(x.difference(y).difference(z))

#More set functions
#discard
#difference_update (also x=x-y)
#remove() like discard but will throw error if no value in set
#intersection will return common ones (also x&y)
#isdisjoint() will return True if no common

#issubset() will return True if b is subset of a
a={"a","b","c","d"}
b={"a","b"}
print(b.issubset(a))

#a | b union (elements in both sets but not duplicated)
#a ^ b symmetric_difference will return values which are in a and be except the common ones