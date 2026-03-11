# control_flow.py - Ultra compact
def if_demo(x):
    return "positive" if x > 0 else "negative" if x < 0 else "zero"

def for_demo():
    return [f"num {i}" for i in range(1, 4)]

def while_demo():
    i, result = 3, []
    while i > 0:
        result.append(f"count {i}")
        i -= 1
    return result

def run():
    print([if_demo(x) for x in [-2, 0, 5]])
    print(for_demo())
    print(while_demo())

if __name__ == "__main__":
    run()