# Naval System Implementation Design for Guerre en Amerique Mod

## Historical Context

Based on research of the French Lake Champlain Fleet (1742-1760), the following ship types were used during the French and Indian War:

### French Vessels
1. **Barque/Schooner (Saintonge)** - 30-40 tons, 2 masts, 4 swivel guns, crew of 6
2. **Topsail Schooner (Vigilante)** - 60 tons, 2 masts, 10 four-pound cannon
3. **Xebecs (Musquelongy, Brochette, Esturgeon)** - 65 feet, polacre-xebec hybrid, 6-10 guns
4. **Tartanes (Grand Diable)** - Row galleys with lateen sails, 3 eighteen-pound cannon, 40-60 oars
5. **Bateaux** - Flat-bottomed boats for troop transport
6. **Whaleboats** - Small rowing boats for scouting

### British Vessels
1. **Brigantine (Duke of Cumberland)** - 155 tons, 16 guns
2. **Sloop (Boscawen)** - 115 tons, 16 guns
3. **Radeau (Ligonier)** - Flat-bottomed sailing barge, 6 guns
4. **Gunboats** - Small boats with single cannon

## Implementation Strategy

### Phase 1: Core Ship Items
Create ship items that players can purchase, capture, or be assigned. Ships will function as:
- Inventory items (can be owned)
- Party modifiers (affect movement speed on water)
- Combat modifiers (provide advantages in naval battles)

### Phase 2: Map Icons & Water Travel
- Create naval map icons for different ship types
- Implement water/land detection system
- Add embark/disembark mechanics at ports/shores
- Modify party movement speed based on ship type

### Phase 3: Naval Encounters
- Create naval encounter system (ship-to-ship battles)
- Implement boarding mechanics
- Add naval combat scenes (ship decks)
- Create AI behavior for naval parties

### Phase 4: Ports & Integration
- Add port locations to existing towns
- Create harbor scenes
- Integrate with faction system
- Add naval missions and quests

## Technical Implementation Details

### Module Files to Modify

1. **module_items.py** - Add ship items
2. **module_parties.py** - Add naval parties
3. **module_party_templates.py** - Add ship party templates
4. **module_map_icons.py** - Add ship map icons
5. **module_scenes.py** - Add naval combat scenes
6. **module_scripts.py** - Add naval mechanics scripts
7. **module_game_menus.py** - Add embark/disembark menus
8. **module_mission_templates.py** - Add naval combat missions
9. **module_triggers.py** - Add naval encounter triggers

### Key Features to Implement

1. **Ship Ownership System**
   - Ships as inventory items
   - Ship capacity (troops, cargo)
   - Ship condition/health
   - Ship upgrades

2. **Water Travel System**
   - Detect water terrain on map
   - Faster movement on water with ships
   - Slower movement on water without ships
   - Embark/disembark at shores

3. **Naval Combat**
   - Ship-to-ship cannon fire
   - Boarding actions
   - Crew management
   - Ship capture mechanics

4. **Port System**
   - Buy/sell ships at ports
   - Repair ships
   - Recruit sailors
   - Naval missions

## Ship Types for Implementation

### Small Vessels (Starting Ships)
- **Bateau** - Basic transport, 20 troops, slow
- **Whaleboat** - Fast scout, 10 troops, very fast

### Medium Vessels
- **Schooner** - 40 troops, medium speed, 4 guns
- **Sloop** - 50 troops, medium speed, 8 guns

### Large Vessels (Late Game)
- **Brigantine** - 80 troops, slow, 16 guns
- **Xebec** - 60 troops, fast, 10 guns

## Viking Conquest Comparison

Viking Conquest's naval system includes:
- Ships as party modifiers
- Faster sea travel
- Naval battles with boarding
- Ship upgrades
- Port system

We will adapt these concepts to the French and Indian War setting with period-appropriate ships and mechanics.

## Next Steps

1. Create ship item definitions
2. Add ship map icons
3. Implement basic embark/disembark system
4. Add naval encounter detection
5. Create naval combat scenes
6. Integrate with existing mod systems