import json

def read_maxes():
    """Helper function that opens maxes.json"""
    with open("maxes.json", "r") as file:
        return json.load(file)

def write_maxes(data):
    """Helper function that passes 'data' to be written to maxes.json"""
    with open("maxes.json", "w") as file:
        json.dump(data, file, indent=4)


def get_max(lift):
    """Uses helper function 'read_maxes' to returns desired lift max by entering 'bench_max', 'squat_max', 'dead_max', or 'press_max'"""
    data = read_maxes()
    return data[lift][1]

def get_name(lift):
    """Uses helper function 'read_maxes' to returns desired lift max by entering 'bench_max', 'squat_max', 'dead_max', or 'press_max'"""
    data = read_maxes()
    return data[lift][0]


def weight_calc(lift, percent):
    """Helper function that calculates desired percentage of lift."""
    weight = lift * (percent / 100)
    return round(weight)


def set_creator(lift, a, b, c=5):
    """Calculates weight percentages from a to b in increments of c%"""
    return {percent: weight_calc(lift, percent) for percent in range(a, b+c, c)}


def max_update(lift_max):
    """Update desired lift in maxes.json by entering 'bench_max', 'squat_max', 'dead_max', or 'press_max'"""
    data = read_maxes()
    data[lift_max] = int(input(f'Enter a new max for {lift_max}: '))
    write_maxes(data)
    print(f'Successfully updated')

    
def update_all_maxes():
    """Updates all maxes"""
    maxArr = ['bench_max', 'squat_max', 'dead_max', 'press_max']
    for max in maxArr:
        max_update(max)

