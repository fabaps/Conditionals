# Evaluar si es triangulo rectangulo
def esEquilatero(lado1, lado2, lado3):

  # Escriba aqui su(s) linea(s) de codigo
  # debe definir una variable llamada rectangulo
  # y asignarle la condicion para que un triangulo sea rectangulo
  # Ejemplo:
  #    rectangulo = lado3 > 1
  #
  # No debe modificar nada mas
  #---------------------------

	equilatero = (lado1 == lado2) and (lado1 == lado3)

  #---------------------------
  if equilatero:
     return True
  else:
     return False

# Evaluar si es triangulo rectangulo
def esIsoceles(lado1, lado2, lado3):

  # Escriba aqui su(s) linea(s) de codigo
  # debe definir una variable llamada rectangulo
  # y asignarle la condicion para que un triangulo sea rectangulo
  # Ejemplo:
  #    rectangulo = lado3 > 1
  #
  # No debe modificar nada mas
  #---------------------------

	isoceles = (lado1 == lado2) or (lado2 == lado3)
  
  #---------------------------
  if isoceles: 
     return True
  else:
     return False
# Evaluar si es triangulo rectangulo
def esRectangulo(lado1, lado2, lado3):

  # Escriba aqui su(s) linea(s) de codigo
  # debe definir una variable llamada rectangulo
  # y asignarle la condicion para que un triangulo sea rectangulo
  # Ejemplo:
  #    rectangulo = lado3 > 1
  #
  # No debe modificar nada mas
  #---------------------------

	rectangulo = pow(lado1,2)+ pow(lado2,2) == pow(lado3,2) or pow(lado2,2) + pow(lado3,2) == pow(lado1,2) or pow(lado1,2) + pow(lado3,2) == pow(lado2,2)
  
  #---------------------------
  if R
  rectangulo: 
     return True
  else:
     return False


