# coding=UTf-8
import requests
import json


class Trello:
        def __init__(self, trello_key, trello_token, trello_id):
            self.trello_key = trello_key
            self.trello_token = trello_token
            self.trello_id = trello_id

            self._print_json_parameters()

            
            #self._create_new_card("nueva_carta", "Esta es la nueva carta que he escrito desde codigo")
            board_json = self._get_boards()
            print("Board {} exists with the given id".format(board_json["name"]))
        
            print("The following Lists have been found within the mentioned Board:")
            self.lists = self._get_lists()
            for key in self.lists:
                print(" - Name: {}, id: {}".format(key, self.lists[key]))
            

        
        def _print_json_parameters(self):
            print("key got from json file: {}".format(self.trello_key))
            print("token got from json file: {}".format(self.trello_token))
            print("board id got from json file {}".format(self.trello_id))
            print("---------------------------------------------------------------------")
        
        def create_new_card(self, card_name, list_id, card_desc):
            
            url = "https://api.trello.com/1/cards"

            query = {
            'key': self.trello_key,
            'token': self.trello_token,
            'idList': list_id,
            'name':card_name,
            'desc':card_desc
            }

            response = requests.request(
            "POST",
            url,
            params=query
            )

            if response.status_code == 200:
                print("Card added successfully")
            else:
                print("Something went wrong when trying to add the Card")



        def _create_new_cards_from_csv(self):
            pass


        def _get_lists(self):
            url = "https://api.trello.com/1/boards/{}/lists".format(self.trello_id)

            query = {
            'key': self.trello_key,
            'token': self.trello_token
            }

            response = requests.request(
            "GET",
            url,
            params=query
            )

            if response.status_code != 200:
                print("Something went wrong retrieving the Lists form the mentioned board; Status code {}".format(response.status_code ))
                return -1

            lists = json.loads(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
            lists_dict = {}
            for list in lists:
                lists_dict[list["name"].encode('ascii', 'ignore')] = list["id"].encode('ascii', 'ignore')
            return lists_dict
            

        def _get_boards(self):
            url = "https://api.trello.com/1/boards/{}".format(self.trello_id)

            headers = {
            "Accept": "application/json"
            }

            query = {
            'key': self.trello_key,
            'token': self.trello_token
            }

            response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
            )

            if response.status_code != 200:
                print("Something went wrong retrieving the Board Name; Status code {}".format(response.status_code ))
                return -1

            return json.loads(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

