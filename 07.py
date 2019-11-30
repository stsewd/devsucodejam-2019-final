# Missing, didn't understood the statement

def reservoirs(connections):
    connections_d = {}
    for a, b in connections:
        connections_d.setdefault(a, [b]).append(b)
