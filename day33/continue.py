#continue:the continue statement is used to skip the current iteration of a loop and move to the next iteration.
#it does not stops the loop,it only skips that one iteration.
#when we use continue?
#when we dont want to execute some code for a particular condition but we still want the loop running
frnds = ["pavss", "gee", "keertzz"]
for x in frnds:
  if x == "gee":
    continue
  print(x)
  
#Example 2:
students=["A","B","Absent","C","D"]
for s in students:
    if s=="Absent":
        continue
    print(s)
