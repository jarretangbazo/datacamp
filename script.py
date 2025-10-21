# Python as a calculator
#print(5 / 8)
#print(4 + 5)
#print(10 / 2)
#print(5 - 5)
#print(3 * 5)

# Variable assignment
## BMI
height = 1.79
weight = 68.7
#print(height)
#print(weight)

## Calculate BMI
bmi = weight / height ** 2
#print(bmi)

# Calulations with variables
## Savings
monthly_savings = 10
num_months = 4
new_savings = monthly_savings * num_months
#print(new_savings)

# Variable types
## See variable types with 'type' function
x = "body mass index"
y = 'this works too'
a = True
b = False
m = 10
n = 11.5

#print(type(bmi))
#print(type(x))
#print(type(y))
#print(type(a))
#print(type(b))
#print(type(m))
#print(type(n))
#print(type(5/8))
#print(type(4+5))

# Python list
## Can contain one type or multiple types
heights = [1.73, 1.68, 1.71, 1.89]  # floats only
fam_heights = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89] # strings and floats

## We can create lists within a list
fam_heights2 = [["liz", 1.73], ["emma", 1.68], ["mom", 1.71], ["dad", 1.89]] # list of lists

#print(heights)
#print(type(heights))
#print(fam_heights)
#print(type(fam_heights))
#print(fam_heights2)
#print(type(fam_heights2))

# Functions


# NumPy
import numpy as np

## Create NumPy arrays from lists
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# NumPy allows for vectorized operations
np_height = np.array(height)
np_weight = np.array(weight)

#print(np_height)
#print(np_weight)
#print(type(np_height))
#print(type(np_weight))  

bmi = np_weight / np_height ** 2
#print(bmi)

# Doing calculations with lists does't work as expected. We are
# only able to do operations when we convert the list to NumPy arrays

# we can also subset numpy arrays using booleans. Say, for example, we want to output all
# bmi values greater than 23
#print(bmi > 23)
#print(bmi[bmi > 23])

# Basic data analysis with NumPy

# Basic plots with matplotlib
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

# Add more data
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

# Create a line plot
#plt.plot(year, pop)

#plt.xlabel("Year")
#plt.ylabel("Population (billions)")
#plt.title("World Population Over Time")
#plt.yticks([0, 2, 4, 6, 8, 10], 
#           ["0", "2B", "4B", "6B", "8B", "10B"])
#plt.show()



# Create a scatter plot
#plt.scatter(year,pop)
#plt.show()

# Create a histogram
values = np.random.randn(10)*5
#print(values)

#plt.hist(values, bins=3)
#plt.show()

# Dictionary to DataFrame with Pandas
import pandas as pd

# Create lists
names = ["United States", "Australia", "Japan", "India", "Russia", "Morocco", "Egypt"]
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary
my_dict = {
    'country': names,
    'drives_right': dr,
    'cars_per_cap': cpc
}

cc# Create DataFrame
cars = pd.DataFrame(my_dict)
print(cars)