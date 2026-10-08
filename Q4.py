code = input("Enter a line of code: ")

stack = []
pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

for char in code:
    if char in "([{":
        stack.append(char)

    elif char in ")]}":
        if not stack or stack[-1] != pairs[char]:
            print("Balanced: False")
            break

        stack.pop()

else:
    print(f"Balanced: {len(stack) == 0}")