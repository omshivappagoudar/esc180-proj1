def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it.
    '''
    global cur_temp # in degrees Celsius
    global cur_charge # in percentage points
    global cur_time # in minutes
    global overcharges # stores overcharges in minutes

    global good_battery_health

    cur_time = 0
    good_battery_health = True
    cur_temp = 20
    cur_charge = 50 #cur_charge < 101
    overcharges = []



def update_battery_health():

    global cur_time # in minutes
    global good_battery_health # boolean
    global overcharges # stores overcharges in minutes

    if len(overcharges) >= 3:

        if overcharges[-3] > (cur_time-360):
            good_battery_health = False



def update_overcharges():

    global cur_charge # in percentage points
    global cur_time # in minutes
    global overcharges # stores overcharges in minutes

    if cur_charge >= 90:
        overcharges.append(cur_time) 



def simulate_activity(activity, duration):
    
    global cur_temp # in degrees Celsius
    global cur_charge # in percentage points
    global cur_time # in minutes
    global good_battery_health # boolean
    global overcharges # stores overcharges in minutes

    if activity == 'charge': 

        fast_charging_time = duration_fast_charge_possible()

        if fast_charging_time > duration:
            fast_charging_time = duration

        while fast_charging_time > 0:
            cur_time += 1
            cur_charge += 3 
            cur_temp += 0.5 
            duration -= 1   
            fast_charging_time -= 1

        while duration > 0 and good_battery_health:

            overcharge_recorded = False

            if cur_charge >= 100:
                cur_time += 1
                cur_temp += 0.25 
                duration -= 1 
                continue

            if not overcharge_recorded and cur_charge >= 90:
                overcharge_recorded = True
                update_overcharges()
                update_battery_health()

            cur_time += 1
            cur_charge = min(100.0, cur_charge + 1)
            cur_temp += 0.25 
            duration -= 1  

            

        while duration > 0 and not good_battery_health:

            if cur_charge <= 80:
                cur_time += 1
                cur_charge = min(80.0, cur_charge + 1)
                cur_temp += 0.25 
                duration -= 1  
            else:
                cur_time += 1
                cur_temp += 0.25 
                duration -= 1                

    if activity == 'use':

        while duration > 0:

            if cur_charge <= 0:
                cur_temp = max(0.0, cur_temp - 1)
                cur_time += 1
                duration -= 1
                continue
                
            cur_charge = max(0.0, cur_charge - 2)
            cur_temp += 1
            cur_time += 1
            duration -= 1

    if activity == 'idle':

        while duration > 0:
        
            if cur_charge <= 0:
                cur_temp = max(0.0, cur_temp - 1)
                cur_time += 1
                duration -= 1
                continue
                        
            cur_charge = max(0.0, cur_charge - 0.5)
            cur_temp = max(0.0, cur_temp - 1)
            cur_time += 1
            duration -= 1
    

def duration_fast_charge_possible(): # checks the duration fast charging is possible

    global cur_temp # in degrees Celsius
    global cur_charge # in percentage points
    global cur_time # in minutes
    global good_battery_health # boolean
    global overcharges # stores overcharges in minutes

    temp = cur_temp
    charge = cur_charge

    if not good_battery_health:
        return 0
    
    possible = (charge < 80) and (0 <= temp <= 40)
    duration = 0
   
    while possible:
        temp += 0.5
        charge += 3
        possible = (charge < 80) and (0 <= temp <= 40)
        duration += 1
        
    return duration
    

def get_cur_temp(): # returns the current temperature of the battery (float)
    global cur_temp
    return cur_temp

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
