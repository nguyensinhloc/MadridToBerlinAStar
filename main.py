# A* algorithm for finding a path from a vertex to a vertex in a graph
# Input: number of vertices, start vertex, end vertex, cost matrix
# Output: path from start to end and cost of the path

# Define a function to calculate the heuristic value of a vertex
def heuristic(vertex, end):
  # For simplicity, use the absolute difference between the vertex and the end as the heuristic
  return abs(vertex - end)

# Define a function to find the lowest cost vertex in the frontier
def lowest_cost(frontier):
  # Initialize the lowest cost and the lowest cost vertex
  lowest_cost = float("inf")
  lowest_cost_vertex = None
  # Loop through the frontier
  for vertex, cost in frontier.items():
    # If the cost is lower than the lowest cost, update the lowest cost and the lowest cost vertex
    if cost < lowest_cost:
      lowest_cost = cost
      lowest_cost_vertex = vertex
  # Return the lowest cost vertex
  return lowest_cost_vertex

# Ask the user to enter the number of vertices
n = int(input("Enter the number of vertices: "))

# Ask the user to enter the start vertex
start = int(input("Enter the start vertex: "))

# Ask the user to enter the end vertex
end = int(input("Enter the end vertex: "))

# Ask the user to enter the cost matrix
cost_matrix = []
print("Enter the cost matrix row by row:")
for i in range(n):
  # Split each row by space and convert to integers
  row = list(map(int, input().split()))
  # Append the row to the cost matrix
  cost_matrix.append(row)

# Initialize an empty dictionary to store the explored vertices and their costs
explored = {}

# Initialize an empty dictionary to store the frontier vertices and their costs
frontier = {}

# Initialize an empty dictionary to store the predecessors of each vertex
predecessors = {}

# Add the start vertex to the frontier with zero cost
frontier[start] = 0

# Initialize a boolean variable to indicate if a path is found or not
path_found = False

# Loop until the frontier is empty or a path is found
while frontier and not path_found:
  # Find the lowest cost vertex in the frontier
  current = lowest_cost(frontier)
  # Remove it from the frontier and add it to the explored vertices
  current_cost = frontier.pop(current)
  explored[current] = current_cost
  # Check if it is the end vertex
  if current == end:
    # Set path_found to True and break out of the loop
    path_found = True
    break
  # Loop through its neighbors in the graph
  for neighbor in range(n):
    # Check if there is an edge between them and if it is not explored already
    if cost_matrix[current][neighbor] > 0 and neighbor not in explored:
      # Calculate the new cost by adding the edge cost and the heuristic value of the neighbor
      new_cost = current_cost + cost_matrix[current][neighbor] + heuristic(neighbor, end)
      # Check if it is already in the frontier or if it has a lower cost than before
      if neighbor not in frontier or new_cost < frontier[neighbor]:
        # Update its cost in the frontier and its predecessor in the predecessors dictionary
        frontier[neighbor] = new_cost
        predecessors[neighbor] = current

# Check if a path was found or not
if path_found:
  # Initialize an empty list to store the path from start to end
  path = []
  # Start from the end vertex and trace back its predecessors until reaching the start vertex
  current = end
  while current != start:
    # Prepend it to the path list
    path.insert(0, current)
    # Move to its predecessor
    current = predecessors[current]
  # Prepend the start vertex to the path list
  path.insert(0, start)
  # Print the path and its cost
  print("Path from", start, "to", end, ":", path)
  print("Cost of the path:", explored[end])
else:
  # Print that no path was found
  print("No path from", start, "to", end)
