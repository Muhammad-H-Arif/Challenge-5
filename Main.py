def josephus_problem(n, k, s):
  """
  Solves the Josephus problem for a given number of people (n), elimination interval (k), and starting index (s).

  Args:
    n: The number of people in the circle.
    k: The elimination interval.
    s: The starting index (where the elimination begins).

  Returns:
    The position of the last person remaining (index starting from s).
  """
  people = list(range(1, n + 1))  # Create a list representing people
  index = (s - 1) % n  # Adjust starting index

  while len(people) > 1:
    index = (index + k - 1) % len(people)  # Calculate the index of the person to eliminate
    people.pop(index)  # Remove the person at the calculated index

  return people[0]  # Return the position of the last remaining person (adjusted for starting index)

# Get user input for n, k, and s
n = int(input("Enter the number of people (N): "))
k = int(input("Enter the elimination interval (K): "))
s = int(input("Enter the starting index (S): "))

# Handle invalid input
if n <= 0 or k <= 0 or s <= 0:
  print("Invalid input. N, K, and S must be positive integers.")
else:
  # Calculate and print the result
  result = josephus_problem(n, k, s)
  print("The last person remaining is at position:", result)
