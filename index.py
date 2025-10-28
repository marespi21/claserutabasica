#nombre = "Camila"
#edad = "29"
nombre = input ("pon tu nombre")
edad = int (input('pon tu edad'))

if edad >= 18:
     print("Eres mayor de edad")
elif edad < 18:
 print("Eres menor de edad")

print(f"tu nombre es:{nombre} y tienes {edad}")

