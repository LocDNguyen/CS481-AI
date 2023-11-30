from heapq import *
from math import sqrt
import random



def generate_maze(rows, cols, wall_prob):
    maze = [[0] * cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0 or row == rows - 1 or col == cols - 1 or random.random() < wall_prob:
                maze[row][col] = 1  # 1 represents a wall
    maze[4][1] = 0
    #maze[rows-2][cols-2] = 0
    maze[4][6] = 0
    return maze

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))

def heuristic(current, goal):
    # Manhattan distance heuristic
    if current is None: 
        return 0 
    else:
        #return abs(current[0] - goal[0]) + abs(current[1] - goal[1])
        return sqrt((current[0] - goal[0])**2 + (current[1] - goal[1])**2)

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from and came_from[current] is not None:
        current = came_from[current]
        path.insert(0, current)
    return path

def get_neighbors(node, rows, cols):
    neighbors = [(node[0] + 1, node[1]), (node[0] - 1, node[1]), (node[0], node[1] + 1), (node[0], node[1] - 1)]
    return [(r, c) for r, c in neighbors if 0 <= r < rows and 0 <= c < cols]

#only removes 1 duplicate
def remove_duplicates_from_open_set(open_set):
    first = []
    for i in range(len(open_set)):
        if open_set[i][1] not in first:
            first.append(open_set[i][1])
        else:
            open_set.pop(i)
            break
    heapify(open_set)
    return open_set

def update_cost(open_set, node, cost):
    for n in open_set:  #doesnt work
        if n[1] == node:
            n[0] = cost
    heapify(open_set)   #the ordering may have changed
    #remove duplicates
    return remove_duplicates_from_open_set(open_set)

def astar_pathfind_gen(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heappush(open_set, (heuristic(start, goal), start))     #remove duplicates
    came_from = {start: None}
    explored = {}
    goal_found = False
    actual_cost = 0
    while open_set and not goal_found:
        current_cost, current_node = heappop(open_set)
        actual_cost = len(reconstruct_path(came_from, current_node))    #actual cost is length of path-1 (since start does not move)
        print(str(actual_cost-1) + " cost for " + str(current_node))    #print for debugging
        explored[current_node] = actual_cost
        
        yield current_node

        #end condition
        if current_node == goal:
            goal_found = True
            print("Goal found!")
            
        for neighbor in get_neighbors(current_node, rows, cols):
            if maze[neighbor[0]][neighbor[1]] != 1 and neighbor not in explored.keys():
                if neighbor not in open_set:    #only covers case where cost is same. Otherwise, it will been seen as unique, which is why the duplicate needs to be removed
                    heappush(open_set, (actual_cost+heuristic(neighbor, goal), neighbor))
                    remove_duplicates_from_open_set(open_set)
                    came_from[neighbor] = current_node
                elif open_set[neighbor] > actual_cost + heuristic(neighbor, goal):
                    open_set = update_cost(open_set, neighbor, actual_cost+heuristic(neighbor, goal))
                    came_from[neighbor] = current_node
        
        #debugging
        print("explored:", end=" ")
        print(explored.keys())
        print("frontier:", end=" ")
        print(open_set)
            

    return None  # No path found



maze_dim_x = 12
maze_dim_y = 12
wall_prob = 0.2

maze = generate_maze(maze_dim_x, maze_dim_y, wall_prob)
print("Initial maze: ")
print_maze(maze)

#create generator
start_cord = (4,1)
end_cord = (4,6)
astar_pgen = astar_pathfind_gen(maze, start_cord, end_cord)
#path taken by A*
astar_path = []
for node in astar_pgen:
    #print(node, end=", ")
    astar_path.append(node)
print()

#iterare through path, display path with letter (starting at 'A')
for i in range(len(astar_path)):
    x='A'
    val=chr(ord(x) + i)
    maze[astar_path[i][0]][astar_path[i][1]] = val

print("A is the start position, " + chr(ord('A') + len(astar_path) - 1) + " is the goal position")
print_maze(maze)