import random 
marco = random.randint(50,150)
jose = random.randint(50,150)
print("Numero de Marco: ", marco)
print("Numero de Jose: ", jose)
if marco == jose:
  print("EMPATADOS!")
elif marco > jose:
  print("Marco escoge")
else:
  print("Jose escoge")