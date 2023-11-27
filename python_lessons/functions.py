"""Write a function that estimates the value of a house.

Create a function get_expected_cost that takes as input three variables:

beds - number of bedrooms (data type float)
baths - number of bathrooms (data type float)
has_basement - whether or not the house has a basement (data type boolean)

It should return the expected cost of a house with those characteristics.

Assume that:
the expected cost for a house with 0 bedrooms and 0 bathrooms, and no basement is 80000,
each bedroom adds 30000 to the expected cost,
each bathroom adds 10000 to the expected cost, and
a basement adds 40000 to the expected cost.

For instance,
a house with 1 bedroom, 1 bathroom, and no basement has an expected cost of 80000 + 30000 + 10000 = 120000. 
This value will be calculated with get_expected_cost(1, 1, False).

a house with 2 bedrooms, 1 bathroom, and a basement has an expected cost of 80000 + 2*30000 + 10000 + 40000 = 190000. 
This value will be calculated with get_expected_cost(2, 1, True)"""

###Solution
def get_expected_cost(beds = 0.0, baths = 0.0, has_basement = False):
    cost = 80000
    if beds > 0:
        cost += beds * 30000
    if baths > 0:
        cost += baths * 10000
    if has_basement:
        cost += 40000
    return cost

print("The expected cost of the house will be:", (get_expected_cost(0,0,False)))
print("The expected cost of the house will be:",(get_expected_cost(1,1, False)))
print("The expected cost of the house will be:",(get_expected_cost(2,1,True)))


