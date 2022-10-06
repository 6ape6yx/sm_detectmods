# This script will create list of used mods
# for your Scrap Mechanic blueprint

import os
import json
from glob import glob

# Find blueprint directory by name
def find_blueprint(path, bp_name):
    for file in glob(path + '\\*\\description.json'):
        with open(file) as description_json:
            description = json.load(description_json)
            description_json.close()
            if description['name'] == bp_name:
                return description['localId']
            else:
                continue

# Get list of mods from blueprint.json
def get_mods_list(bp_name, **kwargs):
    default_path = 'C:\\Users\\' + os.getlogin() + '\\AppData\\Roaming\\Axolot Games\\Scrap Mechanic\\User\\*\\Blueprints'
    path = kwargs.get('bp_path', default_path)
    bp_uuid = find_blueprint(path, bp_name)
    with open(path + '\\' + bp_uuid + '\\blueprint.json') as blueprint_json:
        blueprint = json.load(blueprint_json)
        for mod in blueprint['dependencies']:
            print(mod['name'])


def main():
    # You can use custom blueprints path
    # Example:
    # my_path = "C:\\Users\\vasya\\AppData\\Roaming\\Axolot Games\\Scrap Mechanic\\User\\User_*************\\Blueprints"
    # get_mods_list(bp_name, bp_path=my_path)
    bp_name = input('Blueprint name: ')
    get_mods_list(bp_name)

main()
