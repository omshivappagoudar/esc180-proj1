def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it.
    '''
    global cur_temp # in degrees Celsius
    global cur_charge # in percentage points
    global cur_time # in minutes

    global good_battery_health

    cur_time = 0
    good_battery_health = True

def global_var_initializer(): # this function initializes the global variables at the start of each function
    global cur_temp # in degrees Celsius
    global cur_charge # in percentage points
    global cur_time # in minutes
    global good_battery_health # boolean

def simulate_activity(activity, duration):
    pass

def duration_fast_charge_possible(): # checks the duration fast charging is possible
    global_var_initializer()
    temp = cur_temp
    charge = cur_charge

    if !good_battery_health:
        return 0

    possible = (charge < 80) and (temp < 40)
    duration = 0

    while possible:
        temp += 0.5
        charge += 3
        possible = (charge < 80) and (temp < 40)

    return duration
    

def get_cur_temp(): # returns the current temperature of the battery (float)
    global get_cur_temp
    return get_cur_temp

def get_cur_charge(): # returns the current charge of the battery(float)
    global cur_charge 
    return cur_charge

def get_cur_battery_health(): # returns whether the battery is in good health or no (boolean)
    global good_battery_health
    return good_battery_health

def charge_time_needed(minutes):
    pass

if __name__ == '__main__':
    initialize()

    print(duration_fast_charge_possible()) # 10
    print(charge_time_needed(50)) # 30

    simulate_activity("charge",30)
    print(get_cur_charge()) # 100
    print(get_cur_temp()) # 30

    simulate_activity("use",50)
    print(get_cur_charge()) # 0
    print(get_cur_temp()) # 80

    simulate_activity("use",10)
    print(get_cur_charge()) # 0
    print(get_cur_temp()) # 70

    simulate_activity("charge",100)
    print(get_cur_charge()) # 100
    print(get_cur_temp()) # 95

    simulate_activity("idle",100)
    print(get_cur_charge()) # 50
    print(get_cur_temp()) # 0
    print(get_cur_battery_health()) # True
    print(duration_fast_charge_possible()) # 10

    simulate_activity("charge",80)
    print(get_cur_charge()) # 90
    print(get_cur_temp()) # 22.5
    print(get_cur_battery_health()) # False

    simulate_activity("use",40)
    print(get_cur_charge()) # 10
    print(get_cur_temp()) # 62.5

    simulate_activity("charge",80)
    print(get_cur_charge()) # 80
    print(get_cur_temp()) # 82.5

    initialize()
    # add your tests here
