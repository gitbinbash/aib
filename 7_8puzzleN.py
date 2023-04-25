from collections import deque

# number of elements
n = int(input("Enter numbers of row or column : "))
initial_state = []
i = 1
while i<=n:
    # number of elements
    n1 = n
    # Below line read inputs from user using map() function
    a = list(map(int,input("\nEnter the numbers in the row : ").strip().split()))[:n1]
    initial_state.append(a)
    i= i+1

print("\ninitial state -->",initial_state)

# number of elements
goal_state = []
i = 1
while i<=n:
    # number of elements
    n1 = n
    # Below line read inputs from user using map() function
    a = list(map(int,input("\nEnter the numbers in the row : ").strip().split()))[:n1]
    goal_state.append(a)
    i= i+1

print("\ngoal_state -->", goal_state)


# Define the actions that can be taken
actions = ['up', 'down', 'left', 'right']

# Define a function to get the possible successor states
def get_successors(state):
    successors = []
    row, col = get_blank_location(state)
    for action in actions:
        new_state = perform_action(state, action, row, col)
        if new_state:
            successors.append(new_state)
    return successors

# Define a function to get the location of the blank tile
def get_blank_location(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

# Define a function to perform an action on the state
def perform_action(state, action, row, col):
    if action == 'up':
        if row == 0:
            return None
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row-1][col] = new_state[row-1][col], new_state[row][col]
        return new_state
    elif action == 'down':
        if row == 2:
            return None
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row+1][col] = new_state[row+1][col], new_state[row][col]
        return new_state
    elif action == 'left':
        if col == 0:
            return None
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row][col-1] = new_state[row][col-1], new_state[row][col]
        return new_state
    elif action == 'right':
        if col == 2:
            return None
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row][col+1] = new_state[row][col+1], new_state[row][col]
        return new_state

# Define a function to check if the current state is the goal state
def is_goal(state):
    return state == goal_state

# Define the breadth-first search algorithm
def bfs_search(initial_state):
    frontier = deque([initial_state])
    explored = set()
    while frontier:
        state = frontier.popleft()
        if is_goal(state):
            return state
        explored.add(str(state))
        for successor in get_successors(state):
            if str(successor) not in explored:
                frontier.append(successor)
    return None

# Call the breadth-first search function and print the solution
solution = bfs_search(initial_state)
if solution:
    print('\nSolution:', solution)
else:
    print('\nNo solution found.')
