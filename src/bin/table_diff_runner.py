import os
from table_diff import get_diff, print_diff
import json
# import json

# dummy = {}
#
# for (k, v) in os.environ.items():
#     dummy[k] = v
# sdummy = json.dumps(dummy)
#
# print(json.loads(sdummy))
#

# with open(f"{os.environ["HOME"]}/git/kittles/src/bin/mytxt123.txt", "w") as f:
#     f.write("xd")
#     f.close()

d1 = {}
d2 = {}

with open("e0.txt", "r") as f:
    d1 = json.loads(f.read())
    f.close()

with open("e1.txt", "r") as f:
    d2 = json.loads(f.read())
    f.close()

diff = get_diff(d1, d2)
print_diff(diff)
