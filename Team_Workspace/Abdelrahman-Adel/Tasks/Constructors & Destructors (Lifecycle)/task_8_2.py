from task_8_1 import Logger
print("Step 1")
def test_scope(): 
    log = Logger()
    print("Step 2 (Inside Function)")
test_scope()
print("Step 3 (Outside Function)")