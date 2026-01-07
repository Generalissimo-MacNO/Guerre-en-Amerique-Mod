# Naval System Implementation Guide
## Guerre en Amérique Mod - French & Indian War

---

## Overview

This mod now includes a complete naval system adapted from Viking Conquest, featuring:
- 8 ship types (Ship of the Line, Frigate, Sloop, Brig, Merchant Ship, Longboat, Canoe, Bateau)
- Officer-specific ship preferences (via slot system)
- Naval battles with ship spawning and control
- Ship purchasing and management
- Portaging system for canoes and bateaux

---

## Ship Types

### Large Warships
1. **Ship of the Line** (`ship_type_ship_of_line = 1`)
   - Crew: 90
   - Speed: 16
   - Role: Flagship, fleet command
   - Historical: Large British/French warships

2. **Frigate** (`ship_type_frigate = 2`)
   - Crew: 55
   - Speed: 20
   - Role: Fast warship, patrol
   - Historical: Main naval combat vessel

### Medium Vessels
3. **Sloop** (`ship_type_sloop = 3`)
   - Crew: 30
   - Speed: 12
   - Role: Coastal patrol, lake warfare
   - Historical: Common on Great Lakes

4. **Brig** (`ship_type_brig = 4`)
   - Crew: 16
   - Speed: 14
   - Role: Small warship, fast courier
   - Historical: Versatile two-masted vessel

### Support Vessels
5. **Merchant Ship** (`ship_type_merchant_ship = 5`)
   - Crew: 20
   - Speed: 10
   - Role: Cargo transport, supply
   - Historical: Trade and logistics

6. **Longboat** (`ship_type_longboat = 6`)
   - Crew: 8
   - Speed: 8
   - Role: Small boat, landing craft
   - Historical: Ship's boat, coastal transport

### River Craft (Portage-able)
7. **Canoe** (`ship_type_canoe = 7`)
   - Crew: 2-6
   - Speed: 10
   - Role: Scouting, wilderness travel
   - Historical: Native American and frontier use
   - **Special**: Can be portaged (carried overland)

8. **Bateau** (`ship_type_bateau = 8`)
   - Crew: 15-30
   - Speed: 8
   - Role: River transport, military logistics
   - Historical: Primary military transport on rivers
   - **Special**: Can be portaged (with difficulty)

---

## Slot System

### Troop Slots (180-200)

Officers can have naval preferences stored in these slots:

```python
slot_troop_preferred_ship_type    = 180  # Ship type (1-8, 0=default)
slot_troop_ship_quality_bonus     = 181  # Quality bonus (0-25%)
slot_troop_max_ships_bonus        = 182  # Extra ships (0-5)
slot_troop_naval_specialization   = 183  # Specialization type
```

### Naval Specializations

```python
naval_spec_none    = 0  # No specialization (default assignment)
naval_spec_fleet   = 1  # Fleet command (large warships)
naval_spec_river   = 2  # River warfare (bateaux, canoes)
naval_spec_lake    = 3  # Lake warfare (sloops, brigs)
naval_spec_coastal = 4  # Coastal patrol
naval_spec_merchant = 5  # Supply/merchant ships
```

---

## How to Assign Ships to Officers

### Step 1: Identify the Officer

Find the officer in `module_troops.py`. For example:
```python
["knight_1_10", "Major-General John Bradstreet", "John Bradstreet", ...]
```

### Step 2: Add Slot Assignments

After the troop definition, add a list with slot assignments:

```python
["knight_1_10", "Major-General John Bradstreet", "John Bradstreet", 
 tf_hero, 0, reserved, fac_kingdom_1, 
 [equipment_list], 
 attributes, weapon_proficiencies, skills, 
 face_code],
[
    # Naval assignments
    (troop_set_slot, "knight_1_10", slot_troop_preferred_ship_type, ship_type_bateau),
    (troop_set_slot, "knight_1_10", slot_troop_ship_quality_bonus, 15),
    (troop_set_slot, "knight_1_10", slot_troop_max_ships_bonus, 5),
    (troop_set_slot, "knight_1_10", slot_troop_naval_specialization, naval_spec_river),
]
```

### Step 3: Compile and Test

Compile the module system and test in-game.

---

## Example Assignments

### British Officers

**Admiral Edward Boscawen** (Fleet Commander):
```python
["knight_1_admiral_boscawen", "Admiral Edward Boscawen", "Edward Boscawen", ...],
[
    (troop_set_slot, "knight_1_admiral_boscawen", slot_troop_preferred_ship_type, ship_type_ship_of_line),
    (troop_set_slot, "knight_1_admiral_boscawen", slot_troop_ship_quality_bonus, 25),
    (troop_set_slot, "knight_1_admiral_boscawen", slot_troop_max_ships_bonus, 3),
    (troop_set_slot, "knight_1_admiral_boscawen", slot_troop_naval_specialization, naval_spec_fleet),
]
```

**Major-General John Bradstreet** (Bateau Specialist):
```python
["knight_1_10", "Major-General John Bradstreet", "John Bradstreet", ...],
[
    (troop_set_slot, "knight_1_10", slot_troop_preferred_ship_type, ship_type_bateau),
    (troop_set_slot, "knight_1_10", slot_troop_ship_quality_bonus, 15),
    (troop_set_slot, "knight_1_10", slot_troop_max_ships_bonus, 5),
    (troop_set_slot, "knight_1_10", slot_troop_naval_specialization, naval_spec_river),
]
```

### French Officers

**Admiral Joseph-Hyacinthe de Rigaud, marquis de Vaudreuil**:
```python
["knight_2_1", "Admiral Joseph-Hyacinthe de Rigaud, marquis de Vaudreuil", ...],
[
    (troop_set_slot, "knight_2_1", slot_troop_preferred_ship_type, ship_type_frigate),
    (troop_set_slot, "knight_2_1", slot_troop_ship_quality_bonus, 20),
    (troop_set_slot, "knight_2_1", slot_troop_max_ships_bonus, 3),
    (troop_set_slot, "knight_2_1", slot_troop_naval_specialization, naval_spec_fleet),
]
```

**Admiral Hubert de Brienne, Comte de Conflans**:
```python
["knight_2_2", "Admiral Hubert de Brienne, Comte de Conflans", ...],
[
    (troop_set_slot, "knight_2_2", slot_troop_preferred_ship_type, ship_type_frigate),
    (troop_set_slot, "knight_2_2", slot_troop_ship_quality_bonus, 20),
    (troop_set_slot, "knight_2_2", slot_troop_max_ships_bonus, 3),
    (troop_set_slot, "knight_2_2", slot_troop_naval_specialization, naval_spec_fleet),
]
```

---

## Ship Assignment Logic

### How It Works

1. **Check for Preferred Ship**: System checks if officer has `slot_troop_preferred_ship_type` set
2. **Validate Party Size**: Ensures party is large enough for the preferred ship
3. **Apply Quality Bonus**: Adds quality bonus from `slot_troop_ship_quality_bonus`
4. **Apply Fleet Bonus**: Adds extra ships from `slot_troop_max_ships_bonus`
5. **Fallback to Default**: If no preference or party too small, uses size-based assignment

### Default Assignment (No Preference)

If an officer has no ship preference (slots not set), the system assigns ships based on party size:

```
Party Size > 110 → Ship of the Line
Party Size > 78  → Frigate
Party Size > 54  → Sloop
Party Size > 14  → Brig
Party Size > 0   → Longboat
```

---

## Quality Bonuses

Quality affects ship condition (durability and performance):

- **+25%**: Fleet admirals, legendary commanders
- **+20%**: Senior admirals, experienced fleet commanders
- **+15%**: Specialized captains (bateau masters, lake commanders)
- **+10%**: Regular naval officers
- **+5%**: Officers with some naval experience
- **0%**: Default (no bonus)

---

## Max Ships Bonuses

Determines how many ships an officer can command:

- **Base**: 7 ships (default for all officers)
- **+5 ships**: Bateau fleet commanders (total: 12 ships)
- **+3 ships**: Fleet admirals (total: 10 ships)
- **+2 ships**: Senior captains (total: 9 ships)
- **+1 ship**: Junior officers (total: 8 ships)
- **+0 ships**: Default (total: 7 ships)

---

## Party Ship Slots (301-341)

These slots store actual ship data for parties:

### Ship Type (301-310)
Stores which type of ship (1-8)

### Ship Name (311-320)
Stores custom ship name (troop ID or string)

### Ship Quality (321-330)
Stores ship condition (0-100%)

### Ship Properties (331-340)
Stores encoded customization data (wood, sails, paint, etc.)

---

## Testing Your Assignments

### In-Game Testing

1. **Start a new game** or load a save
2. **Find the officer** you assigned a ship to
3. **Engage in a naval battle** with that officer's party
4. **Verify**:
   - Officer has the correct ship type
   - Ship quality is higher (if bonus applied)
   - Officer commands multiple ships (if bonus applied)

### Debug Commands

Add this script to `module_scripts.py` for testing:

```python
("debug_display_naval_slots",
  [
    (store_script_param, ":troop", 1),
    
    (troop_get_slot, ":ship_type", ":troop", slot_troop_preferred_ship_type),
    (troop_get_slot, ":quality", ":troop", slot_troop_ship_quality_bonus),
    (troop_get_slot, ":max_ships", ":troop", slot_troop_max_ships_bonus),
    (troop_get_slot, ":spec", ":troop", slot_troop_naval_specialization),
    
    (assign, reg0, ":ship_type"),
    (assign, reg1, ":quality"),
    (assign, reg2, ":max_ships"),
    (assign, reg3, ":spec"),
    
    (display_message, "@Naval: Ship={reg0} Quality=+{reg1}% MaxShips=+{reg2} Spec={reg3}"),
  ]
)
```

Call it from a dialog or menu to check an officer's naval slots.

---

## Troubleshooting

### Officer Not Getting Preferred Ship

**Problem**: Officer assigned a ship but gets default instead

**Solutions**:
1. Check slot values are set correctly
2. Verify party size is large enough for the ship
3. Ensure ship type is valid (1-8)
4. Check if script `script_get_lord_preferred_ship` is implemented

### Ship Quality Not Applied

**Problem**: Quality bonus not showing in battle

**Solutions**:
1. Verify `slot_troop_ship_quality_bonus` is set
2. Check if bonus is within valid range (0-25)
3. Ensure ship assignment script applies the bonus

### Too Many/Few Ships

**Problem**: Officer has wrong number of ships

**Solutions**:
1. Check `slot_troop_max_ships_bonus` value
2. Verify total doesn't exceed game limits
3. Ensure party has enough troops for all ships

---

## Advanced: Custom Ship Properties

### Wood Types

```python
wood_type_pine = 1  # Basic (100% base value)
wood_type_oak  = 2  # Good (115% base value)
wood_type_teak = 3  # Best (130% base value)
```

Set preferred wood:
```python
(troop_set_slot, "troop_id", slot_troop_preferred_ship_wood, wood_type_oak),
```

### Sail Designs

Sails 1-9 available (visual customization)

### Paint/Finish

Finishes 0-8 available (visual customization)

---

## Historical Accuracy Notes

### Ship Types by Faction

**British Navy**:
- Ships of the Line (large fleet actions)
- Frigates (patrol, commerce raiding)
- Sloops (Great Lakes, coastal)
- Bateaux (river transport)

**French Navy**:
- Frigates (primary warship)
- Ships of the Line (fewer than British)
- Bateaux (extensive river use)
- Canoes (frontier warfare)

### Notable Commanders

**British**:
- Admiral Edward Boscawen (fleet command)
- Major-General John Bradstreet (bateau operations)
- Captain Joshua Loring (Lake George)

**French**:
- Admiral Hubert de Brienne (fleet command)
- Marquis de Vaudreuil (naval coordination)
- Various captains (river and lake warfare)

---

## Future Enhancements

Possible additions:
- Naval skills (Gunnery, Sailing, Navigation)
- Ship upgrades and repairs
- Naval reputation system
- Port-to-port travel
- Blockade mechanics
- Prize ships (capturing enemy vessels)

---

## Credits

- **Viking Conquest Team**: Original naval system
- **Taleworlds**: Mount & Blade Warband engine
- **Diplomacy Mod Team**: Base mod framework
- **Historical Consultants**: F&I War naval warfare research

---

## Support

For questions or issues:
1. Check this README first
2. Review the slot system analysis document
3. Examine the implementation examples
4. Test with debug scripts

---

## Version History

- **v1.0** (2024): Initial naval system implementation
  - 8 ship types
  - Slot-based officer preferences
  - Naval battles
  - Ship management

---

## Quick Reference

### Slot Numbers
- 180: Preferred ship type
- 181: Quality bonus
- 182: Max ships bonus
- 183: Naval specialization

### Ship Types
- 1: Ship of the Line
- 2: Frigate
- 3: Sloop
- 4: Brig
- 5: Merchant Ship
- 6: Longboat
- 7: Canoe
- 8: Bateau

### Specializations
- 0: None
- 1: Fleet
- 2: River
- 3: Lake
- 4: Coastal
- 5: Merchant