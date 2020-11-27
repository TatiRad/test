import json
import logging
import os
import sys

import jsonschema
import jsonschema
from jsonschema import validate


directory_schema = '/home/nata/welltory/task_folder/schema'
list_of_schema = os.listdir(directory_schema)

directory_files = '/home/nata/welltory/task_folder/event'
list_of_files = os.listdir(directory_files)


def validateJSON(jsonData):
    try:

        json.loads(jsonData)
    except Exception as e:
        temp = sys.stdout
        sys.stdout = open('app.log', 'a')
        print(jsonData)
        print(e)
        sys.stdout.close()
        sys.stdout = temp

        return False
    return True


for file in list_of_files:
    isValid = validateJSON(file)
    if isValid == True:
        print('True')

for schema in list_of_schema:
    isValid = validateJSON(schema)
    if isValid == True:
        print('True')


def validateJson(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except Exception as err:
        temp = sys.stderr
        sys.stdout = open('app.log', 'a')
        print(jsonData)
        print(err)
        sys.stdout.close()
        sys.stderr= temp
        return False
    return True


for schema in list_of_schema:
    for file in list_of_files:
        isValid = validateJson(file, schema)
        if isValid == True:
            print('True')
