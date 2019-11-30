connected_fmt = 'The workers are connected with a grade of {}'
not_connected_fmt = 'The workers have no connection with each other'

def find_connection(connections, first, second, grade):
    if first == second:
        return grade
    search = connections.get(first)
    if not search:
        return None
    all_con = (
        find_connection(connections, c, second, grade + 1)
        for c in search
    )
    all_con = [
        r
        for r in all_con
        if r is not None
    ]
    if not all_con:
        return None
    return min(all_con)

def workers(connections, first, second):
    connections_d = {}
    for a, b in connections:
        connections_d.setdefault(a, [b]).append(b)
    r = find_connection(connections_d, first, second, 0)
    if r is None:
        return not_connected_fmt
    return connected_fmt.format(r)
