from Trello import Trello
import json
import sys
import csv


def main():
    
    with open('parameters.json', 'r') as json_file:
        data = json.load(json_file)

    trello_client = Trello(data["key"], data["token"], data["id"])

    option = input("Enter the desired option (manual/csv):")
    if option != "manual" and option != "csv":
        print("Wrong option")
        return -1

    elif option == "manual":

        print("Enter the values for the desired Card separated by spaces (card_name list_id card_description) or path_to_csv\csv_name.csv")
        x = sys.stdin.readline().strip().split()
        print("Card: ", x[0])
        print("Id of the List: ", x[1])
        description = ""
        for i in range(2, len(x)-1):
            description += x[i] + " "
        description += x[-1]
        print("Descripton of the Card: ", description)

        trello_client.create_new_card(x[0], x[1], description)
        
    elif option == "csv":
        path_csv = input("Enter the path to the csv:")
        if path_csv[-4:] != ".csv":
            print("The file given is not a .csv")
            return -1
        
        with open(path_csv, newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in data:
                if len(row) != 3 or ("" in row):
                    print("Something went wrong with the parameters taken from the csv: {}".format(row))
                    continue
                trello_client.create_new_card(row[0], row[1], row[2])

if __name__ == "__main__":
    main()