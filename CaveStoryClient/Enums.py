from enum import Enum


class CSPacket(Enum):
    READINFO = 0
    RUNTSC = 1
    READFLAGS = 2
    RUNEVENTS = 3
    READMEM = 4
    WRITEMEM = 5
    READSTATE = 6
    ERROR = 255
    DISCONNECT = 255


class CSTrackerAutoTab(Enum):
    MIMIGA_VILLAGE = 0
    REG_EGG_CORRIDOR = 1
    RUIN_EGG_CORRIDOR = 2
    OUTER_WALL = 3
    GRASSTOWN = 4
    SAND_ZONE = 5
    LABYRINTH_WEST = 6
    LABYRINTH_EAST = 7
    PLANTATION = 8
    SACRED_GROUNDS = 9


class CSTrackerEvent(Enum):
    SAVED_SUE = 0
    """Occurs when you talk to Sue in Egg Corridor"""
    SAVED_KAZUMA = 1
    """Occurs after destroying the shelter door in Grasstown"""
    SAVED_CURLY = 2
    """Occurs after Curly is carried through the Main Artery"""
    USED_MA_PIGNON = 3
    """Occurs after feeding Curly Ma Pignon"""
    DEFEATED_BALROG_1 = 3
    """Occurs after defeating Balrog in Mimiga Village"""
    DEFEATED_IGOR = 4
    """Occurs after defeating Igor in Egg Corridor"""
    DEFEATED_BALROG_2 = 5
    """Occurs after defeating Balrog in Power Room"""
    DEFEATED_BALFROG = 6
    """Occurs after defeating Balfrog in Gum"""
    DEFEATED_CURLY = 7
    """Occurs after defeating Curly in Sand Zone Residence"""
    DEFEATED_OMEGA = 8
    """Occurs after defeating Omega in Sand Zone"""
    DEFEATED_TOROKO = 9
    """Occurs after defeating Frenzied Toroko in Sand Zone Warehouse"""
    DEFEATED_PUU_BLACK = 10
    """Occurs after defeating Puu Black in Old Clinic"""
    DEFEATED_MONSTER_X = 11
    """Occurs after defeating Monster X in Labrynith"""
    DEFEATED_BALROG_3 = 12
    """Occurs after defeating Balrog in Boulder Chamber"""
    DEFEATED_CORE = 13
    """Occurs after defeating the Core"""
    DEFEATED_IRONHEAD = 14
    """Occurs after defeating Ironhead in Main Artery"""
    DEFEATED_THE_SISTERS = 15
    """Occurs after defeating The Sisters in Ruined Egg Observation Chamber"""
    DEFEATED_MA_PIGNON = 16
    """Occurs after defeating Ma Pignon in Store Room"""
    DEFEATED_RED_DEMON = 17
    """Occurs after defeating Red Demon in Hidden Last Cave"""
    FINAL_BOSS = 18
    """Occurs after defeating Undead Core or Ballos (depending on goal)"""
