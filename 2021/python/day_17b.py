import sys

# pass 4 values as comand line args
min_x = int(sys.argv[1])
max_x = int(sys.argv[2])
min_y = int(sys.argv[3])
max_y = int(sys.argv[4])

count = 0
for v0_x in range(1, max_x + 1):
    for v0_y in range(min_y, -min_y):
        x, y, v_x, v_y = 0, 0, v0_x, v0_y
        while x <= max_x and y >= min_y:
            if x >= min_x and y <= max_y:
                count += 1
                break

            x += v_x
            y += v_y
            v_x = max(v_x - 1, 0)
            v_y -= 1


print(count)
