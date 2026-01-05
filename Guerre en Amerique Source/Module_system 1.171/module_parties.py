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
  ("zendar","Zendar",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[]),
#FACTION ORDER Towns/Cities
#British 1
  ("town_1","Halifax", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-270,-199.24),[], 170),                      
  ("town_2","Boston", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.2,-161.29),[], 290),                          
  ("town_3","Newport", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-148.5,-148.41),[], 120),
  ("town_4","New York", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.82,-140.44),[], 170),             
  ("town_5","Philadelphia", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.53,-117.76),[], 80),             
  ("town_6","Charlestowne", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.05,3.11),[], 90),                          
  ("town_7","Nassau", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.85,136.18),[],165),                         
  ("town_8","Kingston", icon_british_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.07,259.53),[],195),  
#French 2
  ("town_9","Louisbourg", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-336.21,-223.4),[],225),  
  ("town_10","Québec", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-171,-260.21),[], 155),
  ("town_11","Montréal", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.63,-217.92),[], 240),
  ("town_12","New Orleans", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(167.48,63.26),[], 240),        
  ("town_13","Cap-Français", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-126,224),[],165),
  ("town_14","Saint Pierre", icon_french_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-322.63,315.81),[], 310),
#Spanish 3
  ("town_15","St. Augustine", icon_spanish_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.12,46.9),[], 150),
  ("town_16","Havana", icon_spanish_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41,170),[],75),
  ("town_17","Santo Domingo", icon_spanish_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-169,253),[],270),
  ("town_18","Veracruz", icon_spanish_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(267.11,245.95),[], 60),    
  ("town_19","Ciudad de Mexico", icon_spanish_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(338.89,240.34),[], 135),
#Iroquois 4
  ("town_20","Onondaga", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.58,-178.92),[], 135),
#Cherokee 5
  ("town_21","Chota", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.93,-51.41),[],120),                      
#Wabanaki 6
  ("town_22","Odanak", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-146.43,-235.95),[],270),                       
#Mohawk 7
  ("town_23","Nowdaga", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.54,-180.58),[],240),                        
#Huron 8
  ("town_24","Sunyendeand", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.57,-147.54),[],120),              
#Lenape 9
  ("town_25","Wyolutimunk", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.26,-158.59),[],225),                         
  ("town_26","Goschachgunk", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.23,-130.05),[],225),                        
#Miami 10
  ("town_27","Kiikayonki", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.87,-127.71),[],343),                         
#Shawnee 11 
  ("town_28","Sonnontio", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.02,-95.58),[],225),                  
#Odawa 12
  ("town_29","Waawiyaatanong", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.94,-163.04),[],281),                   
#Ojibwe 13
  ("town_30","Zhaagawaamikong", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(189.27,-239.47),[],225),        
#Potawatomi 14
  ("town_31","Aniquiba", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.13,-155.88),[],135),                         
#Choctaw 15
  ("town_32","Oklahannali", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(168.87,-0.11),[],225),  
#Chickasaw 16
  ("town_33","Chokkilissa", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(172.06,-31.86),[],225),             
#Creek 17
  ("town_34","Coweta", icon_native_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.6,4.41),[],315),
################SPACER#######################################
#FACTION ORDER Forts/Castles
#British 1
  ("castle_1","Fort Augusta, GA",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.17,-16.55),[],50),
  ("castle_2","Fort Dobbs",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.4,-57.55),[],75), 
  ("castle_3","Fort Edward, NS",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-265.28,-205.88),[],100),            
  ("castle_4","Fort Edward, NY",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.78,-186.89),[],180),              
  ("castle_5","Fort Cumberland",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.13,-105.46),[],90),            
  ("castle_6","Fort Lyttleton",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.12,-122.91),[],55),             
  ("castle_7","Fort Augusta, PA",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.71,-137.88),[],45),       
  ("castle_8","Fort George",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-103.38,-140.65),[],30),             
  ("castle_9","Fort Loudon",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.52,-50.93),[],100),              
  ("castle_10","Fort Bedford",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.38,-121.59),[],110),            
  ("castle_11","Fort Ligonier",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.64,-121.48),[],75),             
  ("castle_12","Fort Prince George",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.54,-36.21),[],95),            
  ("castle_13","Rogers' Island",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.29,-186.33),[],115),             
  ("castle_14","Fort Seybert",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.92,-93.55),[],90),            
  ("castle_15","Falmouth Fort",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-187.74,-190.83),[],235),
  ("castle_16","Fort Anne",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-246.38,-202.83),[],120),              
  ("castle_17","Fort Number Four",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-138.07,-180.87),[],120),      
  ("castle_18","Fort Gaspareaux",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-263.57,-230.16),[],260),         
  ("castle_19","Fort Beausejour",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-261.84,-223.78),[],80), 
#French 2
  ("castle_20","Fort Rosalie",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(197.61,-0.55),[],45),
  ("castle_21","Fort Saint-Jean-Baptiste",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(232.66,-19.62),[],15),
  ("castle_22","Fort Saint-Louis",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(196.52,-81.39),[],300),         
  ("castle_23","Fort Vincennes",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.52,-107.16),[],280),
  ("castle_24","Fort de Chartres",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(183.76,-58.51),[],30),          
  ("castle_25","Fort Pontchartrain",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.64,-160.09),[],90),            
  ("castle_26","Fort Duquesne",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.51,-120.52),[],180),             
  ("castle_27","Fort Machault",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.43,-147.44),[],80),          
  ("castle_28","Fort LeBoeuf",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.14,-155.9),[],260),              
  ("castle_29","Fort Niagara",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.1,-177.45),[],120),            
  ("castle_30","Fort Frontenac",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.71,-200.38),[],260),   
  ("castle_31","Fort Levis",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.21,-207.81),[],90),                
  ("castle_32","Fort Carillon",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-109.72,-198.24),[],30),           
  ("castle_33","Fort Ile aux Noix",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-115.51,-213.06),[],280),
  ("castle_34","Fort Saint-Jean",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-124.31,-219.23),[],180),  
  ("castle_35","Fort Menagoueche",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-224.36,-207.04),[],30), 
  ("castle_36","Fort Louisbourg",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-334.35,-222.6),[],180),     
  ("castle_37","Fort Conde",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(143.76,37.1),[],120),  
  ("castle_38","Fort Sainte-Claire",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121.04,250.61),[],60),  
  ("castle_39","Fort Saint-Frederic",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.4,-203.93),[],215),        
  ("castle_40","Fort Michillimackinac",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.77,-219.93),[],10),        
  ("castle_41","Fort Miami",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.96,-161.32),[],71),           
  ("castle_42","Fort des Miamis",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.51,-131.07),[],100),       
  ("castle_43","Fort Toulouse",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.87,9.88),[],120),             
  ("castle_44","Fort Tombecbee",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(149.45,11.27),[],120),        
  ("castle_45","Fort La Pointe",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(185.07,-244.24),[],120), 
  ("castle_46","Fort Toronto",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.03,-187.41),[],197),          
  ("castle_47","Fort Kaministiquia",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(180.64,-260.13),[],120),           
  ("castle_48","Fort Saint Charles",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(228.06,-263.41),[],120),   
  ("castle_49","Fort Bourbon",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(236.5,-303.69),[],120),           
  ("castle_50","Fort Presque Isle",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.07,-160.7),[],120),     
  ("castle_51","Fort Ouiatenon",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(123.31,-120.24),[],210), 
#Spanish 3
  ("castle_52","San Marcos",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.57,49.34),[],15),
  ("castle_53","Pensacola",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.2,42.76),[],260),               
  ("castle_54","El Castillo de la Inmaculada Concepción",icon_wood_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.29,348.43),[],80),    
  ("castle_55","San Antonio",icon_brick_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(290.02,49.52),[],15),
  ("castle_56","San Juan de Ulúa",icon_stone_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(274.84,244),[],280),
  ("castle_57","San Diego",icon_brick_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(343.94,281.35),[],80),
  ("castle_58","Castillo San Felipe del Morro",icon_brick_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-241.24,252.05),[],15),
  ("castle_59","Castillo de San Pedro de la Roca",icon_brick_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70,223),[],15),
  ("castle_60","Fortaleza San Felipe",icon_brick_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161,227),[],60),
#Iroquois 4
  ("castle_61","Chenussio",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.15,-172.55),[],80),
  ("castle_62","Goiogouen",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.63,-173.35),[],40),
  ("castle_63","Kanonwalohale",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.88,-189.34),[],120),
  ("castle_64","Yoghroonwago",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.92,-162.02),[],120),
#Cherokee 5
  ("castle_65","Stecoa",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.35,-58.96),[],175),               
  ("castle_66","Cowee",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.45,-54.59),[],275),                
  ("castle_67","Hiwasee",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(94.04,-41.27),[],120),              
  ("castle_68","Chatuga",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(100.72,-45.35),[],200),          
#Wabanaki 6
  ("castle_69","Medoktak",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210.53,-219.83),[],260),            
  ("castle_70","Mazipskoik",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.45,-209.73),[],80),         
  ("castle_71","Sipekni'katik",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-283.94,-216.75),[],260),   
  ("castle_72","Wolinak",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-160.34,-244.55),[],120),            
#Mohawk 7
  ("castle_73","Canohogo",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.41,-197.67),[],260),
  ("castle_74","Kahnawake",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.19,-208.38),[],55),         
#Huron 8
  ("castle_75","Lorette",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-164.35,-256.89),[],120),          
#Lenape 9
  ("castle_76","Maughwawame",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.03,-125.56),[],120),          
#Miami 10
#NO FORTS FOR MIAMI
#Shawnee 11 
  ("castle_77","Shenango",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.33,-124.03),[],15),              
  ("castle_78","Moguck",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.33,-113.87),[],270),    
  ("castle_79","Kentukee",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.37,-82.31),[],120),
#Odawa 12
  ("castle_80","Waganagisi",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95.19, -214.71),[],162),           
#Ojibwe 13
  ("castle_81","Missinnihe",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.11, -180.5),[],81),             
#Potawatomi 14 
  ("castle_82","Magnawauk",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(138.74, -176.41),[],277),           
#Choctaw 15
  ("castle_83","Schakannapa",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154.98,-5.61),[],190),               
  ("castle_84","Chickasawhay",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(149.94,15.63),[],50),           
  ("castle_85","Sapatchito",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(178.93,-0.34),[],120), 
#Chickasaw 16
  ("castle_86","Apeony",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(158.66,-19.52),[],120),              
  ("castle_87","Tchichatala",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(173.26,-24.28),[],120),          
#Creek 17
  ("castle_88","Tukabatchee",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.9,-4.64),[],60),
  ("castle_89","Kashita",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.16,36.74),[],50),
  ("castle_90","Abihika",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.39,12.45),[],115),        
  ("castle_91","Coosa",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.24,-13.31),[],270),               
  ("castle_92","Tallapoosa",icon_native_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.96,12.21),[],100),
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
("village_1", "Salem",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.04,-164.51),[], 100),            
("village_2", "Middleborough",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-160.53,-156.51),[], 110),      
("village_3", "Leicester",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143.71,-164.9),[], 120),
("village_4", "Hatfield",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.19,-165.41),[], 130),
("village_5", "Providence",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-149.55,-153.49),[], 170),
("village_6", "Hartford",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-134.23,-156.88),[], 100),
("village_7", "New Haven",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123.92,-146.13),[], 110),
("village_8", "Portsmouth",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.84,-177.29),[], 120),
("village_9", "Lyman",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140.7,-193.11),[], 130),         
("village_10","Beaufort",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8,7),[], 170),
("village_11","Bennington",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.84,-176.21),[], 100),
("village_12","Albany",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.78,-170.3),[], 110),      
("village_13","Kingston",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.52,-161.26),[], 120),
("village_14","Morristown",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.45,-139.79),[], 130),         
("village_15","Hempstead",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-115.03,-137.38),[], 170),       
("village_16","Stamford",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.66,-170.5),[], 170),
("village_17","Monroe",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.12,-118.1),[], 35),
("village_18","Freehold",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.83,-129.38),[], 170),
("village_19","Reading",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.95,-128.68),[], 170),    
("village_20","Dover",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.95,-106.2),[], 170),
("village_21","Baltimore",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.76,-103.52),[], 100),
("village_22","York",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.36,-115.06),[], 110),
("village_23","Cambridge",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.28,-92.33),[], 120),
("village_24","Alexandria",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.25,-94.1),[], 130),
("village_25","Williamsburg",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.15,-75.1),[], 170),
("village_26","Fredericksburg",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.52,-84.92),[], 170),
("village_27","Richmond",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.4,-75.15),[], 170),
("village_28","Norfolk",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.03,-65.39),[], 170),
("village_29","Georgetown",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.29,-12.09),[], 170),
("village_30","Falmouth",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-179.8,-190.2),[], 170),
("village_31","New Bern",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.84,-33.09),[], 100),
("village_32","Wilmington",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-20.4,-17.19),[], 110),
("village_33","Savannah",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.22,10.56),[], 120),
("village_34","Orangeburg",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.3,-14.7),[], 130),
("village_35","Easton",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.26,-128.83),[], 170),  
("village_36","Lancaster",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.93,-117.59),[], 170),    
("village_37","Raystown",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.53,-124.36),[], 170),      
("village_38","Long Canes",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.07,-27.61),[], 170),           
("village_39","Lunenburg",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-265.23,-195.85),[], 170),       
("village_40","Iredell",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.94,-60.13),[], 100),
("village_41","Augusta",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39,-13),[], 200),
("village_42","Cumberland",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.62,-101.88),[], 200),    
("village_43","Sunbury",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.84,-138.08),[], 200),     
("village_44","Eleuthera",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70,146),[], 95),
("village_45","Long Island",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81,167),[], 35),
("village_46","Turks and Caicos",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-138,192),[], 60),
("village_47","Andros",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.78,145.83),[], 20),              
("village_48","Spanish Town",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47,261.13),[], 240),         
("village_49","Montego Bay",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.81,250.52),[], 50),        
("village_50","Annapolis Royal",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-244.85,-200.82),[], 90),          
("village_51","Canso",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-316.08,-212.66),[], 180),  
("village_52","Belize",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140.49,268.21),[], 0),
("village_53", "Carlisle",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.39,-126.64),[], 60),       
("village_54", "Aughwick",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.77,-125.03),[], 180),    
("village_55", "Bristol",  icon_british_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.22,-122.52),[], 120),    

#French 2
("village_56","La Balize",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(162.11,65.5),[], 170),          
("village_57","Cap Girardeau",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(181.05,-56.84),[], 10),  
("village_58","Bonne Terre",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(204.8,-52.92),[], 170),   
("village_59","Tadoussac",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-191.37,-278.04),[], 170),        
("village_60","Aubigny",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-175.43,-256.11),[], 170),  
("village_61","Prairie du Pont",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(191.33,-60.64),[], 120),      
("village_62","St. Philippe",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(183.51,-67.28),[], 130),   
("village_63","Terre Haute",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.85,-113.02),[], 170),   
("village_64","Cahokia",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(191.23,-69.93),[], 100),           
("village_65","Pointe Sainte-Anne",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-216.53,-215.83),[], 100),    
("village_66","Saint-Jean-sur-Richelieu",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-124.11,-222.04),[], 100), 
("village_67","Saint-Paul-de-l'Ile-aux-Noix",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.1,-215.74),[], 100),
("village_68","Longueuil",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.78,-215.09),[], 100),        
("village_69","Grand Pre",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-261.98,-207.23),[], 100),      
("village_70","Miramichy",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-257.14,-245.93),[], 100),      
("village_71","Saint-Hyacinthe",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.25,-221.47),[], 100),    
("village_72","Cobeguit",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-276.54,-216.54),[], 20),        
("village_73","Trois-Rivières",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-144.39,-243.06),[], 100),   
("village_74","Basseville",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.64,-200.05),[], 15),     
("village_75","Les Cayes",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.97,256.13),[], 15),        
("village_76","Port-au-Prince",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-122.71,249.02),[], 90),     
("village_77","Môle-Saint-Nicolas",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.84,227.65),[], 180), 
("village_78","Pointe-a-Pitre",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-318.14, 290.14),[], 180),  
("village_79","Roseau",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-318.41,305.04),[], 0),         
("village_80","Beaubassin",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-262.63,-219.98),[], 40),   
("village_81","Porte-la-Joye",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-283.7,-230.38),[], 20), 
("village_82","Niganiche",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-331.19,-236.34),[], 60),    
("village_83","Port Toulouse",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-322.29,-213.99),[], 80),  
("village_84","Biloxi",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154,49.04),[], 110),                
("village_85","Mobile",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(144.16,40.46),[], 120),               
("village_86","Baton Rouge",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(195.26,35.93),[], 130),                 
("village_87","Cote des Allemands",  icon_french_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(185.52,57.92),[], 170),
#Spanish 3    
("village_88","Puerto Principe",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31,198),[], 40),             
("village_89","Santa Rosa",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(310.8,94.79),[], 20),             
("village_90","Tampico",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(310.23,191.53),[], 60),              
("village_91","Panuco",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(316.06,200.5),[], 55),                 
("village_92","Puebla",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(311.92,251.15),[], 15),                
("village_93","Oaxaca",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(300.97,273.85),[], 10),          
("village_94","Ciudad Real",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(235.83,278.61),[], 35),     
("village_95","Campeche",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(192.53,238.24),[], 160),             
("village_96","Merida",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(171.97,204.19),[], 180),
("village_97","Puerto Cortes",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(141.66,298.36),[], 40),         
("village_98","Trujillo",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.19,293.98),[], 20), 
("village_99","Bayamo",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53,217),[], 10),       
("village_100","Trinidad",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2,192),[], 35),
("village_101","Santiago de Cuba",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74,224),[], 160),             
("village_102","Puerto Plata",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.17,225.51),[], 90),   
("village_103","Santiago de los Caballeros",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161,236),[], 220),
("village_104","San Juan",  icon_spanish_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-238.58,251.53),[], 180), 
########## BREAK IN FACTION ORDER FOR VILLAGE ASSIGNMENT
#British 1.1
("village_105", "Gnaddenhutten",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.32,-147.83),[], 100), #Native
#French 2.1
("village_106","Natchitoches",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(221.51,-1.5),[], 170),      #Native
("village_107","Natchez",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(197.31,2.69),[], 170),           #Native
("village_108","Kaskaskia",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(186.97,-64.71),[], 100),       #Native 
("village_109","La Presentation",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.21,-189.23),[], 43), #Native        
("village_110","Oswegatchie",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.16,-202.84),[], 170),    #Native
("village_111","Mandan",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(256.97,-261.92),[], 170),         #Native
("village_112","Venango",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.21,-142.48),[], 100),          #Native
("village_113","Cataraqui",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.12,-202.53),[], 100),      #Native
#Spanish 3.1
("village_114","Jinotega",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.92,344.29),[], 10),         #Native  
("village_115","Calusa",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.37,125.42),[], 35),            #Native           
("village_116","Tocobaga",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.8,91.96),[], 160),           #Native         
("village_117","Apalachee",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.53,50.76),[], 180),         #Native            
("village_118","Panzacola",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.21,39.52),[], 0),          #Native
#Iroquois 4
("village_119","Erie",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.85,-162.83),[], 55),                 
("village_120","Canawaugus",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.15,-169.85),[], 60),           
("village_121","Ganondagan",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.96,-174.39),[], 55),         
("village_122","Cayuga",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.61,-175.53),[], 172),       
("village_123","Susquehanna",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.96,-165.79),[], 150),   
("village_124","Tuscarora",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.7,-170.82),[], 120),   
("village_125","Oneida",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.88,-191.42),[], 100),               
("village_126","Canadasegy",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.85,-176.13),[], 120), 
("village_127","Oriskany",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.3,-184.75),[], 100), 
("village_128","Onnontare",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37,-177),[], 210),
("village_129","Koshaksink",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.73,-132.47),[], 300),       
("village_130","Ononowaga Cochake",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.26,-128.79),[], 10),  
("village_131","Ononowaga Kuskusky",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.59,-139.96),[], 160), 
("village_132","Oweso'gawenoeh",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.27,-123.69),[], 220),   
#Cherokee 5
("village_133","Nununyi",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.54, -63.28),[], 15),        
("village_134","Tuckaseegee",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.77, -51.46),[], 10),       
("village_135","Etchoe",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.88, -47.12),[], 35),          
("village_136", "Estatoe",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.18, -39.19),[], 90),       
("village_137", "Cattoogachaye",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(87.92, -38.51),[], 150),          
("village_138", "Aquonatuste",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(87.77, -43.8),[], 200),    
("village_139", "Little Tellico",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.49, -48.28),[], 200),  
("village_140", "Mialoquo",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.38, -53.5),[], 100),    
("village_141", "Citico",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.93, -52),[], 100),          
#Wabanaki 6                           
("village_142","Woronoke",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-124.46,-162.29),[], 35),         
("village_143","Nanrantsouak",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-188.21,-206.07),[], 160),             
("village_144","Aukpaque",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.79,-217.37),[], 40),      
("village_145","Shubenacadie",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-278.77,-211.63),[], 135),  
("village_146","Passamaquoddy",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213.12,-202.6),[], 100),  
("village_147","Pijelooeekak",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-263.06,-194.63),[], 100),  
("village_148","Sokoki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.97,-238.39),[], 100),       
("village_149","Madawaska",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192.25,-224.53),[], 100),     
("village_150","Alenape Meneha",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-202.68,-207.33),[], 100),
#Mohawk 7
("village_151","Kanien'keha:ka",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.6,-199.34),[], 150),
("village_152","Tarajorees",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91.65,-179.6),[], 200),    
("village_153","Canajoharie",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.72,-181.72),[], 40),
("village_154","Ganienkeh",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.65,-201.86),[], 120),    
("village_155","Ahkwesahsne",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.87,-194.92),[], 200),   
("village_156","Kanesatake",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.19,-212.09),[], 200),    
("village_157","Atheclaghque",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.42,-179.27),[], 200),  
#Huron 8
("village_158","Ancienne Lorette",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161.89,-258.53),[], 200), 
("village_159","Magagua",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.93,-165.17),[], 305),         
("village_160","Anderdon",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.96,-155.35),[], 200),        
("village_161","Junundat",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.43,-149.87),[], 200),      
("village_162","Jejakweyandat",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.18,-131.34),[], 200),  
("village_163","Jejakwe",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.32,-124.04),[], 200),       
("village_164","Ouadot Muskingum",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.4,-129.16),[], 200),  
("village_165","Conchake",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.15,-126.09),[], 100),         
("village_166","Kuskuskyandat",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0,-138.68),[], 50),    
#Lenape 9
("village_167", "Chugnut",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75.3, -165.65),[], 200),      
("village_168", "Owego",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.02, -166),[], 40),         
("village_169", "Sheshequenink",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.86, -158.9),[], 90),            
("village_170", "Indaochaic",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.15, -133),[], 160),     
("village_171", "Muhheconneokink",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.61, -129.69),[], 200),      
("village_172", "Sawcunk",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.08, -123.04),[], 40),        
("village_173", "Gekelmukpechunk",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.71, -127.39),[], 90),             
("village_174", "Wappocomo",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.83, -101.74),[], 160),  
("village_175", "Kuskuskink",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.13, -134.75),[], 160),    
#Miami 10
("village_176","Saakiiweeyonki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(114.92, -149.09),[], 322), 
("village_177","Mihsiiwiateehi",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.27, -150.75),[], 170), 
("village_178","Kineepikomeehkwa",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(119.18, -117.89),[], 160), 
("village_179","Kiteepihkwana",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(129.68, -111.86),[], 173),  
("village_180","Waayaahtanonki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132.14, -110.35),[], 223), 
("village_181","Peeyankihsionki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140.64, -102.89),[], 335), 
("village_182","Aciipihkahkionki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154.94, -85.05),[], 160), 
("village_183","Pinkwaawilenionki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.85, -109.53),[], 160),
#Shawnee 11 
("village_184","Kuskusky",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.09,-137.29),[], 120),      
("village_185","Nonhelemah",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.01,-114.58),[], 100),           
("village_186","Kispoko",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.43,-105.44),[], 110),              
("village_187","Shannoah",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.03,-105.76),[], 120),         
("village_188","Shinoudaista",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.11,-105.3),[], 100),         
("village_189","Eskippakithiki",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.71,-68.39),[], 110),      
("village_190","Chilliocothe",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.9,-109.63),[], 120),        
#Odawa 12
("village_191","Manidoowaling",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.7, -228.37),[], 160),    
("village_192","Ahnumawautinkumig",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.1, -213.76),[], 246),
("village_193","Ahptunwating",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.69, -210.87),[], 166),   
("village_194","Wabigungweshcupago",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(114.41, -181.93),[], 160), 
("village_195","Shingobeeng",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.94, -170.46),[], 160),    
("village_196","Owashtanong",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(104.96, -153.8),[], 227),    
("village_197","Maamii",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.51, -143.04),[], 160),         
("village_198","Ogantz",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.94, -150.48),[], 160),      
#Ojibwe 13 
("village_199","Gichiziibiwininiwag",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(252.5, -254.7),[], 20),        
("village_200","Gichigamiing",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(191.24, -256.76),[], 60),       
("village_201","Baawiting",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(90.13, -235.24),[], 55),       
("village_202","Zaaga'iganing",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(196.88, -221.38),[], 15),      
("village_203","Sagenong",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.58, -185.38),[], 10),  
("village_204","Cobechenonk",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.23, -184.07),[], 35),        
("village_205","Mekisewancenonk",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.19, -177.6),[], 160), 
#Potawatomi 14
("village_206","Kwikwiyak",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.04, -204.52),[], 62),  
("village_207","Wnaneg-gizs",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(149.7, -192.42),[], 160),   
("village_208","Zhegagoynak",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.51, -155.11),[], 127), 
("village_209","Sheggwe",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(100.96, -147.18),[], 353),     
("village_210","Nadowesippi",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91.25, -159.01),[], 160),   
("village_211","Wawiatenang",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.15, -160.16),[], 64), 
#Choctaw 15
("village_212","Yowannis",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(148.22,23.38),[], 135),           
("village_213","Yashu Iskitini",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(155.09,5.02),[], 180),    
("village_214","Oaka Loosa",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.52,46.36),[], 200), 
("village_215","Louckata",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(160.58,-0.63),[], 135),           
("village_216","Abeka",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(151.62,-4.2),[], 120),              
("village_217","Ayanabi",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(160.59,6.07),[], 40),             
("village_218","Bouctoucoulou",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(152.12,-0.58),[], 300),     
("village_219","Cuctachas",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(170.49,7.05),[], 200),            
("village_220","Mongoulacha",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(152.08,3.02),[], 70),         
("village_221","Concha",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(162.82,12.79),[], 200),           
("village_222","Pante",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(157.84,12.34),[], 70),           
#Chickasaw 16
("village_223","Tchokaffala",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(155.66,-16.6),[], 70),       
("village_224","Tchikoulechasto",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(171.18,-34.57),[], 70),  
("village_225","Falatchao",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(170.28,-28.81),[], 70),        
("village_226","Chatelaw",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(168.26,-21.81),[], 70),         
#Creek 17
("village_227","Tokepahce",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.56,-1.99),[], 50),              
("village_228","Cusseta",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.26,34.28),[], 110),               
("village_229","Talladega",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.83,8.25),[], 120),
("village_230","Etowah",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.5,-8.7),[], 20),            
("village_231","Cahawba",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.06,16),[], 80), 
("village_232","Okfuskee",  icon_native_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105,-3),[], 135),

#nonexistant villages
("village_a","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(233.91,-303.32),[], 135),       
("village_b","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(180.57,-262.31),[], 135),       
("village_c","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(85.12,-217.36),[], 135),      
("village_d","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.68,-163.92),[], 135),      
("village_e","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.6,-133.12),[], 135),       
("village_f","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(188.59,-244.24),[], 135),     
("village_g","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.42,-118.04),[], 135),      
("village_h","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.97,-118.91),[], 135),      
("village_i","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.15,-139.26),[], 135),      
("village_j","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.03,-153.59),[], 135),      
("village_k","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.2,-157.71),[], 135),      
("village_l","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.06,-47.05),[], 135),      
("village_m","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.34,-174.53),[], 135),     
("village_n","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(123.72,-122.8),[], 135),      
("village_o","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.32,-157.97),[], 135),        
("village_p","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.86,-205.89),[], 135),     
("village_q","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.86,-91.67),[], 135),       
("village_r","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(349.96,-349.26),[], 135),    
("village_s","irrelevant",  icon_native_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(126.98,11.99),[], 135),      

###################################
 
  #Guerre en Amerique microfactions! start
  #Guerre en Amerique forts
  ("fort_1","Moose Factory",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.78,-330.01),[],165), #Hudson Bay Company 
  ("fort_2","Philipsburg",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-288.56,256.54),[],165), #Dutch 
  ("fort_3","Fort La Reine",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(238.19,-281.42),[],165), #Coureurs des Bois 
  ("fort_4","Boston Common",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.89,-159.44),[],165), #Sons of Liberty 
  ("fort_5","Navassa Island",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.3,250.77),[],165), #Maroons 
  ("fort_6","Misipawistik",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(215.14,-325.19),[],165), #Cree 
  ("fort_7","Kitcispirini",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.93,-219.34),[],165), #Algonkin 
  ("fort_8","Whahktukuk",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.41,-163.39),[],165), #Mohican 
  ("fort_9","Nassaw-Weyapee",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.64,-61.3),[],165), #Catawba 
  ("fort_10","Grand Inagua",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.08,206.56),[],165), #West Indies Assassins
  ("fort_11","Davenport Homestead",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159.66,-166.87),[],165), #American Assassins 
  ("fort_12","Fort Arsenal",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.08,-144.21),[],165), #Templars  
  #Guerre en Amerique microfactions! end
  
  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("dhorak_keep","Dhorak_Keep",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 

  ("training_ground_1", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("training_ground_2", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("training_ground_3", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("training_ground_4", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 
  ("training_ground_5", "Training Field",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-310),[], 100), 


#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], -95),
  ("Bridge_2","{!}2",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 100),
  ("Bridge_3","{!}3",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 170),
  ("Bridge_4","{!}4",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], -26),
  ("Bridge_5","{!}5",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 105),
  ("Bridge_6","{!}6",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], -51),
  ("Bridge_7","{!}7",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], -80),
  ("Bridge_8","{!}8",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 23),
  ("Bridge_9","{!}9",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], -80),
  ("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 48),
  ("Bridge_11","{!}11",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 104),
  ("Bridge_12","{!}12",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 40),
  ("Bridge_13","{!}13",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 54),
  ("Bridge_14","{!}14",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], -12),
  ("Bridge_15","{!}15",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], -9),
  ("Bridge_16","{!}16",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 106),
  ("Bridge_17","{!}17",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 14),
  ("Bridge_18","{!}18",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 92),
  ("Bridge_19","{!}19",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 85),
  ("Bridge_20","{!}20",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], -12),
  ("Bridge_21","{!}21",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 81),
  ("Bridge_22","{!}22",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 58),
  ("Bridge_23","{!}23",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 144.5),
  ("Bridge_24","{!}24",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 51),
  ("Bridge_25","{!}25",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 17),
  ("Bridge_26","{!}26",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 16.5),
  ("Bridge_27","{!}27",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 173),
  ("Bridge_28","{!}28",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 146),
  ("Bridge_29","{!}29",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 32),
  ("Bridge_30","{!}30",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[], 36),
  ("Bridge_31","{!}31",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],19),
  ("Bridge_32","{!}32",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],136),
  ("Bridge_33","{!}33",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],12), 
  ("Bridge_34","{!}34",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],176), 
  ("Bridge_35","{!}35",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],88), 
  ("Bridge_36","{!}36",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],215), 
  ("Bridge_37","{!}37",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],79),  
  ("Bridge_38","{!}38",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],20),  
  ("Bridge_39","{!}39",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],93), 
  ("Bridge_40","{!}40",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],149), 
  ("Bridge_41","{!}41",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],146), 
  ("Bridge_42","{!}42",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],156),  
  ("Bridge_43","{!}43",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],161), 
  ("Bridge_44","{!}44",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],148), 
  ("Bridge_45","{!}45",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280,-10),[],87), 

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(34, -114),[(trp_looter,15,0)]), #not enabled
  ("seto_pirate_spawn_point"  ,"The Caribbean",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-107.07,205.16),[(trp_looter,15,0)]),
  ("kanto_rebel_spawn_point"   ,"Ohio River Valley",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(78.33,-94.76),[(trp_looter,15,0)]), 
  ("shinano_rebel_spawn_point"  ,"Appalachia",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(10.28,-89.62),[(trp_looter,15,0)]),  
  ("woku_pirate_spawn_point" ,"Acadia",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-234.8,-219.25),[(trp_looter,15,0)]),  
  ("kinai_rebel_spawn_point"   ,"Basse Louisiane",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(177.59,12.39),[(trp_looter,15,0)]), 
  ("monk_rebel_spawn_point"   ,"Great Plains",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(205.57,-144.73),[(trp_looter,15,0)]), 
  ("northern_raider_spawn_point"  ,"Algonquin",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-54.84,-223.06),[(trp_looter,15,0)]),  
  
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(280,-310),[(trp_looter,15,0)]),
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
