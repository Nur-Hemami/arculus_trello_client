# arculus_trello_client
Client application to communicate with Arculus' Trello board.

This app is a client for Arculus organizational Kanban board.It allows the user to create new cards within the command line tool.

In order to do that a .json file should be configured with the parameters corresponding to the Arculus organizational borad. An example of this is provided in parameters_example.json.

## Running the application
To run the application, the user must start by executing the following command:

```console
foo@bar:~$ python3 Arculus_client.py
foo
```

The user will be prompt to introduce cards manually or by a .csv file.

In case of choosing manual process the user must introduce the parameters following this format: card_name list_id description.
An example of this looks like this:
```console
Enter the desired option (manual/csv):manual
Enter the values for the desired Card separated by spaces (card_name list_id card_description) or path_to_csv\csv_name.csv
Code-Refactoring 60d87219d408b73c6056150d Code refactor was done correctly with the proper push to the repository
Card:  Code-Refactoring
Id of the List:  60d87219d408b73c6056150d
Descripton of the Card:  Code refactor was done correctly with the proper push to the repository
Card added successfully
foo
```

After adding this card, our Kanban boards should look like the following image:

![alt text](./images/example1.png)

The user can also pick the option of adding Cards through csv file. To do that, every card will consist of a row in the csv file and each row is formed by card_name, list_id, description.
An example of this can be found in this repository as example.csv:

![alt text](./images/example2.png)

