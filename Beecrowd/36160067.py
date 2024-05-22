f, s, g, u, d = map(int, input().split())

def find_shortest_presses(f, s, g, u, d):
    visited = [False] * (f + 1)
    queue = [(s, 0)]  

    while queue:
        current, presses = queue.pop(0)

        if current == g:
            return presses

        up_floor = current + u
        down_floor = current - d

        if 1 <= up_floor <= f and not visited[up_floor]:
            visited[up_floor] = True
            queue.append((up_floor, presses + 1))

        if 1 <= down_floor <= f and not visited[down_floor]:
            visited[down_floor] = True
            queue.append((down_floor, presses + 1))

    return "use the stairs"

result = find_shortest_presses(f, s, g, u, d)
print(result)