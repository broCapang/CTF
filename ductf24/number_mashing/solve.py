from z3 import Int, Solver, And, Not, sat

# Define integer variables
x = Int('x')
y = Int('y')

# Create a solver instance
solver = Solver()

# Add constraints
solver.add(x != 0)               # x cannot be 0
solver.add(y != 0)               # y cannot be 0
solver.add(y != 1)               # y cannot be 1
solver.add(x / y == x)           # x / y should be equal to x

# Check satisfiability
if solver.check() == sat:
    model = solver.model()
    print(f"x = {model[x]}, y = {model[y]}")
else:
    print("No values of x and y found where x / y = x")








1 2 -1 -2

2 -1 -2



1 2
1 -1
1 -2

2 2
2 -1
2 -2

-1 2
-1 -1
-1 -2

-2 2
-2 -1
-2 -2

