from phue import Bridge
import sys

group_name, action = sys.argv[1:]

# TODO: env var?
b = Bridge('192.168.1.119')

b.connect()
b.get_api()

group_id = b.get_group_id_by_name(group_name)
light_ids = b.get_group(group_name, "lights")
lights = b.get_light_objects('id')

for light_id in light_ids:
    light_id = int(light_id)
    if action.lower() == 'on':
        lights[light_id].on = True
    elif action.lower() == 'off':
        lights[light_id].on = False
    elif action.lower() == 'toggle':
        lights[light_id].on = not lights[light_id].on
    else:
        print(f"Invalid action: {action}")
        break
