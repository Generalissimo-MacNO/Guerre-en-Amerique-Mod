# -*- coding: utf-8 -*-
from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.05),("woku_pirates", -0.02),("shinano_rebels", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",   "{!}culture_1", 0, 0.9, [], []),
  ("culture_2",   "{!}culture_2", 0, 0.9, [], []),
  ("culture_3",   "{!}culture_3", 0, 0.9, [], []),
  ("culture_4",   "{!}culture_4", 0, 0.9, [], []),
  ("culture_5",   "{!}culture_5", 0, 0.9, [], []),
  ("culture_6",   "{!}culture_6", 0, 0.9, [], []),
  ("culture_7",   "{!}culture_7", 0, 0.9, [], []),
  ("culture_8",   "{!}culture_8", 0, 0.9, [], []),
  ("culture_9",   "{!}culture_9", 0, 0.9, [], []),
  ("culture_10",  "{!}culture_10", 0, 0.9, [], []),
  ("culture_11",  "{!}culture_11", 0, 0.9, [], []),
  ("culture_12",  "{!}culture_12", 0, 0.9, [], []),
  ("culture_13",  "{!}culture_13", 0, 0.9, [], []),
  ("culture_14",  "{!}culture_14", 0, 0.9, [], []),
  ("culture_15",  "{!}culture_15", 0, 0.9, [], []),
  ("culture_16",  "{!}culture_16", 0, 0.9, [], []),
  ("culture_17",  "{!}culture_17", 0, 0.9, [], []),
  ("culture_18",  "{!}culture_18", 0, 0.9, [], []), #
  ("culture_19",  "{!}culture_19", 0, 0.9, [], []), #
  ("culture_20",  "{!}culture_20", 0, 0.9, [], []), #
  ("culture_player",  "{!}culture_player", 0, 0.9, [], []),

#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("deserters", -0.02),("woku_pirates", 0.0),("shinano_rebels", -0.02)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
  ("kingdom_1",   "British America",		0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.50),("shinano_rebels", -0.01)], [], 0x993333), #British America 100
  ("kingdom_2",   "Nouvelle-France",	    0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", +0.50),("shinano_rebels", -0.50)], [], 0x003168), #New France 100
  ("kingdom_3",   "Nueva España",		    0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xFFD700), #New Spain 100
  ("kingdom_4",   "Haudenosaunee",		    0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05),("kingdom_7", +0.9)], [], 0x8502F7), #Iroquois 85
  ("kingdom_5",   "Ani-Yvwiya",  	        0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xF28305), #Cherokee 75
  ("kingdom_6",   "Wabana'ki Mawuhkacik",  	0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x28694B), #Wabanaki 85
  ("kingdom_7",   "Kanien'keha:ka",	        0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05),("kingdom_4", +0.9)], [], 0x5e3000), #Mohawk 85
  ("kingdom_8",   "Wyandot",		        0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xa6d5ff), #Huron 75
  ("kingdom_9",   "Lenapehoking",		    0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xe0ba81), #Lenape 65
  ("kingdom_10",  "Myaamia",		        0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xffff80), #Miami 60
  ("kingdom_11",  "Shaawana",	            0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xff4444), #Shawnee 65
  ("kingdom_12",  "Nishnaabe",	            0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xc5a43d), #Odawa 65
  ("kingdom_13",  "Anishinaabe",		    0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x000000), #Ojibwe 60
  ("kingdom_14",  "Neshnabek",             	0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x680000), #Potawatomi 60
  ("kingdom_15",  "Chatah",	                0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x2e1891), #Choctaw 60
  ("kingdom_16",  "Chikasha",	            0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xe4af3b), #Chickasaw 60
  ("kingdom_17",  "Este Mvskokvlke",	    0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x60b33b), #Creek 60
  ("kingdom_18",  "Unused",	                0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xffffff),
  ("kingdom_19",  "Unused",	                0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xffffff), 
  ("kingdom_20",  "Unused",	                0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xffffff), 

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1),("woku_pirates", 0.00)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("woku_pirates","Acadiens", 0, 0.5,[("commoners",-0.2),("merchants",-0.7),("manhunters",-0.6),("player_faction",0.0)], [], 0x888888),
  ("shinano_rebel","Frontiersmen", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("shinano_rebels","{!}Shinano Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
]

##diplomacy start+ Define these for convenience
dplmc_factions_begin = 1 #As mentioned in the notes above, this is hardcoded and shouldn't be altered.  Deliberately excludes "no faction".
dplmc_non_generic_factions_begin = [x[0] for x in enumerate(factions) if x[1][0] == "merchants"][0] + 1
dplmc_factions_end   = len(factions)
##diplomacy end+

# modmerger_start version=201 type=4
try:
    component_name = "factions"
    var_set = { "factions":factions,"default_kingdom_relations":default_kingdom_relations, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
