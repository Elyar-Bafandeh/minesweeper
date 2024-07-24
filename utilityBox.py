from constants import HUD_AREA , BOX_SIDE
def get_index(click_pos , size):
    return ((click_pos[0]-HUD_AREA)//(BOX_SIDE)  , (click_pos[1]-50)//(BOX_SIDE))

def is_in_2dArray(array , obj):
    for i in array:
        for j in i:
            if j.pos == obj.pos:
                return True 
    return False