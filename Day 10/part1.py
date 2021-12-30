with open("chunk_data.txt", "r") as f:
    illegal_chars = []
    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    for line in f:
        stack = []
        for char in line.strip():
            if char in bracket_pairs:
                stack.append(char)
            else:
                open_bracket = stack.pop()
                if bracket_pairs[open_bracket] != char:
                    # Illegal character
                    illegal_chars.append(char)
                    break

illegal_char_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

syntax_score = 0
for char in illegal_chars:
    syntax_score += illegal_char_scores[char]

print(syntax_score)
