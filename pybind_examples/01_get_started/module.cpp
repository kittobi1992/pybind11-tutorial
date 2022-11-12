#include <pybind11/pybind11.h>

#include "vector_int.h"

namespace py = pybind11;

PYBIND11_MODULE(vecint, m) {
  py::class_<VectorInt>(m, "PyVectorInt")
    .def(py::init<>())
    .def("push_back", &VectorInt::push_back)
    .def("get", &VectorInt::get)
    .def("size", &VectorInt::size)
    .def("is_empty", &VectorInt::is_empty);
}
