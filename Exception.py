
try:
    sum.xyz
except AttributeError:
    print("not defined")
finally:
    print("Fertig!")
    
    
r20 = range(20)

print(r20[5:15])