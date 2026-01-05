# Naval System for Guerre en Amerique Mod

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
