def string_math(user_input):
    results = []
    expressions = user_input.split(";")

    for expr in expressions:
        parts = expr.strip().split()

        if len(parts) >= 3:
            operation = parts[0]
            num1 = int(parts[1])
            num2 = int(parts[2])

            if operation == "A":
                results.append(num1 + num2)

            elif operation == "S":
                results.append(num2 - num1)

    return results


def main():
    user_input = input("Enter expressions (example: A 3 4; S 2 10): ")

    results = string_math(user_input)

    print("\nResults:")
    for value in results:
        print(value)


main()
