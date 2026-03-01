def calculate_average(g1, g2, g3):
    return (g1 + g2 + g3) / 3


def main():
    input_file_name = input("Enter the name of the input file: ").strip()
    output_file_name = input("Enter the name of the output file: ").strip()

    infile = open(input_file_name, "r")
    outfile = open(output_file_name, "w")

    student_id = infile.readline().strip()

    while student_id != "":
        grade1 = float(infile.readline().strip())
        grade2 = float(infile.readline().strip())
        grade3 = float(infile.readline().strip())

        average = calculate_average(grade1, grade2, grade3)
        avg_print = format(average, ".2f")

        print("Student", student_id, "Average", avg_print)
        outfile.write(student_id + " " + avg_print + "\n")

        student_id = infile.readline().strip()

    infile.close()
    outfile.close()


main()
