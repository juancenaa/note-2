x = 10
print("Initial value of global variable:", x)

def my_function():
    global x 
    y = 5   
    print("Local variable:", y)
    x = 20  

my_function()

print("Final value of global variable:", x)
