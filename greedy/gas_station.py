def start_station(gas, cost):
    if len(gas) != len(cost):
        print(f'incorrect input!')
        return -1
    
    station_len = len(gas)
    start = station_len - 1


    # the loop structure could not be known in advance which is depends on the real situtaion, that's why we use while to stop the loop based on specific value
    while start >= 0:
        print(f'start_station={start}')
        remaining_gas = 0
        # treat a specifc station as start, to check if it can reach the final state
        # if not, we need to move backward one station, for start with the next station does not work either
        for i in range(0, station_len):
            cur_station = (start + i) % station_len
            cur_station_gas = gas[cur_station]
            print(f'cur_station={cur_station}, remaining_gas={remaining_gas}, cur_station_gas={cur_station_gas}, cost={cost[cur_station]}')
            remaining_gas = remaining_gas + cur_station_gas - cost[cur_station]
            print(f'remaining_gas={remaining_gas}')
            if remaining_gas < 0:
                start = start - 1
                break
        if remaining_gas < 0:
            continue
        else:
            return start
             

    return -1


# print(start_station([1, 2, 3, 4, 5],  [3, 4, 5, 1, 2]))
# print(start_station([2, 3, 4],   [3, 4, 3]))
print(start_station([5, 1, 2, 3, 4],  [4, 4, 1, 5, 1]))