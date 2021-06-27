from Trello import Trello
import json
import sys


def main():
    
    with open('parameters.json', 'r') as json_file:
        data = json.load(json_file)

    trello_client = Trello(data["key"], data["token"], data["id"])

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

if __name__ == "__main__":
    main()
