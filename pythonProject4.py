import sys
sys.setrecursionlimit(15000)
sys.argv[1] = open("maze.txt", "r")
sys.argv[2] = open("maze_health.txt", "r")
health_time = int(sys.argv[3])
sys.argv[4] = open("output.txt", "w")
maze = []
for line in sys.argv[1]:
    line = line.strip("\n")
    line = list(line)
    maze.append(line)
for line in maze:
    if 'S' in line:
        a = maze.index(line)    # a o anki konumun  satır numarası
        b = line.index('S')     # b o anki konumun sütun numarası
def maze_solver(a, b, health_time):
    if a == 0:                       # ilk satırdaysak kontrol edilecekler
        if b == 0:                   # ilk satırın başı
            if maze[a][1] == "F" or maze[1][b] == "F":
                health_time -= 1
                return maze
            if maze[a][1] == "H":
                health_time = int(sys.argv[3])
                maze[a][1] = "1"
                return maze_solver(a, 1, health_time - 1)
            if maze[a][1] == "P":
                maze[a][1] = "1"
                return maze_solver(0, 1, health_time - 1)
            if maze[1][b] == "H":
                health_time = int(sys.argv[3])
                maze[1][b] = "1"
                return maze_solver(1, b, health_time - 1)
            if maze[1][b] == "P":
                maze[1][b] = "1"
                return maze_solver(1, b, health_time - 1)
        elif b == len(maze[a]) - 1:           # ilk satırın sonu
            if maze[0][b - 1] == "F" or maze[1][b] == "F":
                health_time -= 1
                return maze
            if maze[0][b - 1] == "H":
                health_time = int(sys.argv[3])
                maze[0][b - 1] = "1"
                return maze_solver(0, b - 1, health_time - 1)
            if maze[0][b - 1] == "P":
                maze[0][b - 1] = "1"
                return maze_solver(0, b - 1, health_time - 1)
            if maze[1][b] == "H":
                health_time = int(sys.argv[3])
                maze[1][b] = "1"
                return maze_solver(1, b, health_time - 1)
            if maze[1][b] == "P":
                maze[1][b] = "1"
                return maze_solver(1, b, health_time - 1)
        else:                               # ilk satırda arada bir yerde ise
            if maze[a][b - 1] == "F" or maze[a][b + 1] == "F" or maze[a + 1][b] == "F":
                health_time -= 1
                return maze
            if maze[a][b - 1] == "H":
                health_time = int(sys.argv[3])
                maze[a][b - 1] = "1"
                return maze_solver(a, b - 1, health_time - 1)
            if maze[a][b - 1] == "P":
                maze[a][b - 1] = "1"
                return maze_solver(a, b - 1, health_time - 1)
            if maze[a][b + 1] == "H":
                health_time = int(sys.argv[3])
                maze[a][b + 1] = "1"
                return maze_solver(a, b + 1, health_time - 1)
            if maze[a][b + 1] == "P":
                maze[a][b + 1] = "1"
                return maze_solver(a, b + 1, health_time - 1)
            if maze[a + 1][b] == "H":
                health_time = int(sys.argv[3])
                maze[a + 1][b] = "1"
                return maze_solver(a + 1, b, health_time - 1)
            if maze[a + 1][b] == "P":
                maze[a + 1][b] = "1"
                return maze_solver(a + 1, b, health_time - 1)
    elif a == len(maze) - 1:           # son satırdaysak kontrol edilecekler
        if b == 0:                     # alt sol köşe
            if maze[a][1] == "F" or maze[a - 1][0] == "F":
                health_time -= 1
                return maze
            if maze[a][1] == "H":
                health_time = int(sys.argv[3])
                maze[a][1] = "1"
                return maze_solver(a, 1, health_time - 1)
            if maze[a][1] == "P":
                maze[a][1] = "1"
                return maze_solver(a, 1, health_time - 1)
            if maze[a - 1][0] == "H":
                health_time = int(sys.argv[3])
                maze[a - 1][0] = "1"
                return maze_solver(a - 1, 0, health_time - 1)
            if maze[a - 1][0] == "P":
                maze[a - 1][0] = "1"
                return maze_solver(a - 1, 0, health_time - 1)
        elif b == len(maze[a]) - 1:    # alt sağ köşe
            if maze[a][b - 1] or maze[a - 1][b] == "F":
                health_time -= 1
                return maze
            if maze[a][b - 1] == "H":
                health_time = int(sys.argv[3])
                maze[a][b - 1] = "1"
                return maze_solver(a, b - 1, health_time - 1)
            if maze[a][b - 1] == "P":
                maze[a][b - 1] = "1"
                return maze_solver(a, b - 1, health_time - 1)
            if maze[a - 1][b] == "H":
                health_time = int(sys.argv[3])
                maze[a - 1][b] = "1"
                return maze_solver(a - 1, b, health_time - 1)
            if maze[a - 1][b] == "P":
                maze[a - 1][b] = "1"
                return maze_solver(a - 1, b, health_time - 1)
        else:                          # alt satırda bir yerde ise
            if maze[a][b + 1] == "F" or maze[a][b - 1] == "F" or maze[a - 1][b] == "F":
                health_time -= 1
                return maze
            if maze[a][b + 1] == "H":
                health_time = int(sys.argv[3])
                maze[a][b + 1] = "1"
                return maze_solver(a, b + 1, health_time - 1)
            if maze[a][b + 1] == "P":
                maze[a][b + 1] = "1"
                return maze_solver(a, b + 1, health_time - 1)
            if maze[a][b - 1] == "H":
                health_time = int(sys.argv[3])
                maze[a][b - 1] = "1"
                return maze_solver(a, b - 1, health_time - 1)
            if maze[a][b - 1] == "P":
                maze[a][b - 1] = "1"
                return maze_solver(a, b - 1, health_time - 1)
            if maze[a - 1][b] == "H":
                health_time = int(sys.argv[3])
                maze[a - 1][b] = "1"
                return maze_solver(a - 1, b, health_time - 1)
            if maze[a - 1][b] == "P":
                maze[a - 1][b] = "1"
                return maze_solver(a - 1,b, health_time - 1)
    elif b == 0 and a != 0 and a != (len(maze) - 1):                       # ilk sütundaysak kontrol edilecekler
        if maze[a][b + 1] == "F" or maze[a - 1][b] == "F" or maze[a + 1][b] == "F":
            health_time -= 1
            return maze
        if maze[a][b + 1] == "H":
            health_time = int(sys.argv[3])
            maze[a][b + 1] = "1"
            return maze_solver(a, b + 1, health_time - 1)
        if maze[a][b + 1] == "P":
            maze[a][b + 1] = "1"
            return maze_solver(a, b + 1, health_time - 1)
        if maze[a - 1][b] == "H":
            health_time = int(sys.argv[3])
            maze[a - 1][b] = "1"
            return maze_solver(a - 1, b, health_time - 1)
        if maze[a - 1][b] == "P":
            maze[a - 1][b] = "1"
            return maze_solver(a - 1, b, health_time - 1)
        if maze[a + 1][b] == "H":
            health_time = int(sys.argv[3])
            maze[a + 1][b] = "1"
            return maze_solver(a + 1, b, health_time - 1)
        if maze[a + 1][b] == "P":
            maze[a + 1][b] = "1"
            return maze_solver(a + 1, b, health_time - 1)
    elif b == (len(maze[0]) - 1) and a != 0 and a != len(maze) - 1:        # en sağdaki sütundaysak kontrol edilecekler
        if maze[a][b - 1] == "F" or maze[a - 1][b] == "F" or maze[a + 1][b] == "F":
            health_time -= 1
            return maze
        if maze[a][b - 1] == "H":
            health_time = int(sys.argv[3])
            maze[a][b - 1] = "1"
            return maze_solver(a, b - 1, health_time - 1)
        if maze[a][b - 1] == "P":
            maze[a][b - 1] = "1"
            return maze_solver(a, b - 1, health_time - 1)
        if maze[a - 1][b] == "H":
            health_time = int(sys.argv[3])
            maze[a - 1][b] = "1"
            return maze_solver(a - 1, b, health_time - 1)
        if maze[a - 1][b] == "P":
            maze[a - 1][b] = "1"
            return maze_solver(a - 1, b, health_time - 1)
        if maze[a + 1][b] == "H":
            health_time = int(sys.argv[3])
            maze[a + 1][b] = "1"
            return maze_solver(a + 1, b, health_time - 1)
        if maze[a + 1][b] == "P":
            maze[a + 1][b] = "1"
            return maze_solver(a + 1, b, health_time - 1)
    else:                             # arada bir yerdeysek kontrol edilecekler
        if maze[a + 1][b] == "F" or maze[a - 1][b] == "F" or maze[a][b - 1] == "F":
            health_time -= 1
            return maze
        if maze[a][b - 1] == "H":
            health_time = int(sys.argv[3])
            maze[a][b - 1] = "1"
            return maze_solver(a, b - 1, health_time - 1)
        if maze[a][b - 1] == "P":
            maze[a][b - 1] = "1"
            return maze_solver(a, b - 1, health_time - 1)
        if maze[a - 1][b] == "H":
            health_time = int(sys.argv[3])
            maze[a - 1][b] = "1"
            return maze_solver(a - 1, b, health_time - 1)
        if maze[a - 1][b] == "P":
            maze[a - 1][b] = "1"
            return maze_solver(a - 1, b, health_time - 1)
        if maze[a + 1][b] == "H":
            health_time = int(sys.argv[3])
            maze[a + 1][b] = "1"
            return maze_solver(a + 1, b, health_time - 1)
        if maze[a + 1][b] == "P":
            maze[a + 1][b] = "1"
            return maze_solver(a + 1, b, health_time - 1)
        if maze[a][b + 1] == "H":
            health_time = int(sys.argv[3])
            maze[a][b + 1] = "1"
            return maze_solver(a, b + 1, health_time - 1)
        if maze[a][b + 1] == "P":
            maze[a][b + 1] = "1"
            return maze_solver(a, b + 1, health_time - 1)
    if a == 0:                               # ilk satır
        if b == 0:
            if maze[0][1] == "1":
                maze[0][0] = "W"
                return maze_solver(a, b + 1, health_time)
            if maze[1][0] == "1":
                maze[0][0] = "W"
                return maze_solver(a + 1, b, health_time)
        elif b == len(maze[0]) - 1:
            if maze[a][b - 1] == "1":
                maze[a][b] = "W"
                return maze_solver(a, b - 1, health_time)
            if maze[a + 1][b] == "1":
                maze[a][b] = "W"
                return maze_solver(a + 1, b, health_time)
        else:
            if maze[a][b + 1] == "1":
                maze[a][b] = "W"
                return maze_solver(a, b + 1, health_time)
            if maze[a][b - 1] == "1":
                maze[a][b] = "W"
                return maze_solver(a, b - 1, health_time)
            if maze[a + 1][b] == "1":
                maze[a][b] = "W"
                return maze_solver(a + 1, b, health_time)
    elif a == len(maze) - 1:                   # son satır
        if b == 0:
            if maze[a][b + 1] == "1":
                maze[a][b] = "W"
                return maze_solver(a, b + 1, health_time)
            if maze[a - 1][b] == "1":
                maze[a][b] = "W"
                return maze_solver(a - 1, b, health_time)
        elif b == len(maze[a]) - 1:
            if maze[a][b - 1] == "1":
                maze[a][b] = "W"
                return maze_solver(a, b - 1, health_time)
            if maze[a - 1][b] == "1":
                maze[a][b] = "W"
                return maze_solver(a - 1, b, health_time)
        else:
            if maze[a][b + 1] == "1":
                maze[a][b] = "W"
                return maze_solver(a, b + 1, health_time)
            elif maze[a][b - 1] == "1":
                maze[a][b] = "W"
                return maze_solver(a, b - 1, health_time)
            elif maze[a - 1][b] == "1":
                maze[a][b] = "W"
                return maze_solver(a - 1, b, health_time)
    elif  b == 0 and a != 0 and a != (len(maze) - 1):                   # ilk sütun
        if maze[a][b + 1] == "1":
            maze[a][b] = "W"
            return maze_solver(a, b + 1, health_time)
        if maze[a - 1][b] == "1":
            maze[a][b] = "W"
            return maze_solver(a - 1, b, health_time)
        if maze[a + 1][b] == "1":
            maze[a][b] = "W"
            return maze_solver(a + 1, b, health_time)
    elif b == (len(maze[0]) - 1) and a != 0 and a != len(maze) - 1:    # son sütun
        if maze[a][b - 1] == "1":
            maze[a][b] = "W"
            return maze_solver(a, b - 1, health_time)
        if maze[a - 1][b] == "1":
            maze[a][b] = "W"
            return maze_solver(a - 1, b, health_time)
        if maze[a + 1][b] == "1":
            maze[a][b] = "W"
            return maze_solver(a + 1, b, health_time)
    else:
        if maze[a][b + 1] == "1":
            maze[a][b] = "W"
            return maze_solver(a, b + 1, health_time)
        if maze[a][b - 1] == "1":
            maze[a][b] = "W"
            return maze_solver(a, b - 1, health_time)
        if maze[a + 1][b] == "1":
            maze[a][b] = "W"
            return maze_solver(a + 1, b, health_time)
        if maze[a - 1][b] == "1":
            maze[a][b] = "W"
            return maze_solver(a - 1, b, health_time)
maze_solver(a, b, health_time)
for line in range(len(maze)):
    for i in range(len(maze[line])):
        if maze[line][i] == "W":
            maze[line][i] = "0"
        if maze[line][i] == "P":
            maze[line][i] = "0"
sys.argv[4].write("Maze without health condition:\n")
for line in maze:
    line.append("\n")
for line in maze:
    sys.argv[4].writelines(line)
maze = []
for line in sys.argv[2]:
    line = line.strip("\n")
    line = list(line)
    maze.append(line)
for line in maze:
    if 'S' in line:
        a = maze.index(line)
        b = line.index('S')
maze_solver(a, b, health_time)
for line in range(len(maze)):
    for i in range(len(maze[line])):
        if maze[line][i] == "W":
            maze[line][i] = "0"
        if maze[line][i] == "P":
            maze[line][i] = "0"
sys.argv[4].write("Maze with health condition:\n")
for line in maze:
    line.append("\n")
for line in maze:
    sys.argv[4].writelines(line)

