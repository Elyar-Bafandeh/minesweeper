class game_object:
    def __init__(self , id = "blank" , status = "unmarked" , neighbour_bomb = 0 , position = (None , None) , isVisiable = False):
        self.id = id 
        self.status = status
        self.neighbourBomb = neighbour_bomb
        self.pos = position
        self.isVisiable = isVisiable
