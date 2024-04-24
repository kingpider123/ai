from pulp import *

prob= LpProblem("hw3",LpMaximize)

x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)
z = LpVariable(name="z", lowBound=0)

prob += 3*x+2*y+5*z

prob += x+y <=10
prob += 2*x+z <=9
prob += y+2*z <=11

prob.solve()
#print(prob.solve())

for var in prob.variables():
    print(var, "=", value(var))
print("MAX = ", value(prob.objective))