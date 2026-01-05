# Naval System Integration Guide for Guerre en Amerique Mod

## Overview
This guide explains how to integrate the Viking Conquest-style naval system into your French and Indian War mod.

## Files Created
1. `naval_system_items.py` - Ship item definitions
2. `naval_system_scripts.py` - Naval mechanics scripts
3. `naval_system_menus.py` - Port and naval encounter menus
4. `NAVAL_SYSTEM_DESIGN.md` - Design documentation

## Integration Steps

### Step 1: Add Ship Items to module_items.py

1. Open `module_items.py`
2. Find the section with horse items (search for `itp_type_horse`)
3. Add the ship items from `naval_system_items.py` after the existing horse items
4. Ships use the `itp_type_horse` flag to leverage existing mount mechanics

**Location to add:** After the last horse item, before the musical instruments section

```python
# Add these lines from naval_system_items.py
["ship_bateau", "Bateau", [("boat_a", 0)], 
 itp_type_horse|itp_merchandise|itp_civilian, 0, 150,
 abundance(80)|body_armor(5)|difficulty(0)|horse_speed(35)|horse_maneuver(40)|horse_charge(5)|horse_scale(100),
 imodbits_horse_basic],
# ... (add all ship items)
```

### Step 2: Add Naval Scripts to module_scripts.py

1. Open `module_scripts.py`
2. Scroll to the end of the scripts list
3. Add all scripts from `naval_system_scripts.py`

**Location to add:** At the end of the scripts list, before the closing bracket

```python
# Naval System Scripts
("check_party_on_water", [
    # ... (add script content)
]),
# ... (add all naval scripts)
```

### Step 3: Add Naval Menus to module_game_menus.py

1. Open `module_game_menus.py`
2. Find a suitable location (after town menus or at the end)
3. Add all menus from `naval_system_menus.py`

**Location to add:** After existing town/village menus

```python
# Naval System Menus
("port", 0,
 "You arrive at the port...",
 # ... (add menu content)
),
# ... (add all naval menus)
```

### Step 4: Add Naval Constants to module_constants.py

1. Open `module_constants.py`
2. Add these constants at the end:

```python
# Naval System Constants
water_area_x_min = -100
water_area_x_max = 100
water_area_y_min = -100
water_area_y_max = 100

# Party slots for naval system
slot_party_on_water = 50
slot_party_embarked = 51
slot_party_current_ship = 52
slot_party_movement_speed = 53
```

### Step 5: Add Naval Map Icons to module_map_icons.py

The mod already has ship icons! Look for these existing entries:
```python
("ship", mcn_no_shadow, "boat_sail_on", 0.12, snd_footstep_grass, 0.0, 0.05, 0),
("ship_on_land", mcn_no_shadow, "boat_sail_off", 0.12, 0),
```

You can add additional ship types if needed:
```python
# Add after existing ship icons
("ship_schooner", mcn_no_shadow, "ship_medium_a", 0.15, snd_footstep_grass, 0.0, 0.05, 0),
("ship_brigantine", mcn_no_shadow, "ship_large_a", 0.18, snd_footstep_grass, 0.0, 0.05, 0),
```

### Step 6: Add Port Locations to Towns

1. Open `module_parties.py`
2. Find town definitions
3. Add port functionality to coastal towns

Example modification:
```python
# For coastal towns, add a slot to mark them as ports
(party_set_slot, "p_town_boston", slot_town_is_port, 1),
```

### Step 7: Add Naval Triggers to module_triggers.py

Add these triggers to handle naval mechanics:

```python
# Naval system triggers
(1, 0, 0, [],
 [
     # Check if player is on water
     (call_script, "script_check_party_on_water", "p_main_party"),
     (assign, ":on_water", reg0),
     
     # Apply ship speed bonuses
     (try_begin),
         (eq, ":on_water", 1),
         (call_script, "script_apply_ship_speed_bonus", "p_main_party"),
     (try_end),
 ]),

# Naval encounter trigger
(1, 0, 0, [],
 [
     # Check for naval encounters when on water
     (party_get_slot, ":embarked", "p_main_party", slot_party_embarked),
     (eq, ":embarked", 1),
     
     # Random chance of naval encounter
     (store_random_in_range, ":rand", 0, 1000),
     (lt, ":rand", 5),  # 0.5% chance per check
     
     (jump_to_menu, "mnu_naval_encounter"),
 ]),
```

### Step 8: Create Naval Combat Scenes

1. Open `module_scenes.py`
2. Add naval combat scenes (ship decks for boarding actions)

```python
# Naval combat scene - Ship deck
("naval_combat_deck", sf_generate, 0, "none", [
    # Scene props for ship deck
    (0, mtef_scene_source|mtef_team_0, af_override_horse, 0, 1, []),
    (1, mtef_scene_source|mtef_team_1, af_override_horse, 0, 1, []),
]),
```

### Step 9: Add Naval Mission Templates

1. Open `module_mission_templates.py`
2. Add naval combat mission template

```python
# Naval boarding mission
("naval_boarding", mtf_battle_mode, -1,
 "You board the enemy vessel!",
 [
     # Mission triggers for naval combat
     (ti_on_agent_spawn, 0, 0, [],
      [
          # Spawn agents on ship deck
      ]),
 ]),
```

### Step 10: Compile and Test

1. Run the module system compiler:
   ```
   cd "Guerre en Amerique Source/Module_system 1.171"
   python build_module.py
   ```

2. Copy compiled files to your mod directory

3. Test in-game:
   - Visit a port town
   - Purchase a ship
   - Test embark/disembark
   - Test water travel speed
   - Test naval encounters

## Testing Checklist

- [ ] Ships appear in port merchants
- [ ] Ships can be purchased
- [ ] Ships appear in inventory
- [ ] Embark/disembark works at water's edge
- [ ] Movement speed increases on water with ship
- [ ] Movement speed decreases on water without ship
- [ ] Naval encounters trigger
- [ ] Naval combat works
- [ ] Ship capacity limits work
- [ ] Ship repair works

## Known Limitations

1. **Mesh Requirements**: The ship meshes referenced in the items (boat_a, boat_b, ship_medium_a, etc.) need to exist in your mod's Resource folder. You may need to:
   - Use existing boat meshes from the mod
   - Import meshes from Viking Conquest
   - Create new meshes

2. **Water Detection**: The current water detection is simplified. For production, you'll need to:
   - Define actual water areas on your map
   - Use proper terrain type detection
   - Mark coastal areas

3. **AI Naval Behavior**: AI parties don't automatically use ships. You'll need to:
   - Add scripts for AI ship usage
   - Create naval patrol parties
   - Implement AI naval combat behavior

## Advanced Features to Add

1. **Ship Damage System**: Track hull integrity and require repairs
2. **Crew Management**: Require sailors to operate ships effectively
3. **Naval Supplies**: Require provisions for long voyages
4. **Weather Effects**: Add storms and wind direction
5. **Ship Upgrades**: Allow cannon upgrades, hull reinforcement, etc.
6. **Naval Missions**: Add specific naval quests and objectives
7. **Faction Naval Power**: Track each faction's naval strength
8. **Blockades**: Implement port blockade mechanics

## Troubleshooting

### Ships don't appear in inventory
- Check that ship items are properly added to module_items.py
- Verify itp_type_horse flag is set
- Recompile the module system

### Can't embark/disembark
- Check water area constants are defined
- Verify scripts are properly added
- Check menu conditions

### Movement speed not changing
- Verify triggers are added to module_triggers.py
- Check script logic for speed calculation
- Ensure party slots are properly set

## Support

For issues or questions:
1. Check the module system error log
2. Verify all files are properly integrated
3. Test each component individually
4. Review the Viking Conquest mod for reference

## Credits

Based on the Viking Conquest naval system, adapted for the French and Indian War period with historically accurate vessels from the Lake Champlain fleet (1742-1760).