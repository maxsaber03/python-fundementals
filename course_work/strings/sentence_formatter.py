def main():
    outfile = open("sentence_format.txt", "w")

    while True:
        sentence = input("Enter a run-together sentence (or 'no' to quit): ")

        if sentence.lower() == "no":
            break

        if not sentence:
            print("Empty input. Try again.")
            continue

        spaced = sentence[0]

        for char in sentence[1:]:
            if char.isupper():
                spaced += " "
            spaced += char

        formatted = spaced.capitalize()

        print(formatted)
        outfile.write(formatted + "\n")

    outfile.close()


main()
