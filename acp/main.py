import math

def calculate_circumference(radius):
  """
  Calculates the circumference of a circle given its radius.

  Args:
    radius: The radius of the circle (a numerical value).

  Returns:
    The circumference of the circle.
  """
  circumference = 2 * math.pi * radius
  return circumference

# Get radius input from the user
try:
  user_radius = float(input("Enter the radius of the circle: "))
  
  # Calculate and print the circumference
  circle_circumference = calculate_circumference(user_radius)
  print(f"The circumference of the circle with radius {user_radius} is: {circle_circumference}")

except ValueError:
  print("Invalid input. Please enter a numerical value for the radius.")