# -*- coding: utf-8 -*-
from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################
#FACTION ORDER Base
#British 1
#French 2
#Spanish 3
#Iroquois 4
#Cherokee 5
#Wabanaki 6
#Mohawk 7
#Huron 8
#Lenape 9
#Miami 10
#Shawnee 11 
#Odawa 12
#Ojibwe 13
#Potawatomi 14
#Choctaw 15
#Chickasaw 16
#Creek 17
no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(325,-85),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(325,-85),[]),                         
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(325,-85),[(trp_temp_troop,3,0)]),  
#parties before this point are hardwired. Their order should not be changed.
# -*- coding: utf-8 -*-

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]), 
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(325,-85),[]), #new:  

###############################################################  
  ("zendar","Zendar",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(697.78,-1690.26),[]), #[swycartographr] prev. coords: (280, -310) #[swycartographr] prev. coords: (104.43, -322.29)
#FACTION ORDER Towns/Cities
#British 1
  ("town_1","Halifax", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(595.69,821.92),[], 170),                       #[swycartographr] prev. coords: (-270, -199.24) #[swycartographr] prev. coords: (626.23, 862.02) #[swycartographr] prev. coords: (337.94, 465.46)
  ("town_2","Boston", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(399.88,560.95),[], 290),                           #[swycartographr] prev. coords: (-158.2, -161.29)
  ("town_3","Newport", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(399.82,530.99),[], 120),                   #[swycartographr] prev. coords: (-148.5, -148.41)
  ("town_4","New York", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(281.85,447.19),[], 170),                  #[swycartographr] prev. coords: (-105.82, -140.44)
  ("town_5","Philadelphia", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(228.73,373.39),[], 80),               #[swycartographr] prev. coords: (-79.53, -117.76) #[swycartographr] prev. coords: (220.94, 367.29) #[swycartographr] prev. coords: (120.51, 199.77)
  ("town_6","Charlestowne", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(173.32,-51.16),[], 90),                           #[swycartographr] prev. coords: (1.05, 3.11)
  ("town_7","Nassau", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(342.97,-553.35),[],165),                          #[swycartographr] prev. coords: (-41.85, 136.18) #[swycartographr] prev. coords: (-56.23, 182.97)
  ("town_8","Kingston", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(459.61,-935.49),[],195),                  #[swycartographr] prev. coords: (-51.07, 259.53)
#French 2
  ("town_9","Louisbourg", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(695.56,949.73),[],225),                  #[swycartographr] prev. coords: (-336.21, -223.4)
  ("town_10","Québec", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(273.99,838.02),[], 155),                   #[swycartographr] prev. coords: (-171, -260.21) #[swycartographr] prev. coords: (293.06, 835.85)
  ("town_11","Montréal", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(181.86,711.08),[], 240),                 #[swycartographr] prev. coords: (-98.63, -217.92) #[swycartographr] prev. coords: (180.44, 653.34) #[swycartographr] prev. coords: (90.52, 385.04)
  ("town_12","New Orleans", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-338.23,-399.43),[], 240),             #[swycartographr] prev. coords: (167.48, 63.26) #[swycartographr] prev. coords: (-195.63, -207.17)
  ("town_13","Cap-Français", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(679.87,-742.21),[],165),             #[swycartographr] prev. coords: (-126, 224) #[swycartographr] prev. coords: (381.92, -419.22)
  ("town_14","Saint Pierre", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1421.89,-831.1),[], 310),             #[swycartographr] prev. coords: (-322.63, 315.81)
#Spanish 3
  ("town_15","St. Augustine", icon_spanish_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(87.25,-275.05),[], 150),            #[swycartographr] prev. coords: (27.12, 46.9)
  ("town_16","Havana", icon_spanish_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.16,-709.39),[],75),                      #[swycartographr] prev. coords: (41, 170) #[swycartographr] prev. coords: (65.47, 152.73)
  ("town_17","Santo Domingo", icon_spanish_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(890.53,-762.02),[],270),            #[swycartographr] prev. coords: (-169, 253)
  ("town_18","Veracruz", icon_spanish_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(267.11,245.95),[], 60),    
  ("town_19","Ciudad de Mexico", icon_spanish_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(264.29,280.54),[], 135),       
#Iroquois 4
  ("town_20","Onondaga", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.93,532.95),[], 135),                   #[swycartographr] prev. coords: (-63.58, -178.92) #[swycartographr] prev. coords: (69.02, 297.49)
#Cherokee 5
  ("town_21","Chota", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.78,-2.85),[],120),                       #[swycartographr] prev. coords: (98.93, -51.41) #[swycartographr] prev. coords: (87.09, -43.59)
#Wabanaki 6
  ("town_22","Odanak", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280.86,806.72),[],270),                        #[swycartographr] prev. coords: (-146.43, -235.95)
#7 Nations 7
  ("town_23","Kahnawake", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(189.18,688.61),[],240),                         #[swycartographr] prev. coords: (-87.54, -180.58)
#Huron 8
  ("town_24","Sunyendeand", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.22,372.88),[],120),               #[swycartographr] prev. coords: (45.57, -147.54)
#Lenape 9
  ("town_25","Wyolutimunk", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.26,-158.59),[],225),                         
  ("town_26","Goschachgunk", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.24,283.76),[],225),                         #[swycartographr] prev. coords: (17.23, -130.05)
#Miami 10
  ("town_27","Kiikayonki", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-263.23,285.14),[],343),                          #[swycartographr] prev. coords: (99.87, -127.71)
#Shawnee 11 
  ("town_28","Sonnontio", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.03,254.35),[],225),                   #[swycartographr] prev. coords: (43.02, -95.58)
#Odawa 12
  ("town_29","Waawiyaatanong", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-136.04,419.71),[],281),                    #[swycartographr] prev. coords: (54.94, -163.04)
#Ojibwe 13
  ("town_30","Zhaagawaamikong", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-533.84,650.77),[],225),           #[swycartographr] prev. coords: (70.01, -241.71)
#Potawatomi 14
  ("town_31","Aniquiba", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-282.12,366.85),[],135),                      #[swycartographr] prev. coords: (57.28, -188.26)
#Choctaw 15
  ("town_32","Oklahannali", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-442.59,-216.13),[],225),              #[swycartographr] prev. coords: (168.87, -0.11)
#Chickasaw 16
  ("town_33","Chokkilissa", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-489.96,-140.58),[],225),              #[swycartographr] prev. coords: (172.06, -31.86)
#Creek 17
  ("town_34","Coweta", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-340,-202),[],315),
################SPACER#######################################
#FACTION ORDER Forts/Castles
#British 1
  ("castle_1","Fort Augusta, GA",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],50),
  ("castle_2","Fort Dobbs",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],75), 
  ("castle_3","Fort Edward, NS",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],100),             #[swycartographr] prev. coords: (-265.28, -205.88)
  ("castle_4","Fort Edward, NY",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],180),              
  ("castle_5","Fort Cumberland",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],90),            
  ("castle_6","Fort Lyttleton",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],55),             
  ("castle_7","Fort Augusta, PA",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],45),       
  ("castle_8","Fort George",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],30),             
  ("castle_9","Fort Loudon",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],100),                 #[swycartographr] prev. coords: (105.52, -50.93)
  ("castle_10","Fort Bedford",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],110),            
  ("castle_11","Fort Ligonier",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],75),             
  ("castle_12","Fort Prince George",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],95),            
  ("castle_13","Rogers' Island",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],115),             
  ("castle_14","Fort Seybert",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],90),            
  ("castle_15","Falmouth Fort",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],235),           #[swycartographr] prev. coords: (-187.74, -190.83)
  ("castle_16","Fort Anne",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],120),               #[swycartographr] prev. coords: (-246.38, -202.83)
  ("castle_17","Fort Number Four",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],120),      
  ("castle_18","Fort Gaspareaux",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],260),          #[swycartographr] prev. coords: (-263.57, -230.16)
  ("castle_19","Fort Beausejour",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[],80),          #[swycartographr] prev. coords: (-261.84, -223.78)
#French 2
  ("castle_20","Fort Rosalie",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],45),
  ("castle_21","Fort Saint-Jean-Baptiste",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],15),   #[swycartographr] prev. coords: (232.66, -19.62)
  ("castle_22","Fort Saint-Louis",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],300),           #[swycartographr] prev. coords: (196.52, -81.39)
  ("castle_23","Fort Vincennes",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],280),
  ("castle_24","Fort de Chartres",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],30),           #[swycartographr] prev. coords: (183.76, -58.51) #[swycartographr] prev. coords: (157.66, -46.31)
  ("castle_25","Fort Pontchartrain",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],90),             #[swycartographr] prev. coords: (56.64, -160.09)
  ("castle_26","Fort Duquesne",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],180),             
  ("castle_27","Fort Machault",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],80),          
  ("castle_28","Fort LeBoeuf",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],260),              
  ("castle_29","Fort Niagara",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],120),            
  ("castle_30","Fort Frontenac",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],260),   
  ("castle_31","Fort Levis",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],90),                
  ("castle_32","Fort Carillon",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],30),           
  ("castle_33","Fort Ile aux Noix",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],280),
  ("castle_34","Fort Saint-Jean",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],180),  
  ("castle_35","Fort Menagoueche",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],30),         #[swycartographr] prev. coords: (-224.36, -207.04)
  ("castle_36","Fort Louisbourg",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],180),     
  ("castle_37","Fort Conde",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],120),  
  ("castle_38","Fort Sainte-Claire",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],60),  
  ("castle_39","Fort Saint-Frederic",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],215),        
  ("castle_40","Fort Michillimackinac",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],10),         #[swycartographr] prev. coords: (85.77, -219.93)
  ("castle_41","Fort Miami",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],71),                  #[swycartographr] prev. coords: (112.96, -161.32)
  ("castle_42","Fort des Miamis",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],100),       
  ("castle_43","Fort Toulouse",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],120),             
  ("castle_44","Fort Tombecbee",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],120),        
  ("castle_45","Fort La Pointe",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],120),            #[swycartographr] prev. coords: (185.07, -244.24)
  ("castle_46","Fort Toronto",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],197),          
  ("castle_47","Fort Kaministiquia",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],120),            #[swycartographr] prev. coords: (180.64, -260.13)
  ("castle_48","Fort Saint Charles",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],120),        #[swycartographr] prev. coords: (228.06, -263.41)
  ("castle_49","Fort Bourbon",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],120),              #[swycartographr] prev. coords: (236.5, -303.69)
  ("castle_50","Fort Presque Isle",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],120),     
  ("castle_51","Fort Ouiatenon",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[],210),            #[swycartographr] prev. coords: (123.31, -120.24)
#Spanish 3
  ("castle_52","San Marcos",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[],15),                   #[swycartographr] prev. coords: (73.57, 49.34)
  ("castle_53","Pensacola",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[],260),               
  ("castle_54","El Castillo de la Inmaculada Concepción",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[],80),     #[swycartographr] prev. coords: (93.29, 348.43)
  ("castle_55","San Antonio",icon_brick_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[],15),                #[swycartographr] prev. coords: (290.02, 49.52) #[swycartographr] prev. coords: (277.65, 78.26)
  ("castle_56","San Juan de Ulúa",icon_stone_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[],280),        #[swycartographr] prev. coords: (274.84, 244)
  ("castle_57","San Diego",icon_brick_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[],80),                 #[swycartographr] prev. coords: (343.94, 281.35)
  ("castle_58","Castillo San Felipe del Morro",icon_brick_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[],15),
  ("castle_59","Castillo de San Pedro de la Roca",icon_brick_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[],15),
  ("castle_60","Fortaleza San Felipe",icon_brick_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[],60),
#Iroquois 4
  ("castle_61","Chenussio",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[],80),
  ("castle_62","Goiogouen",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[],40),
  ("castle_63","Kanonwalohale",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[],120),
  ("castle_64","Yoghroonwago",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[],120),
#Cherokee 5
  ("castle_65","Stecoa",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[],175),               
  ("castle_66","Cowee",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[],275),                
  ("castle_67","Hiwasee",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[],120),                #[swycartographr] prev. coords: (94.04, -41.27)
  ("castle_68","Chatuga",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[],200),                #[swycartographr] prev. coords: (100.72, -45.35)
#Wabanaki 6
  ("castle_69","Medoktak",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[],260),             #[swycartographr] prev. coords: (-210.53, -219.83) #[swycartographr] prev. coords: (-207.76, -227.78)
  ("castle_70","Mazipskoik",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[],80),         
  ("castle_71","Sipekni'katik",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[],260),   
  ("castle_72","Wolinak",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[],120),            
#Mohawk 7
  ("castle_73","Canohogo",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-155.00),[],260),
  ("castle_74","Kahnawake",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-155.00),[],55),         
#Huron 8
  ("castle_75","Lorette",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-125.00),[],120),          
#Lenape 9
  ("castle_76","Maughwawame",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-95.00),[],120),          
#Miami 10
#NO FORTS FOR MIAMI
#Shawnee 11 
  ("castle_77","Shenango",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-65.00),[],15),              
  ("castle_78","Moguck",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-65.00),[],270),    
  ("castle_79","Kentukee",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-65.00),[],120),
#Odawa 12
  ("castle_80","Waganagisi",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-50.00),[],162),            #[swycartographr] prev. coords: (95.19, -214.71)
#Ojibwe 13
  ("castle_81","Missinnihe",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-35.00),[],81),             
#Potawatomi 14 
  ("castle_82","Magnawauk",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-20.00),[],277),            #[swycartographr] prev. coords: (138.74, -176.41) #[swycartographr] prev. coords: (66.22, -179.37)
#Choctaw 15
  ("castle_83","Schakannapa",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[],190),               
  ("castle_84","Chickasawhay",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[],50),           
  ("castle_85","Sapatchito",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[],120), 
#Chickasaw 16
  ("castle_86","Apeony",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,10.00),[],120),              
  ("castle_87","Tchichatala",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,10.00),[],120),          
#Creek 17
  ("castle_88","Tukabatchee",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,25.00),[],60),
  ("castle_89","Kashita",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,25.00),[],50),                  #[swycartographr] prev. coords: (92.16, 36.74)
  ("castle_90","Abihika",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,25.00),[],115),                #[swycartographr] prev. coords: (110.39, 12.45)
  ("castle_91","Coosa",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,25.00),[],270),               
  ("castle_92","Tallapoosa",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,25.00),[],100),
  ###################################################### 
  #        
  #("castle_95","UNUSED FORT",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(322,14.79),[],120),          
  #("castle_96","UNUSED FORT",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(303.23,0.78),[],120),            
  #("castle_97","UNUSED FORT",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(320.76,-10.83),[],120),        
 # ("castle_98","UNUSED FORT",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(304.36,12.32),[],120),          
 # ("castle_99","UNUSED FORT",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(321.49,9.22),[],120),          
 # ("castle_100","UNUSED FORT",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(321.81,11.84),[],120),         
  #("castle_101","UNUSED FORT",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(321.33,-0.21),[],120),        

#FACTION ORDER villages
#British 1
("village_1", "Salem",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 100),            
("village_2", "Middleborough",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 110),      
("village_3", "Leicester",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 120),
("village_4", "Hatfield",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 130),
("village_5", "Providence",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),
("village_6", "Hartford",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 100),
("village_7", "New Haven",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 110),
("village_8", "Portsmouth",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 120),
("village_9", "Lyman",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 130),         
("village_10","Beaufort",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),
("village_11","Bennington",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 100),
("village_12","Albany",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 110),      
("village_13","Kingston",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 120),
("village_14","Morristown",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 130),         
("village_15","Hempstead",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),       
("village_16","Stamford",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),
("village_17","Monroe",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 35),
("village_18","Freehold",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),
("village_19","Reading",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),    
("village_20","Dover",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),
("village_21","Baltimore",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 100),
("village_22","York",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 110),
("village_23","Cambridge",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 120),
("village_24","Alexandria",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 130),
("village_25","Williamsburg",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),
("village_26","Fredericksburg",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),
("village_27","Richmond",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),
("village_28","Norfolk",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),
("village_29","Georgetown",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),
("village_30","Falmouth",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),
("village_31","New Bern",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 100),
("village_32","Wilmington",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 110),
("village_33","Savannah",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 120),
("village_34","Orangeburg",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 130),
("village_35","Easton",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),  
("village_36","Lancaster",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),    
("village_37","Raystown",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),      
("village_38","Long Canes",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),           
("village_39","Lunenburg",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 170),        #[swycartographr] prev. coords: (-265.23, -195.85)
("village_40","Iredell",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 100),            #[swycartographr] prev. coords: (5.94, -60.13)
("village_41","Augusta",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 200),
("village_42","Cumberland",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 200),    
("village_43","Sunbury",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 200),     
("village_44","Eleuthera",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 95),         #[swycartographr] prev. coords: (-70, 146)
("village_45","Long Island",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 35),
("village_46","Turks and Caicos",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 60), #[swycartographr] prev. coords: (-138, 192)
("village_47","Andros",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 20),               #[swycartographr] prev. coords: (-33.78, 145.83)
("village_48","Spanish Town",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 240),          #[swycartographr] prev. coords: (-47, 261.13)
("village_49","Montego Bay",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 50),         #[swycartographr] prev. coords: (-34.81, 250.52) #[swycartographr] prev. coords: (-35.95, 253.74)
("village_50","Annapolis Royal",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 90),           #[swycartographr] prev. coords: (-244.85, -200.82)
("village_51","Canso",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 180),  
("village_52","Belize",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 0),
("village_53", "Carlisle",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 60),       
("village_54", "Aughwick",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 180),    
("village_55", "Bristol",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 120),    

#French 2
("village_56","La Balize",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 170),          
("village_57","Cap Girardeau",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 10),      #[swycartographr] prev. coords: (181.05, -56.84) #[swycartographr] prev. coords: (156.56, -37.99)
("village_58","Bonne Terre",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 170),        #[swycartographr] prev. coords: (204.8, -52.92)
("village_59","Tadoussac",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 170),        
("village_60","Aubigny",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 170),  
("village_61","Prairie du Pont",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 120),       #[swycartographr] prev. coords: (191.33, -60.64) #[swycartographr] prev. coords: (161.62, -43.75)
("village_62","St. Philippe",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 130),      #[swycartographr] prev. coords: (183.51, -67.28)
("village_63","Terre Haute",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 170),   
("village_64","Cahokia",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100),            #[swycartographr] prev. coords: (191.23, -69.93) #[swycartographr] prev. coords: (159.35, -51.59)
("village_65","Pointe Sainte-Anne",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100),     #[swycartographr] prev. coords: (-216.53, -215.83)
("village_66","Saint-Jean-sur-Richelieu",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100), 
("village_67","Saint-Paul-de-l'Ile-aux-Noix",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100),
("village_68","Longueuil",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100),        
("village_69","Grand Pre",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100),       #[swycartographr] prev. coords: (-261.98, -207.23)
("village_70","Miramichy",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100),       #[swycartographr] prev. coords: (-257.14, -245.93)
("village_71","Saint-Hyacinthe",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100),    
("village_72","Cobeguit",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 20),        
("village_73","Trois-Rivières",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100),   
("village_74","Basseville",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 15),     
("village_75","Les Cayes",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 15),        
("village_76","Port-au-Prince",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 90),     
("village_77","Môle-Saint-Nicolas",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 180), 
("village_78","Pointe-a-Pitre",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 180),  
("village_79","Roseau",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 0),         
("village_80","Beaubassin",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 40),       #[swycartographr] prev. coords: (-262.63, -219.98)
("village_81","Porte-la-Joye",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 20), 
("village_82","Niganiche",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 60),    
("village_83","Port Toulouse",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 80),  
("village_84","Biloxi",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 110),                
("village_85","Mobile",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 120),               
("village_86","Baton Rouge",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 130),                 
("village_87","Cote des Allemands",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 170),
#Spanish 3    
("village_88","Puerto Principe",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 40),             
("village_89","Santa Rosa",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 20),              #[swycartographr] prev. coords: (310.8, 94.79) #[swycartographr] prev. coords: (283.76, 99.01)
("village_90","Tampico",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 60),               #[swycartographr] prev. coords: (310.23, 191.53) #[swycartographr] prev. coords: (250.46, 222.15)
("village_91","Panuco",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 55),                  #[swycartographr] prev. coords: (316.06, 200.5) #[swycartographr] prev. coords: (256.48, 236.52)
("village_92","Puebla",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 15),                 #[swycartographr] prev. coords: (311.92, 251.15)
("village_93","Oaxaca",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 10),            #[swycartographr] prev. coords: (300.97, 273.85)
("village_94","Ciudad Real",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 35),     
("village_95","Campeche",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 160),             
("village_96","Merida",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 180),           #[swycartographr] prev. coords: (171.97, 204.19)
("village_97","Puerto Cortes",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 40),         
("village_98","Trujillo",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 20),          #[swycartographr] prev. coords: (103.19, 293.98)
("village_99","Bayamo",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 10),            #[swycartographr] prev. coords: (-53, 217)
("village_100","Trinidad",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 35),            #[swycartographr] prev. coords: (2, 192)
("village_101","Santiago de Cuba",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 160),             
("village_102","Puerto Plata",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 90),   
("village_103","Santiago de los Caballeros",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 220),
("village_104","San Juan",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 180),        #[swycartographr] prev. coords: (-238.58, 251.53)
########## BREAK IN FACTION ORDER FOR VILLAGE ASSIGNMENT
#British 1.1
("village_105", "Gnaddenhutten",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-200.00),[], 100), #Native
#French 2.1
("village_106","Natchitoches",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 170),      #Native #[swycartographr] prev. coords: (221.51, -1.5)
("village_107","Natchez",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 170),           #Native
("village_108","Kaskaskia",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100),       #Native  #[swycartographr] prev. coords: (186.97, -64.71) #[swycartographr] prev. coords: (168.01, -49.33)
("village_109","La Presentation",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 43), #Native        
("village_110","Oswegatchie",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 170),    #Native
("village_111","Mandan",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 170),         #Native #[swycartographr] prev. coords: (256.97, -261.92)
("village_112","Venango",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100),          #Native
("village_113","Cataraqui",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-260.00),[], 100),      #Native
#Spanish 3.1
("village_114","Jinotega",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 10),         #Native   #[swycartographr] prev. coords: (113.92, 344.29)
("village_115","Calusa",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 35),            #Native            #[swycartographr] prev. coords: (25.37, 125.42)
("village_116","Tocobaga",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 160),           #Native          #[swycartographr] prev. coords: (49.8, 91.96)
("village_117","Apalachee",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 180),         #Native            
("village_118","Panzacola",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-320.00),[], 0),          #Native
#Iroquois 4
("village_119","Erie",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 55),                 
("village_120","Canawaugus",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 60),           
("village_121","Ganondagan",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 55),         
("village_122","Cayuga",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 172),       
("village_123","Susquehanna",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 150),   
("village_124","Tuscarora",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 120),   
("village_125","Oneida",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 100),               
("village_126","Canadasegy",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 120), 
("village_127","Oriskany",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 100), 
("village_128","Onnontare",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 210),
("village_129","Koshaksink",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 300),       
("village_130","Ononowaga Cochake",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 10),  
("village_131","Ononowaga Kuskusky",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 160), 
("village_132","Oweso'gawenoeh",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-170.00),[], 220),   
#Cherokee 5
("village_133","Nununyi",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[], 15),        
("village_134","Tuckaseegee",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[], 10),       
("village_135","Etchoe",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[], 35),          
("village_136", "Estatoe",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[], 90),       
("village_137", "Cattoogachaye",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[], 150),           #[swycartographr] prev. coords: (87.92, -38.51)
("village_138", "Aquonatuste",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[], 200),     #[swycartographr] prev. coords: (87.77, -43.8)
("village_139", "Little Tellico",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[], 200),   #[swycartographr] prev. coords: (86.49, -48.28)
("village_140", "Mialoquo",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[], 100),       #[swycartographr] prev. coords: (107.38, -53.5) #[swycartographr] prev. coords: (110.57, -51.26)
("village_141", "Citico",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-110.00),[], 100),           #[swycartographr] prev. coords: (88.93, -52) #[swycartographr] prev. coords: (90.5, -49.86)
#Wabanaki 6                           
("village_142","Woronoke",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[], 35),         
("village_143","Nanrantsouak",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[], 160),              #[swycartographr] prev. coords: (-188.21, -206.07)
("village_144","Aukpaque",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[], 40),        #[swycartographr] prev. coords: (-212.79, -217.37) #[swycartographr] prev. coords: (-221.26, -211.38)
("village_145","Shubenacadie",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[], 135),  
("village_146","Passamaquoddy",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[], 100),   #[swycartographr] prev. coords: (-213.12, -202.6)
("village_147","Pijelooeekak",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[], 100),   #[swycartographr] prev. coords: (-263.06, -194.63)
("village_148","Sokoki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[], 100),       
("village_149","Madawaska",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[], 100),      #[swycartographr] prev. coords: (-192.25, -224.53)
("village_150","Alenape Meneha",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-140.00),[], 100),  #[swycartographr] prev. coords: (-202.68, -207.33) #[swycartographr] prev. coords: (-198.9, -217.98)
#Mohawk 7
("village_151","Kanien'keha:ka",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-155.00),[], 150),
("village_152","Tarajorees",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-155.00),[], 200),    
("village_153","Canajoharie",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-155.00),[], 40),
("village_154","Ganienkeh",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-155.00),[], 120),    
("village_155","Ahkwesahsne",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-155.00),[], 200),   
("village_156","Kanesatake",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-155.00),[], 200),    
("village_157","Atheclaghque",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-155.00),[], 200),  
#Huron 8
("village_158","Ancienne Lorette",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-125.00),[], 200), 
("village_159","Magagua",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-125.00),[], 305),          #[swycartographr] prev. coords: (57.93, -165.17)
("village_160","Anderdon",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-125.00),[], 200),          #[swycartographr] prev. coords: (55.96, -155.35)
("village_161","Junundat",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-125.00),[], 200),      
("village_162","Jejakweyandat",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-125.00),[], 200),  
("village_163","Jejakwe",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-125.00),[], 200),       
("village_164","Ouadot Muskingum",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-125.00),[], 200),  
("village_165","Conchake",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-125.00),[], 100),         
("village_166","Kuskuskyandat",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-125.00),[], 50),    
#Lenape 9
("village_167", "Chugnut",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-95.00),[], 200),      
("village_168", "Owego",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-95.00),[], 40),         
("village_169", "Sheshequenink",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-95.00),[], 90),            
("village_170", "Indaochaic",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-95.00),[], 160),     
("village_171", "Muhheconneokink",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-95.00),[], 200),      
("village_172", "Sawcunk",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-95.00),[], 40),        
("village_173", "Gekelmukpechunk",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-95.00),[], 90),             
("village_174", "Wappocomo",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-95.00),[], 160),  
("village_175", "Kuskuskink",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-95.00),[], 160),    
#Miami 10
("village_176","Saakiiweeyonki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-80.00),[], 322),   #[swycartographr] prev. coords: (114.92, -149.09)
("village_177","Mihsiiwiateehi",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-80.00),[], 170),  #[swycartographr] prev. coords: (110.27, -150.75)
("village_178","Kineepikomeehkwa",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-80.00),[], 160),  #[swycartographr] prev. coords: (119.18, -117.89)
("village_179","Kiteepihkwana",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-80.00),[], 173),   #[swycartographr] prev. coords: (129.68, -111.86)
("village_180","Waayaahtanonki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-80.00),[], 223), 
("village_181","Peeyankihsionki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-80.00),[], 335),  #[swycartographr] prev. coords: (140.64, -102.89)
("village_182","Aciipihkahkionki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-80.00),[], 160),  #[swycartographr] prev. coords: (154.94, -85.05)
("village_183","Pinkwaawilenionki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-80.00),[], 160),
#Shawnee 11 
("village_184","Kuskusky",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-65.00),[], 120),      
("village_185","Nonhelemah",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-65.00),[], 100),           
("village_186","Kispoko",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-65.00),[], 110),               #[swycartographr] prev. coords: (43.43, -105.44)
("village_187","Shannoah",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-65.00),[], 120),          #[swycartographr] prev. coords: (56.03, -105.76)
("village_188","Shinoudaista",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-65.00),[], 100),         
("village_189","Eskippakithiki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-65.00),[], 110),      
("village_190","Chilliocothe",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-65.00),[], 120),        
#Odawa 12
("village_191","Manidoowaling",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-50.00),[], 160),    
("village_192","Ahnumawautinkumig",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-50.00),[], 246), #[swycartographr] prev. coords: (99.1, -213.76) #[swycartographr] prev. coords: (78.54, -196.76)
("village_193","Ahptunwating",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-50.00),[], 166),    #[swycartographr] prev. coords: (102.69, -210.87)
("village_194","Wabigungweshcupago",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-50.00),[], 160),  #[swycartographr] prev. coords: (114.41, -181.93)
("village_195","Shingobeeng",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-50.00),[], 160),    
("village_196","Owashtanong",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-50.00),[], 227),      #[swycartographr] prev. coords: (104.96, -153.8)
("village_197","Maamii",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-50.00),[], 160),         
("village_198","Ogantz",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-50.00),[], 160),      
#Ojibwe 13 
("village_199","Gichiziibiwininiwag",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-35.00),[], 20),         #[swycartographr] prev. coords: (252.5, -254.7)
("village_200","Gichigamiing",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-35.00),[], 60),        #[swycartographr] prev. coords: (191.24, -256.76)
("village_201","Baawiting",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-35.00),[], 55),        #[swycartographr] prev. coords: (90.13, -235.24)
("village_202","Zaaga'iganing",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-35.00),[], 15),       #[swycartographr] prev. coords: (196.88, -221.38)
("village_203","Sagenong",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-35.00),[], 10),  
("village_204","Cobechenonk",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-35.00),[], 35),        
("village_205","Mekisewancenonk",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-35.00),[], 160), 
#Potawatomi 14
("village_206","Kwikwiyak",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-20.00),[], 62),        #[swycartographr] prev. coords: (135.04, -204.52)
("village_207","Wnaneg-gizs",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-20.00),[], 160),     #[swycartographr] prev. coords: (149.7, -192.42)
("village_208","Zhegagoynak",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-20.00),[], 127),     #[swycartographr] prev. coords: (135.51, -155.11) #[swycartographr] prev. coords: (64.48, -175.73)
("village_209","Sheggwe",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-20.00),[], 353),         #[swycartographr] prev. coords: (100.96, -147.18)
("village_210","Nadowesippi",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-20.00),[], 160),      #[swycartographr] prev. coords: (91.25, -159.01)
("village_211","Wawiatenang",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-20.00),[], 64),      #[swycartographr] prev. coords: (62.15, -160.16)
#Choctaw 15
("village_212","Yowannis",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[], 135),           
("village_213","Yashu Iskitini",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[], 180),    
("village_214","Oaka Loosa",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[], 200), 
("village_215","Louckata",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[], 135),           
("village_216","Abeka",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[], 120),              
("village_217","Ayanabi",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[], 40),             
("village_218","Bouctoucoulou",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[], 300),     
("village_219","Cuctachas",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[], 200),            
("village_220","Mongoulacha",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[], 70),          #[swycartographr] prev. coords: (152.08, 3.02)
("village_221","Concha",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[], 200),           
("village_222","Pante",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,-5.00),[], 70),           
#Chickasaw 16
("village_223","Tchokaffala",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,10.00),[], 70),       
("village_224","Tchikoulechasto",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,10.00),[], 70),  
("village_225","Falatchao",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,10.00),[], 70),        
("village_226","Chatelaw",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,10.00),[], 70),         
#Creek 17
("village_227","Tokepahce",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,25.00),[], 50),              
("village_228","Cusseta",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,25.00),[], 110),                #[swycartographr] prev. coords: (92.26, 34.28)
("village_229","Talladega",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,25.00),[], 120),         #[swycartographr] prev. coords: (105.83, 8.25)
("village_230","Etowah",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,25.00),[], 20),            
("village_231","Cahawba",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,25.00),[], 80), 
("village_232","Okfuskee",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-450.00,25.00),[], 135),

#nonexistant villages
("village_a","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(94.38,-309.23),[], 135),        #[swycartographr] prev. coords: (233.91, -303.32)
("village_b","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81.84,-272.61),[], 135),        #[swycartographr] prev. coords: (180.57, -262.31)
("village_c","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.97,-213.87),[], 135),        #[swycartographr] prev. coords: (85.12, -217.36)
("village_d","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.39,-189.69),[], 135),        #[swycartographr] prev. coords: (112.68, -163.92)
("village_e","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.6,-133.12),[], 135),       
("village_f","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.28,-248.81),[], 135),        #[swycartographr] prev. coords: (188.59, -244.24)
("village_g","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.42,-118.04),[], 135),      
("village_h","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.97,-118.91),[], 135),      
("village_i","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.15,-139.26),[], 135),      
("village_j","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.03,-153.59),[], 135),      
("village_k","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.84,-157.11),[], 135),        #[swycartographr] prev. coords: (59.2, -157.71)
("village_l","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.03,-23.55),[], 135),         #[swycartographr] prev. coords: (106.06, -47.05)
("village_m","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.34,-174.53),[], 135),     
("village_n","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(121.17,-110.94),[], 135),       #[swycartographr] prev. coords: (123.72, -122.8)
("village_o","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.32,-157.97),[], 135),        
("village_p","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.86,-205.89),[], 135),     
("village_q","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.86,-91.67),[], 135),       
("village_r","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(155.8,-422.55),[], 135),       #[swycartographr] prev. coords: (349.96, -349.26) #[swycartographr] prev. coords: (345.23, -425.22) #[swycartographr] prev. coords: (288.59, -423.39)
("village_s","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.98,11.99),[], 135),      

###################################
 
  #Guerre en Amerique microfactions! start
  #Guerre en Amerique forts
  ("fort_1","Moose Factory",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.37,987.97),[],165), #Hudson Bay Company  #[swycartographr] prev. coords: (18.78, -330.01) #[swycartographr] prev. coords: (-579.83, 1258.58) #[swycartographr] prev. coords: (-153.26, 592.6)
  ("fort_2","Philipsburg",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-288.56,256.54),[],165), #Dutch 
  ("fort_3","Fort La Reine",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.09,-290.24),[],165), #Coureurs des Bois  #[swycartographr] prev. coords: (238.19, -281.42)
  ("fort_4","Boston Common",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.89,-159.44),[],165), #Sons of Liberty 
  ("fort_5","Limbé",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(732.14,-747.41),[],165), #Maroons  #[swycartographr] prev. coords: (747.91, -756.72) #[swycartographr] prev. coords: (255.07, -425.46)
  ("fort_6","Misipawistik",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.91,-326.39),[],165), #Cree  #[swycartographr] prev. coords: (215.14, -325.19)
  ("fort_7","Kitcispirini",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.93,-219.34),[],165), #Algonkin 
  ("fort_8","Whahktukuk",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.41,-163.39),[],165), #Mohican 
  ("fort_9","Nassaw-Weyapee",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.64,-61.3),[],165), #Catawba 
  ("fort_10","Grand Inagua",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.08,206.56),[],165), #West Indies Assassins
  ("fort_11","Davenport Homestead",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159.66,-166.87),[],165), #American Assassins 
  ("fort_12","Fort Arsenal",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.08,-144.21),[],165), #Templars  
  #Guerre en Amerique microfactions! end
  
  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(699.59,-1689.7),[], 100),  #[swycartographr] prev. coords: (280, -310) #[swycartographr] prev. coords: (107.52, -312.72)
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(703.01,-1688.17),[], 100),  #[swycartographr] prev. coords: (280, -310) #[swycartographr] prev. coords: (92.21, -297.71)
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.99,-297.96),[], 100),  #[swycartographr] prev. coords: (280, -310)
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("dhorak_keep","Dhorak_Keep",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 

  ("training_ground_1", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("training_ground_2", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("training_ground_3", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("training_ground_4", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("training_ground_5", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(34, -114),[(trp_looter,15,0)]), #not enabled
  ("seto_pirate_spawn_point"  ,"The Caribbean",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-106.07,207.37),[(trp_looter,15,0)]), #[swycartographr] prev. coords: (-107.07, 205.16)
  ("kanto_rebel_spawn_point"   ,"Ohio River Valley",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(78.33,-94.76),[(trp_looter,15,0)]), 
  ("shinano_rebel_spawn_point"  ,"Appalachia",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(10.28,-89.62),[(trp_looter,15,0)]),  
  ("woku_pirate_spawn_point" ,"Acadia",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-234.8,-219.25),[(trp_looter,15,0)]),  
  ("kinai_rebel_spawn_point"   ,"Basse Louisiane",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(177.59,12.39),[(trp_looter,15,0)]), 
  ("monk_rebel_spawn_point"   ,"Great Plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(132.81,-90.82),[(trp_looter,15,0)]),  #[swycartographr] prev. coords: (205.57, -144.73)
  ("northern_raider_spawn_point"  ,"Algonquin",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-54.84,-223.06),[(trp_looter,15,0)]),  
  
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(92.55,-297.96),[(trp_looter,15,0)]), #[swycartographr] prev. coords: (280, -310)
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(280,-310),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(280,-310),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(280,-310),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(280,-310),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(280,-310),[(trp_looter,15,0)]),
  ]
  
# modmerger_start version=201 type=2
try:
    component_name = "parties"
    var_set = { "parties" : parties }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
