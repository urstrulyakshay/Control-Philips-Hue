from ipaddress import ip_address
from phue import Bridge
from ip_adress import IPaddress


def light_list(IPaddress):
    b = Bridge(IPaddress)
    list_of_light_names = b.get_light_objects('name')
    return list_of_light_names

def daytime_light():
    lights = light_list(IPaddress)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 20000
        lights[light].saturation = 100

def cozy_light():
    lights = light_list(IPaddress)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 190
        lights[light].saturation = 100



if __name__ == '__main__':
    daytime_light()
    #cozy_light()
