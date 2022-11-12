#pragma once

#include <vector>

class VectorInt {

 public:
  VectorInt();

  void push_back(const int val);
  int get(const size_t idx) const;
  size_t size() const;
  bool is_empty() const;

 private:
  std::vector<int> _vec;
};
