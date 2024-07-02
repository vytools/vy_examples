import json, sys, random
from pathlib import Path

def rval(low,high):
  return low + random.random()*(high-low)

if __name__ == '__main__':
  # Read an input json file containing problems
  data = json.loads(Path(sys.argv[1]).read_text())
  for ii in range(3):
    data["problems"].append({
      "name": "Random problem #"+str(ii+1),
      "outputs": {
        "c": {"points_possible":3,"tolerance":0.00001}
      },
      "inputs":{
        "a": rval(-10,10),
        "b": rval(-10,10),
      }
    })
  Path(sys.argv[2]).write_text(json.dumps(data,indent=2))
