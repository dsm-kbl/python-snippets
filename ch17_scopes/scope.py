import json

X = 99

def func(Y):
    return X + Y

print(func(1))

event_str = '{"version": 4}'
event_json = json.loads(event_str)

event_json['topic'] = "tier/pod1/slot1/eject"

print('Event json here : ', event_json)

