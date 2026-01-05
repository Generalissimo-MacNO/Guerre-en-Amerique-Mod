# -*- coding: utf-8 -*-
# Naval System Menus for Guerre en Amerique Mod
# These menus should be added to module_game_menus.py

from header_common import *
from header_operations import *
from module_constants import *

naval_menus = [
    # Port/Harbor menu
    ("port", 0,
     "You arrive at the port. Ships bob gently in the harbor, and sailors bustle about loading cargo.",
     "none",
     [
         # Show available ships for purchase
         ("port_buy_ship", [], "Visit the shipwright.",
          [
              (jump_to_menu, "mnu_port_shipwright"),
          ]),
         
         # Repair current ship
         ("port_repair_ship", 
          [
              (call_script, "script_check_party_has_ship", "p_main_party"),
              (eq, reg0, 1),
          ], 
          "Repair your ship.",
          [
              (call_script, "script_get_party_best_ship", "p_main_party"),
              (assign, ":ship_id", reg0),
              
              # Calculate repair cost
              (item_get_value, ":ship_value", ":ship_id"),
              (store_div, ":repair_cost", ":ship_value", 10),
              
              (try_begin),
                  (store_troop_gold, ":gold", "trp_player"),
                  (ge, ":gold", ":repair_cost"),
                  
                  (troop_remove_gold, "trp_player", ":repair_cost"),
                  (display_message, "@Your ship has been repaired."),
                  
                  # Restore ship condition (implement ship damage system)
                  (jump_to_menu, "mnu_port"),
              (else_try),
                  (display_message, "@You don't have enough gold to repair your ship."),
                  (jump_to_menu, "mnu_port"),
              (try_end),
          ]),
         
         # Recruit sailors
         ("port_recruit_sailors", [], "Recruit sailors.",
          [
              (jump_to_menu, "mnu_port_recruit"),
          ]),
         
         # Embark/Set sail
         ("port_embark", 
          [
              (call_script, "script_check_party_has_ship", "p_main_party"),
              (eq, reg0, 1),
          ], 
          "Set sail.",
          [
              (party_set_slot, "p_main_party", slot_party_embarked, 1),
              (display_message, "@You set sail from the port."),
              (change_screen_return),
          ]),
         
         ("port_leave", [], "Leave the port.",
          [
              (change_screen_return),
          ]),
     ]),
    
    # Shipwright menu
    ("port_shipwright", 0,
     "The shipwright shows you the vessels available for purchase.",
     "none",
     [
         # Small vessels
         ("buy_bateau", 
          [
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", 150),
          ], 
          "Buy a Bateau (150 denars) - Small transport vessel, 20 troops.",
          [
              (troop_remove_gold, "trp_player", 150),
              (troop_add_item, "trp_player", "itm_ship_bateau", 0),
              (display_message, "@You have purchased a Bateau."),
              (jump_to_menu, "mnu_port"),
          ]),
         
         ("buy_whaleboat", 
          [
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", 200),
          ], 
          "Buy a Whaleboat (200 denars) - Fast scout vessel, 10 troops.",
          [
              (troop_remove_gold, "trp_player", 200),
              (troop_add_item, "trp_player", "itm_ship_whaleboat", 0),
              (display_message, "@You have purchased a Whaleboat."),
              (jump_to_menu, "mnu_port"),
          ]),
         
         # Medium vessels
         ("buy_schooner", 
          [
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", 800),
          ], 
          "Buy a Schooner (800 denars) - Medium vessel with 4 guns, 40 troops.",
          [
              (troop_remove_gold, "trp_player", 800),
              (troop_add_item, "trp_player", "itm_ship_schooner", 0),
              (display_message, "@You have purchased a Schooner."),
              (jump_to_menu, "mnu_port"),
          ]),
         
         ("buy_sloop", 
          [
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", 1200),
          ], 
          "Buy a Sloop (1200 denars) - Medium warship with 8 guns, 50 troops.",
          [
              (troop_remove_gold, "trp_player", 1200),
              (troop_add_item, "trp_player", "itm_ship_sloop", 0),
              (display_message, "@You have purchased a Sloop."),
              (jump_to_menu, "mnu_port"),
          ]),
         
         # Large vessels
         ("buy_brigantine", 
          [
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", 2500),
          ], 
          "Buy a Brigantine (2500 denars) - Large warship with 16 guns, 80 troops.",
          [
              (troop_remove_gold, "trp_player", 2500),
              (troop_add_item, "trp_player", "itm_ship_brigantine", 0),
              (display_message, "@You have purchased a Brigantine."),
              (jump_to_menu, "mnu_port"),
          ]),
         
         ("buy_xebec", 
          [
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", 2000),
          ], 
          "Buy a Xebec (2000 denars) - Fast warship with 10 guns, 60 troops.",
          [
              (troop_remove_gold, "trp_player", 2000),
              (troop_add_item, "trp_player", "itm_ship_xebec", 0),
              (display_message, "@You have purchased a Xebec."),
              (jump_to_menu, "mnu_port"),
          ]),
         
         ("shipwright_back", [], "Back.",
          [
              (jump_to_menu, "mnu_port"),
          ]),
     ]),
    
    # Sailor recruitment menu
    ("port_recruit", 0,
     "Experienced sailors are available for hire.",
     "none",
     [
         ("recruit_sailors", [], "Recruit sailors (50 denars each).",
          [
              (jump_to_menu, "mnu_port"),
              # Add sailor recruitment logic here
              (display_message, "@Sailor recruitment not yet implemented."),
          ]),
         
         ("recruit_back", [], "Back.",
          [
              (jump_to_menu, "mnu_port"),
          ]),
     ]),
    
    # Embark/Disembark menu (triggered when near water)
    ("embark_disembark", 0,
     "You are near the water's edge.",
     "none",
     [
         ("embark", 
          [
              (call_script, "script_check_party_has_ship", "p_main_party"),
              (eq, reg0, 1),
              (party_get_slot, ":embarked", "p_main_party", slot_party_embarked),
              (eq, ":embarked", 0),
          ], 
          "Embark on your ship.",
          [
              (party_set_slot, "p_main_party", slot_party_embarked, 1),
              (display_message, "@You embark on your ship."),
              (change_screen_return),
          ]),
         
         ("disembark", 
          [
              (party_get_slot, ":embarked", "p_main_party", slot_party_embarked),
              (eq, ":embarked", 1),
          ], 
          "Disembark from your ship.",
          [
              (party_set_slot, "p_main_party", slot_party_embarked, 0),
              (display_message, "@You disembark from your ship."),
              (change_screen_return),
          ]),
         
         ("embark_cancel", [], "Continue on your way.",
          [
              (change_screen_return),
          ]),
     ]),
    
    # Naval encounter menu
    ("naval_encounter", 0,
     "You spot another vessel on the horizon!",
     "none",
     [
         ("naval_engage", [], "Engage the enemy vessel!",
          [
              # Start naval combat
              (jump_to_menu, "mnu_naval_combat"),
          ]),
         
         ("naval_flee", [], "Attempt to flee.",
          [
              (call_script, "script_get_party_best_ship", "p_main_party"),
              (assign, ":player_ship", reg0),
              
              # Check if player ship is faster
              (try_begin),
                  (ge, ":player_ship", 0),
                  (item_get_horse_speed, ":player_speed", ":player_ship"),
                  
                  # Random chance based on ship speed
                  (store_random_in_range, ":rand", 0, 100),
                  (try_begin),
                      (lt, ":rand", ":player_speed"),
                      (display_message, "@You successfully escape!"),
                      (change_screen_return),
                  (else_try),
                      (display_message, "@The enemy catches up to you!"),
                      (jump_to_menu, "mnu_naval_combat"),
                  (try_end),
              (else_try),
                  (display_message, "@You have no ship to flee with!"),
                  (jump_to_menu, "mnu_naval_combat"),
              (try_end),
          ]),
         
         ("naval_parley", [], "Attempt to parley.",
          [
              (display_message, "@The enemy agrees to talk."),
              # Add parley logic here
              (change_screen_return),
          ]),
     ]),
    
    # Naval combat menu
    ("naval_combat", 0,
     "The vessels close in for combat!",
     "none",
     [
         ("naval_cannon", [], "Fire cannons!",
          [
              (display_message, "@Your cannons roar!"),
              # Add cannon combat logic
              (jump_to_menu, "mnu_naval_combat_result"),
          ]),
         
         ("naval_board", [], "Prepare to board!",
          [
              (display_message, "@You prepare boarding parties!"),
              # Start boarding mission
              (jump_to_menu, "mnu_naval_boarding"),
          ]),
         
         ("naval_maneuver", [], "Attempt to outmaneuver.",
          [
              (display_message, "@You attempt tactical maneuvers."),
              (jump_to_menu, "mnu_naval_combat"),
          ]),
     ]),
]