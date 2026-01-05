# -*- coding: utf-8 -*-
# Naval System Scripts for Guerre en Amerique Mod
# These scripts should be added to module_scripts.py

from header_common import *
from header_operations import *
from module_constants import *

# Script IDs will need to be added to ID_scripts.py after compilation

naval_scripts = [
    # Check if party is on water terrain
    ("check_party_on_water", [
        (store_script_param, ":party_no", 1),
        (assign, ":result", 0),
        
        (try_begin),
            (party_is_active, ":party_no"),
            (party_get_position, pos1, ":party_no"),
            (position_get_x, ":x", pos1),
            (position_get_y, ":y", pos1),
            
            # Check terrain type at party position
            # This is a simplified check - in reality you'd need to check map terrain
            # For now, we'll use a slot to mark water areas
            (try_begin),
                (is_between, ":x", water_area_x_min, water_area_x_max),
                (is_between, ":y", water_area_y_min, water_area_y_max),
                (assign, ":result", 1),
            (try_end),
        (try_end),
        
        (assign, reg0, ":result"),
    ]),
    
    # Check if party has a ship
    ("check_party_has_ship", [
        (store_script_param, ":party_no", 1),
        (assign, ":has_ship", 0),
        
        (try_begin),
            (party_is_active, ":party_no"),
            
            # Check party leader's inventory for ship items
            (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
            (try_for_range, ":i", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":troop_id", ":party_no", ":i"),
                (try_begin),
                    (eq, ":troop_id", "trp_player"),
                    # Check player inventory for ships
                    (troop_get_inventory_capacity, ":inv_cap", ":troop_id"),
                    (try_for_range, ":item_slot", 0, ":inv_cap"),
                        (troop_get_inventory_slot, ":item_id", ":troop_id", ":item_slot"),
                        (ge, ":item_id", 0),
                        (item_get_type, ":item_type", ":item_id"),
                        # Ships are stored as horse-type items
                        (try_begin),
                            (eq, ":item_type", itp_type_horse),
                            # Check if it's actually a ship (by ID range)
                            (is_between, ":item_id", "itm_ship_bateau", "itm_ship_tartane"),
                            (assign, ":has_ship", 1),
                        (try_end),
                    (try_end),
                (try_end),
            (try_end),
        (try_end),
        
        (assign, reg0, ":has_ship"),
    ]),
    
    # Apply ship speed bonus to party
    ("apply_ship_speed_bonus", [
        (store_script_param, ":party_no", 1),
        
        (try_begin),
            (party_is_active, ":party_no"),
            
            # Check if on water
            (call_script, "script_check_party_on_water", ":party_no"),
            (eq, reg0, 1),
            
            # Check if has ship
            (call_script, "script_check_party_has_ship", ":party_no"),
            (eq, reg0, 1),
            
            # Apply speed bonus (ships are faster on water)
            (party_get_slot, ":current_speed", ":party_no", slot_party_movement_speed),
            (store_mul, ":new_speed", ":current_speed", 150),
            (val_div, ":new_speed", 100),
            (party_set_slot, ":party_no", slot_party_movement_speed, ":new_speed"),
        (else_try),
            # On water without ship - apply penalty
            (call_script, "script_check_party_on_water", ":party_no"),
            (eq, reg0, 1),
            
            (party_get_slot, ":current_speed", ":party_no", slot_party_movement_speed),
            (store_mul, ":new_speed", ":current_speed", 50),
            (val_div, ":new_speed", 100),
            (party_set_slot, ":party_no", slot_party_movement_speed, ":new_speed"),
        (try_end),
    ]),
    
    # Get best ship in party inventory
    ("get_party_best_ship", [
        (store_script_param, ":party_no", 1),
        (assign, ":best_ship", -1),
        (assign, ":best_value", 0),
        
        (try_begin),
            (party_is_active, ":party_no"),
            (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
            
            (try_for_range, ":i", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":troop_id", ":party_no", ":i"),
                (try_begin),
                    (eq, ":troop_id", "trp_player"),
                    (troop_get_inventory_capacity, ":inv_cap", ":troop_id"),
                    
                    (try_for_range, ":item_slot", 0, ":inv_cap"),
                        (troop_get_inventory_slot, ":item_id", ":troop_id", ":item_slot"),
                        (ge, ":item_id", 0),
                        (is_between, ":item_id", "itm_ship_bateau", "itm_ship_tartane"),
                        
                        (item_get_value, ":ship_value", ":item_id"),
                        (try_begin),
                            (gt, ":ship_value", ":best_value"),
                            (assign, ":best_ship", ":item_id"),
                            (assign, ":best_value", ":ship_value"),
                        (try_end),
                    (try_end),
                (try_end),
            (try_end),
        (try_end),
        
        (assign, reg0, ":best_ship"),
    ]),
    
    # Calculate ship capacity for troops
    ("get_ship_capacity", [
        (store_script_param, ":ship_id", 1),
        (assign, ":capacity", 0),
        
        (try_begin),
            (eq, ":ship_id", "itm_ship_bateau"),
            (assign, ":capacity", 20),
        (else_try),
            (eq, ":ship_id", "itm_ship_whaleboat"),
            (assign, ":capacity", 10),
        (else_try),
            (eq, ":ship_id", "itm_ship_schooner"),
            (assign, ":capacity", 40),
        (else_try),
            (eq, ":ship_id", "itm_ship_sloop"),
            (assign, ":capacity", 50),
        (else_try),
            (eq, ":ship_id", "itm_ship_brigantine"),
            (assign, ":capacity", 80),
        (else_try),
            (eq, ":ship_id", "itm_ship_xebec"),
            (assign, ":capacity", 60),
        (else_try),
            (eq, ":ship_id", "itm_ship_radeau"),
            (assign, ":capacity", 70),
        (else_try),
            (eq, ":ship_id", "itm_ship_tartane"),
            (assign, ":capacity", 50),
        (try_end),
        
        (assign, reg0, ":capacity"),
    ]),
    
    # Check if party can embark (has access to water and ship)
    ("can_party_embark", [
        (store_script_param, ":party_no", 1),
        (assign, ":can_embark", 0),
        
        (try_begin),
            (party_is_active, ":party_no"),
            
            # Check if near water
            (call_script, "script_check_party_on_water", ":party_no"),
            (assign, ":on_water", reg0),
            
            # Check if has ship
            (call_script, "script_check_party_has_ship", ":party_no"),
            (assign, ":has_ship", reg0),
            
            # Can embark if near water and has ship
            (try_begin),
                (eq, ":on_water", 1),
                (eq, ":has_ship", 1),
                (assign, ":can_embark", 1),
            (try_end),
        (try_end),
        
        (assign, reg0, ":can_embark"),
    ]),
]

# Constants for water areas (these should be defined in module_constants.py)
# water_area_x_min = -100
# water_area_x_max = 100
# water_area_y_min = -100
# water_area_y_max = 100

# Slot definitions (add to module_constants.py)
# slot_party_movement_speed = 0
# slot_party_on_water = 1
# slot_party_embarked = 2
# slot_party_current_ship = 3