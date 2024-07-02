# I suggest that you don't modify this file! It is used to test your code locally
# and any changes you make won't be used in the actual grading. This file:
#  1. loads some test inputs 
#  2. executes your code on those inputs
#  3. stores the result
import json, sys
from pathlib import Path
import factorial              # <--- Loading your function!
import vy_tests               # <---- Loads built-in helper function

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print(sys.argv,"requires two inputs: a path to the input file, a path to the output file")
    sys.exit(1)

  # Read an input json file containing problems
  data = json.loads(Path(sys.argv[1]).read_text())
  Path(sys.argv[2]).write_text(json.dumps(data,indent=2))

  # Run the problems
  for problem in data.get("problems",[]):
    if "inputs" in problem:
      n = problem["inputs"].get("n",-1.0)
      if 'outputs' in problem:
        vy_tests.grade_problem(problem["outputs"], "nfac", factorial.factorial(n))

  Path(sys.argv[2]).write_text(json.dumps(data,indent=2))
