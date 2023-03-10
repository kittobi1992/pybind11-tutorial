# Copy the *.so file from the build folder to this folder to run the example

from vecint import PyVectorInt
from vecint import Access
import random

vec = PyVectorInt()

# String Representatation
for i in range(10):
  vec.push_back(random.randint(0,100))
print(vec)

# Properties
print(vec.length)
vec.name = "Vector of Integers"
print(vec.__dict__)

# Overloaded Methods
vec.clear()
vec.push_back(41)
vec.push_back(42, 3)
print(vec)

# Enum Types
print(vec.access)
vec.access = Access.READONLY
print(vec.access)

# Lambda Expression
vec.clear()
for i in range(10):
  vec.push_back(i)
print(vec)
l = []
vec.doForAllElements(lambda x : l.append(x * x) )
print(l)

# Operator Overloading
print(len(vec))
print(vec)
print(str(vec))
print(vec[1])
for elem in vec:
  print(elem, end=' ')
print("")