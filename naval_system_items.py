# -*- coding: utf-8 -*-
# Naval System Items for Guerre en Amerique Mod
# These items should be added to module_items.py

from header_items import *

# Ship item definitions based on French and Indian War vessels
# Ships function similar to horses but provide water travel bonuses

naval_items = [
    # Small Vessels - Starting Ships
    ["ship_bateau", "Bateau", [("boat_a", 0)], 
     itp_type_horse|itp_merchandise|itp_civilian, 0, 150,
     abundance(80)|body_armor(5)|difficulty(0)|horse_speed(35)|horse_maneuver(40)|horse_charge(5)|horse_scale(100),
     imodbits_horse_basic],
    
    ["ship_whaleboat", "Whaleboat", [("boat_b", 0)], 
     itp_type_horse|itp_merchandise|itp_civilian, 0, 200,
     abundance(70)|body_armor(3)|difficulty(0)|horse_speed(45)|horse_maneuver(50)|horse_charge(3)|horse_scale(95),
     imodbits_horse_basic],
    
    # Medium Vessels
    ["ship_schooner", "Schooner", [("ship_medium_a", 0)], 
     itp_type_horse|itp_merchandise, 0, 800,
     abundance(50)|body_armor(15)|difficulty(1)|horse_speed(42)|horse_maneuver(38)|horse_charge(10)|horse_scale(110),
     imodbits_horse_basic],
    
    ["ship_sloop", "Sloop", [("ship_medium_b", 0)], 
     itp_type_horse|itp_merchandise, 0, 1200,
     abundance(40)|body_armor(20)|difficulty(2)|horse_speed(40)|horse_maneuver(35)|horse_charge(15)|horse_scale(115),
     imodbits_horse_basic],
    
    # Large Vessels - Late Game
    ["ship_brigantine", "Brigantine", [("ship_large_a", 0)], 
     itp_type_horse|itp_merchandise, 0, 2500,
     abundance(20)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(30)|horse_charge(25)|horse_scale(125),
     imodbits_horse_basic|imodbit_champion],
    
    ["ship_xebec", "Xebec", [("ship_large_b", 0)], 
     itp_type_horse|itp_merchandise, 0, 2000,
     abundance(25)|body_armor(25)|difficulty(3)|horse_speed(45)|horse_maneuver(42)|horse_charge(20)|horse_scale(120),
     imodbits_horse_basic|imodbit_champion],
    
    # Special Vessels
    ["ship_radeau", "Radeau", [("ship_special_a", 0)], 
     itp_type_horse|itp_merchandise, 0, 1500,
     abundance(30)|body_armor(35)|difficulty(2)|horse_speed(30)|horse_maneuver(25)|horse_charge(30)|horse_scale(130),
     imodbits_horse_basic],
    
    ["ship_tartane", "Tartane", [("ship_special_b", 0)], 
     itp_type_horse|itp_merchandise, 0, 1800,
     abundance(25)|body_armor(22)|difficulty(2)|horse_speed(43)|horse_maneuver(45)|horse_charge(18)|horse_scale(115),
     imodbits_horse_basic],
]

# Notes on ship stats:
# - body_armor represents hull strength
# - horse_speed represents sailing speed on water
# - horse_maneuver represents handling/agility
# - horse_charge represents ramming/boarding effectiveness
# - horse_scale affects visual size on map

# Ship Capacity (troops):
# Bateau: 20 troops
# Whaleboat: 10 troops
# Schooner: 40 troops
# Sloop: 50 troops
# Brigantine: 80 troops
# Xebec: 60 troops
# Radeau: 70 troops
# Tartane: 50 troops