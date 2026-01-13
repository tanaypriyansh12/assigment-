def get_all_decodings(cipher_text):
    # Mapping based on Alice's specific rules
    morse_rules = {
        "._": "A", "_...": "B", "_._.": "C", "_..": "D", ".": "E",
        ".._.": "F", "__.": "G", "....": "H", "..": "I", ".---": "J",
        "_._": "K", "._..": "L", "__": "M", "_.": "N", "___": "O",
        ".__.": "P", "__._": "Q", ".-.": "R", "...": "S", "_": "T",
        ".._": "U", "..._": "V", ".__": "W", "_.._": "X", "_.__": "Y",
        "__..": "Z"
    }

    results = []

    def solve(remaining, path):
        if not remaining:
            results.append(path)
            return

        # Check segments from length 1 to 4
        for i in range(1, 5):
            if i <= len(remaining):
                segment = remaining[:i]
                if segment in morse_rules:
                    solve(remaining[i:], path + morse_rules[segment])

    solve(cipher_text, "")
    return sorted(results)

if __name__ == "__main__":
    import sys
    # Reading input from STDIN
    input_data = sys.stdin.read().strip()
    if input_data:
        decoded_words = get_all_decodings(input_data)
        for word in decoded_words:
            print(word)