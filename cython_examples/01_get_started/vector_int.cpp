#include "vector_int.h"

VectorInt::VectorInt() :
  _vec() { }

void VectorInt::push_back(const int val) {
  _vec.push_back(val);
}

int VectorInt::get(const size_t idx) const {
  return _vec[idx];
}

size_t VectorInt::size() const {
  return _vec.size();
}

bool VectorInt::is_empty() const {
  return _vec.empty();
}