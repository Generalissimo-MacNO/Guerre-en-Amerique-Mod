#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Naval System Implementation Script
This script helps integrate the naval system into the Guerre en Amerique mod
"""

import os
import shutil
from datetime import datetime

def backup_file(filepath):
    """Create a backup of the original file"""
    if os.path.exists(filepath):
        backup_path = filepath + f".backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(filepath, backup_path)
        print(f"✓ Backed up: {filepath}")
        return True
    return False

def add_ships_to_items(module_items_path):
    """Add ship items to module_items.py"""
    print("\n=== Adding Ships to module_items.py ===")
    
    if not os.path.exists(module_items_path):
        print(f"✗ Error: {module_items_path} not found")
        return False
    
    backup_file(module_items_path)
    
    # Read the file
    with open(module_items_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ship items to add
    ship_items = '''
# Naval System - Ship Items (French and Indian War vessels)
# Ships function as mounts but provide water travel bonuses

["ship_bateau", "Bateau", [("boat_a", 0)], 
 itp_type_horse|itp_merchandise|itp_civilian, 0, 150,
 abundance(80)|body_armor(5)|difficulty(0)|horse_speed(35)|horse_maneuver(40)|horse_charge(5)|horse_scale(100),
 imodbits_horse_basic],

["ship_whaleboat", "Whaleboat", [("boat_b", 0)], 
 itp_type_horse|itp_merchandise|itp_civilian, 0, 200,
 abundance(70)|body_armor(3)|difficulty(0)|horse_speed(45)|horse_maneuver(50)|horse_charge(3)|horse_scale(95),
 imodbits_horse_basic],

["ship_schooner", "Schooner", [("ship_medium_a", 0)], 
 itp_type_horse|itp_merchandise, 0, 800,
 abundance(50)|body_armor(15)|difficulty(1)|horse_speed(42)|horse_maneuver(38)|horse_charge(10)|horse_scale(110),
 imodbits_horse_basic],

["ship_sloop", "Sloop", [("ship_medium_b", 0)], 
 itp_type_horse|itp_merchandise, 0, 1200,
 abundance(40)|body_armor(20)|difficulty(2)|horse_speed(40)|horse_maneuver(35)|horse_charge(15)|horse_scale(115),
 imodbits_horse_basic],

["ship_brigantine", "Brigantine", [("ship_large_a", 0)], 
 itp_type_horse|itp_merchandise, 0, 2500,
 abundance(20)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(30)|horse_charge(25)|horse_scale(125),
 imodbits_horse_basic|imodbit_champion],

["ship_xebec", "Xebec", [("ship_large_b", 0)], 
 itp_type_horse|itp_merchandise, 0, 2000,
 abundance(25)|body_armor(25)|difficulty(3)|horse_speed(45)|horse_maneuver(42)|horse_charge(20)|horse_scale(120),
 imodbits_horse_basic|imodbit_champion],

["ship_radeau", "Radeau", [("ship_special_a", 0)], 
 itp_type_horse|itp_merchandise, 0, 1500,
 abundance(30)|body_armor(35)|difficulty(2)|horse_speed(30)|horse_maneuver(25)|horse_charge(30)|horse_scale(130),
 imodbits_horse_basic],

["ship_tartane", "Tartane", [("ship_special_b", 0)], 
 itp_type_horse|itp_merchandise, 0, 1800,
 abundance(25)|body_armor(22)|difficulty(2)|horse_speed(43)|horse_maneuver(45)|horse_charge(18)|horse_scale(115),
 imodbits_horse_basic],

# End Naval System Ships
'''
    
    # Find a good insertion point (after horses, before lyre/lute)
    if '["lyre"' in content:
        insertion_point = content.find('["lyre"')
        modified_content = content[:insertion_point] + ship_items + '\n' + content[insertion_point:]
        
        # Write back
        with open(module_items_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        print("✓ Ship items added successfully")
        return True
    else:
        print("✗ Could not find insertion point (looking for lyre item)")
        return False

def add_naval_constants(module_constants_path):
    """Add naval system constants to module_constants.py"""
    print("\n=== Adding Constants to module_constants.py ===")
    
    if not os.path.exists(module_constants_path):
        print(f"✗ Error: {module_constants_path} not found")
        return False
    
    backup_file(module_constants_path)
    
    constants = '''

####################################################
# Naval System Constants
####################################################

# Water area boundaries (adjust based on your map)
water_area_x_min = -100
water_area_x_max = 100
water_area_y_min = -100
water_area_y_max = 100

# Party slots for naval system
slot_party_on_water = 50
slot_party_embarked = 51
slot_party_current_ship = 52
slot_party_movement_speed = 53

# Town slots
slot_town_is_port = 100

# Ship item ID ranges (will be set after compilation)
# These will need to be updated with actual IDs from ID_items.py
'''
    
    with open(module_constants_path, 'a', encoding='utf-8') as f:
        f.write(constants)
    
    print("✓ Naval constants added successfully")
    return True

def create_readme():
    """Create a README for the naval system"""
    readme_content = """# Naval System for Guerre en Amerique Mod

## Installation Complete!

The naval system files have been prepared. Follow these steps to complete integration:

### 1. Review Generated Files
- `naval_system_items.py` - Ship definitions
- `naval_system_scripts.py` - Naval mechanics
- `naval_system_menus.py` - Port and encounter menus
- `NAVAL_SYSTEM_INTEGRATION_GUIDE.md` - Detailed integration guide

### 2. Manual Integration Required
Due to the complexity of the module system, some files need manual integration:

1. **module_scripts.py** - Add scripts from `naval_system_scripts.py`
2. **module_game_menus.py** - Add menus from `naval_system_menus.py`
3. **module_triggers.py** - Add naval triggers (see integration guide)
4. **module_scenes.py** - Add naval combat scenes (see integration guide)

### 3. Compile Module System
```bash
cd "Guerre en Amerique Source/Module_system 1.171"
python build_module.py
```

### 4. Test Features
- Purchase ships at ports
- Embark/disembark
- Water travel
- Naval encounters

### 5. Mesh Requirements
The following meshes need to be available in your mod:
- boat_a, boat_b (small vessels)
- ship_medium_a, ship_medium_b (schooners, sloops)
- ship_large_a, ship_large_b (brigantines, xebecs)
- ship_special_a, ship_special_b (radeaux, tartanes)

You can:
- Use existing boat meshes from the mod
- Import from Viking Conquest
- Create custom meshes

### 6. Historical Accuracy
Ships are based on actual vessels from the French Lake Champlain Fleet (1742-1760):
- Bateaux and whaleboats for transport
- Schooners like the Vigilante (60 tons, 10 guns)
- Xebecs like the Musquelongy (flagship)
- Brigantines like the Duke of Cumberland (155 tons, 16 guns)

### Support
See `NAVAL_SYSTEM_INTEGRATION_GUIDE.md` for detailed instructions and troubleshooting.

### Credits
Based on Viking Conquest naval mechanics, adapted for the French and Indian War period.
"""
    
    with open("NAVAL_SYSTEM_README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✓ README created")

def main():
    """Main implementation function"""
    print("=" * 60)
    print("Naval System Implementation for Guerre en Amerique Mod")
    print("=" * 60)
    
    # Define paths
    base_path = "Guerre-en-Amerique-Mod/Guerre en Amerique Source/Module_system 1.171"
    module_items_path = os.path.join(base_path, "module_items.py")
    module_constants_path = os.path.join(base_path, "module_constants.py")
    
    # Check if base path exists
    if not os.path.exists(base_path):
        print(f"✗ Error: Module system path not found: {base_path}")
        print("Please ensure you're running this script from the correct directory.")
        return
    
    # Perform automated integrations
    success = True
    
    # Add ships to items
    if not add_ships_to_items(module_items_path):
        success = False
    
    # Add constants
    if not add_naval_constants(module_constants_path):
        success = False
    
    # Create documentation
    create_readme()
    
    # Summary
    print("\n" + "=" * 60)
    if success:
        print("✓ Automated integration complete!")
        print("\nNext steps:")
        print("1. Review the backup files created")
        print("2. Follow NAVAL_SYSTEM_INTEGRATION_GUIDE.md for manual steps")
        print("3. Add scripts, menus, and triggers manually")
        print("4. Compile the module system")
        print("5. Test in-game")
    else:
        print("✗ Some integrations failed. Check error messages above.")
        print("You may need to integrate files manually.")
    print("=" * 60)

if __name__ == "__main__":
    main()