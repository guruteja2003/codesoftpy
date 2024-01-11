def simple_calculator():
  """Performs basic arithmetic operations based on user input."""

  while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
      result = num1 + num2
    elif operation == "-":
      result = num1 - num2
    elif operation == "*":
      result = num1 * num2
    elif operation == "/":
      try:
        result = num1 / num2
      except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        continue  # Go back to the start of the loop
    else:
      print("Invalid operation. Please try again.")
      continue

    print("Result:", result)

    # Ask if the user wants to perform another calculation
    another_calc = input("Do you want to perform another calculation? (yes/no): ")
    if another_calc.lower() != "yes":
      break

simple_calculator()
