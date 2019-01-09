import numpy as np
def give_rain_volume(list_of_heights):
    island_len = len(list_of_heights)
    idx = 0
    total_vol = 0
    while idx <= island_len-2:
        if list_of_heights[idx] > list_of_heights[idx+1]:
            first_shore_idx = idx
            second_shore_idx = find_next_shore(list_of_heights, first_shore_idx=first_shore_idx)
            if second_shore_idx == None:
                lake_volume = 0
            else:
                lake_volume = calculate_lake_volume(list_of_heights, first_shore_idx, second_shore_idx)
                idx = second_shore_idx
            total_vol += lake_volume
        else:
            idx += 1
    return total_vol


def find_next_shore(list_of_heights, first_shore_idx):
    island_len = len(list_of_heights)
    idx = first_shore_idx + 1
    while idx <= island_len-1:
        if idx == island_len-1:
            m_idx = np.argmax(list_of_heights[first_shore_idx+1:idx+1]) + first_shore_idx+1
            if m_idx == first_shore_idx+1:
                return None
            else:
                return m_idx
        elif list_of_heights[idx] >= list_of_heights[first_shore_idx]:
            return idx
        else:
            idx += 1

def calculate_lake_volume(list_of_heights, first_shore_idx, second_shore_idx):
    lake_height = min(list_of_heights[first_shore_idx], list_of_heights[second_shore_idx])
    vol = 0
    for patch_height in list_of_heights[first_shore_idx+1:second_shore_idx]:
        vol += (lake_height - patch_height)
    return vol


give_rain_volume([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2])