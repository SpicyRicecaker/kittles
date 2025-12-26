import subprocess
import os
import json
from kittens.tui.handler import result_handler

def environ_json(e):
    dummy = {}

    for (k, v) in e.items():
        dummy[k] = v
    return json.dumps(dummy)

def main(args):
    # o = subprocess.run([f"{os.environ["HOME"]}/.cargo/bin/kittles", "--adjacent"], capture_output=True)
    # print(o)
    # print("hi")
    # o = subprocess.run(["kitty", "@", "launch"])

    # o = subprocess.run(["kittles"])
    # print(os.environ)
    # o = subprocess.run([f"{os.environ["HOME"]}/.cargo/bin/kittles"], capture_output=True)
    # print(o)
    # input()
    # print(os.environ)
    # input()
    # subprocess.run(["kitty", "@", "launch"])
    # pass
    # return {'a': '3', 'b': '9'}
    
    return environ_json(os.environ)

@result_handler(no_ui=False)
def handle_result(args, new_environ, target_window_id, boss):
    with open(f"{os.environ["HOME"]}/git/kittles/src/bin/e0.txt", "w") as f:
        f.write(environ_json(os.environ))
        f.close()

    with open(f"{os.environ["HOME"]}/git/kittles/src/bin/e1.txt", "w") as f:
        f.write(new_environ)
        f.close()

    # new_environ = json.loads(new_environ)
    # # o = subprocess.run([f"{os.environ["HOME"]}/.cargo/bin/kittles", "--adjacent"], capture_output=True)
    # # print(o)
    #
    # # input: d1, d2
    # # output:
    # # key       old     new
    # # HOME      ---     99
    # # D         999     ---
    # # DF        123     456
    # # assume each k, v only appear once
    #
    # diff = {}
    # t = json.loads(json.dumps(new_environ))
    #
    # # diff environ
    # for (k, v) in os.environ.items():
    #     match diff[k], diff[v])
    #
    #
    #
    # with open(f"{os.environ["HOME"]}/git/kittles/src/bin/mytxt123.txt", "w") as f:
    #     for i in range(3):
    #         f.write("\n")
    #     for (k, v) in environ.items():
    #         os.environ[k] = v
    #         f.write(f"{k}:{v}\n")
    #     f.close()
    #
    # os.reload_environ()
    # # Popen(["kitty", "@", "launch"])
    #
    # # o = subprocess.run(["ttt"])
    #
    # with open(f"/Users/oliver/git/kittles/src/bin/mytxt123.txt", "w") as f:
    #     f.write("=================== section after reload =================")
    #     # f.write(str(o))
    #     # f.write(os.environ["HOME"])
    #     # f.write('\n')
    #     # f.write("hi9999999999999999999")
    #     f.close()
    #
    # # print('sub')
