# if you will create an api doc using openapi, use this python script to get the $ref paths and create the yaml files automatically! Don't forget to put the file paths in the openapi.yaml!

import yaml
import os
n = 0

# OpenAPI YAML file path
openapi_file = 'openapi.yaml'

# Read the OpenAPI YAML file
with open(openapi_file, 'r') as f:
    openapi_data = yaml.safe_load(f)
# Get all the $ref parameters
for reports in openapi_data["paths"].values():
    if os.path.exists(reports["$ref"]):
        print("already exists, skipping...")
    else:
        a = open(reports["$ref"], 'a')
        a.write('get:\n  tags:\n    - Customer\n  summary: a\n  description: a\n  security:\n    - Token: []\n  responses:\n    "200":\n      description: OK\n      content:\n        application/json:\n          schema:\n            type: string\n          examples:\n            response:\n              value:\n                {}\n    "400":\n      description: Bad Request \n      content:\n        application/json:\n          schema:\n            type: string\n          examples:\n            response:\n              value:\n                {}\n    "401":\n      description: Unauthorized\n      content:\n        text/plain:\n          schema:\n            type: string\n          examples:\n            response:\n              value:\n                Unauthorized (Token not found on request)\n  requestBody:\n    content:\n      application/json:\n        schema:\n          type: string\n          example:\n            {}\n    required: true')
        a.close
    print(reports["$ref"])
