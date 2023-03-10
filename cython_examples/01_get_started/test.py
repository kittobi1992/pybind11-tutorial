# Run setup.py before and copy the *.so file from the build folder to this folder to run the example

from vecint import PyVectorInt

vec = PyVectorInt()
print("Empty?="  + str(vec.is_empty()))

for i in range(10):
  vec.push_back(i)

for i in range(10):
  print("vec[" + str(i) + "]=" + str(vec.get(i)))

print("Size="  + str(vec.size()))
print("Empty?="  + str(vec.is_empty()))

