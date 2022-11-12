# Run setup.py before and copy the *.so file from the build folder to this folder

from time import time
from vecint import PyVectorInt

vec = PyVectorInt()

start = time()
for i in range(1000000):
  vec.push_back(i)
end = time()

print("Running Time = " + str(end - start) + "s")
print("Vector Size = " + str(vec.size()))

