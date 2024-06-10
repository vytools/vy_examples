// This is the test program your coded will be run against. If you modify it
// locally just remember your changes won't be included when the grading test is run.
#include <cctype>
#include "vy_tests.hpp"
#include "add.cpp"

// Test program
int main(int argc, char *argv[]) {
  if (argc != 3) {
    std::cout << argv[0] << " requires two inputs: a path to the input file, a path to the output file" << std::endl;
    return 1;
  }
  // Load tests from file
  nlohmann::json data = vy_tests::parse_json_file(argv[1]);
  vy_tests::write_json_file(argv[2], 1, data);

  // Run the problems
  for (auto &problem : data["problems"]) {
    double a = problem["inputs"].value("a",-1.0);
    double b = problem["inputs"].value("b",1.0);
    double c = add(a,b);
    if (problem.find("outputs") != problem.end()) {
      vy_tests::grade_problem(problem["outputs"], "c", c);
    }
  }

  // Build some plots
  vy_tests::write_json_file(argv[2], 1, data);
  return 0;
}
