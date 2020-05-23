from csv import writer

def writeToCollege(colleges):
    with open("colleges.csv", "w") as csv_file:
        csv_writer = writer(csv_file)

        for state in colleges:
            csv_writer.writerow([state])
            for college in colleges[state]:
                csv_writer.writerow(["".join(["\t", college])])
                for requirements in colleges[state][college]:
                    csv_writer.writerow(["".join(["\t\t", requirements])])