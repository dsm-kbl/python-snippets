import json
import copy
import os
from cfn_flip import flip, to_json, to_yaml


def create_cfn():
    template_file = open(r'data.yaml')
    template_str = template_file.read()

    template = json.loads(to_json(template_str))

    accessLogsBucket = template["Resources"]["AccessLogsBucket"]

    print(accessLogsBucket)


create_cfn()
