import json 

# input: d1, d2
# output:
# key       old     new
# HOME      ---     99
# D         999     ---
# DF        123     456
# assume each k, v only appear once

def print_diff(d):
    print(d)
    print("\t\t\t".join(["key", "old", "new"]))
    print("\t\t\t".join(["---", "---", "---",]))
    for (k, v) in d.items():
        p = list(map(lambda x : '---' if not x else str(x), [k, v['old'], v['new']]))
        print("\t\t\t".join(p))

def get_diff(d1, d2):
    # unprocessed
    up = json.loads(json.dumps(d1))
    diff = { }

    # diff environ
    for (k, v) in d2.items():
        # print("aaaaaaaaaaaaaaaa", k, v)
        match (d1.get(k), v):
            # assume we don't need guards here
            case (None, _):
                # print("branch 1")
                tt = {}
                tt['old'] = None
                tt['new'] = v
                diff[k] = tt
            case (a, b):
                # print("branch 2")
                if a != b:
                    tt = {}
                    tt['old'] = a
                    tt['new'] = b
                    # print(tt)
                    diff[k] = tt
                del up[k]

    for (k, v) in up.items():
        tt = {}
        tt['old'] = v
        tt['new'] = None
        diff[k] = tt

    return diff

def json_eq(d1, d2):
    return json.dumps(get_diff(d1, d2)) == "{}"

def test1():
    input = {
        'd1': {
            'D': 999,
            'DF': 123
        },
        'd2': {
            'HOME': 99,
            'DF': 456
        }
    }
    r = get_diff(input['d1'], input['d2'])
    re = {'HOME': {'old': None, 'new': 99}, 'DF': {'old': 123, 'new': 456}, 'D': {'old': 999, 'new': None}}
    assert json_eq(r, re)

def test2():
    input = {
        'd1': {
            'D': 999,
            'DF': 123
        },
        'd2': {
            'HOME': 99,
            'DF': 456
        }
    }
    r = get_diff(input['d1'], input['d2'])
    print_diff(r)


# test_cases = [
#     test1,
#     test2
# ]
#
# for test_case in test_cases:
#     test_case()
#
