import statistics

with open("chunk_data.txt", "r") as f:
    completion_scores = []
    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    closing_bracket_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    for line in f:
        stack = []
        for char in line.strip():
            if char in bracket_pairs:
                stack.append(char)
            else:
                open_bracket = stack.pop()
                if bracket_pairs[open_bracket] != char:
                    # Illegal character, clear stack
                    stack = []
                    break

        if stack:
            # Incomplete line
            score = 0
            for open_bracket in reversed(stack):
                score *= 5
                score += closing_bracket_scores[bracket_pairs[open_bracket]]
            completion_scores.append(score)

print(statistics.median(completion_scores))
