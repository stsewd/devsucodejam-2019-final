def searchEngine(query, elements):
    elements = sorted(elements)
    results = []
    for i in range(2, len(query) + 1):
        word = query[:i]
        results.append(
            [
                element
                for element in elements
                if element.startswith(word)
            ]
        )
        elements = results[-1]
    results = [
        r[:3]
        for r in results
    ]
    return results
