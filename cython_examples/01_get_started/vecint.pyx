cdef extern from "vector_int.h":
  cdef cppclass VectorInt:
    VectorInt()
    void push_back(int)
    int get(int)
    int size()
    bint is_empty()

cdef class PyVectorInt:
  cdef VectorInt *vec

  def __init__(self):
    self.vec = new VectorInt()

  def __dealloc(self):
    del self.vec

  def push_back(self, val):
    self.vec.push_back(val)

  def get(self, idx):
    return self.vec.get(idx)

  def size(self):
    return self.vec.size()

  def is_empty(self):
    return self.vec.is_empty()