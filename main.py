num1 = input("Введите первое число >> ")
num2 = input("Введите второе число >> ")

if num1.isdigit() and num2.isdigit():
  result = int(num1) + int(num2)
  print("Результат: " + str(result))
else:
  print("Ошибка. Введите числа.")
  input("")