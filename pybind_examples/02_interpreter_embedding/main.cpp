#include <iostream>
#include <string>
#include <vector>

#include <pybind11/embed.h>

namespace py = pybind11;

int main() {
  py::scoped_interpreter guard{}; // start the interpreter and keep it alive

  // Run Python code in C++
  py::exec("print('Hello World')");

  // Import python module and list content of current directory
  py::module os = py::module::import("os");
  py::object result = os.attr("listdir")(".");
  for ( auto& res : result ) {
    std::cout << res.cast<std::string>() << std::endl;
  }
}
