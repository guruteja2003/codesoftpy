import random

# Define character sets for password generation
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{};':\"\\|,.<>/?"

def generate_password(length):
  """Generates a random password of the specified length."""

  # Combine all character sets for a wider range of characters
  all_chars = letters + numbers + symbols

  # Create an empty password string
  password = ""

  # Generate random characters and append them to the password
  for i in range(length):
    password += random.choice(all_chars)

  # Shuffle the password for extra randomness
  random.shuffle(password)

  return password

# Get user input for desired password length
while True:
  try:
    password_length = int(input("Enter the desired password length: "))
    if password_length >= 8:
      break
    else:
      print("Password length must be at least 8.")
  except ValueError:
    print("Invalid input. Please enter a number.")

# Generate the password
password = generate_password(password_length)

# Print the generated password
print("Generated password:", password)
