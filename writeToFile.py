from csv import writer

def writeToCollege(colleges):
    with open("colleges.csv", "w") as csv_file:
        # csv_writer = writer(csv_file)
        csv_file.write("State, College, National Rank, Applications Accepted, In state tuition, Out of State Tuition, On Campus Housing, SAT, GPA, Applicant Competition, \n")
        for state in colleges:
            # csv_writer.writerow([state])
            for college in colleges[state]:
                # csv_writer.writerow(["".join(["\t", college])])
                csv_file.write("".join([state+", ", college + ", ", "".join(colleges[state][college]), "\n"]))