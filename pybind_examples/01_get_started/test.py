# Run setup.py before and copy the *.so file from the build folder to this folder

from vecint import PyVectorInt

vec = PyVectorInt()
print("Vector Empty? = " + str(vec.is_empty()))
for i in range(10):
  vec.push_back(i)
  print("Element on position " + str(i) + " is " + str(vec.get(i)))

print("Vector Size   = " + str(vec.size()))
print("Vector Empty? = " + str(vec.is_empty()))