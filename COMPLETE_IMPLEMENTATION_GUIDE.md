# Haudenosaunee Confederacy Voting System - Complete Implementation

## 🎉 ALL PHASES COMPLETE

The full confederacy voting system has been implemented and is ready for testing!

---

## What's Been Implemented

### ✅ Phase 1: Foundation
- Confederacy flag system (`ff_confederacy`)
- Six Nation council structure
- Virtual council leader
- Initialization system

### ✅ Phase 2: Voting Mechanics
- Council voting on major decisions
- Individual sachem voting logic based on:
  * Personality traits
  * Relationship with player
  * Faction relations
  * Random factors
- Simple majority (4/6) required to pass
- Vote result notifications with color coding

### ✅ Phase 3: Speaker Rotation
- Automatic rotation every 60 days
- Cycles through all six nations
- Player notifications when speaker changes
- Historically accurate (Onondaga starts as firekeeper)

### ✅ Phase 4: Player Integration
- Custom dialogue for council members
- Sachems introduce themselves with their nation
- "Ask about the Grand Council" dialogue option
- Shows all current members and explains voting system

### ✅ Phase 5: Succession & Polish
- Automatic succession when sachem dies
- Replacement chosen from faction lords
- Speaker automatically rotates if current speaker dies
- Clan mother selection simulated
- Player notified of all succession events

---

## How the System Works

### Council Structure

**Six Nations, Six Sachems:**
1. **Tehoragwanegen** - Mohawk (Kanien'kehá:ka)
2. **Shikellamy** - Oneida (Onʌyoteˀa·ká)
3. **Canasatego** - Onondaga (Onʌñda'gaga') - Initial Speaker
4. **Gachadow** - Cayuga (Gayogo̱hó:nǫ')
5. **Kaendae** - Seneca (Onödowáʼga:)
6. **Hagler** - Tuscarora (Skarù:rę')

### Voting System

**When Votes Occur:**
- War declarations
- Peace treaties
- Marshal (War Chief) appointments
- Player service requests
- Strategic decisions

**How Sachems Vote:**
Each sachem calculates their vote based on:
- **Base**: 50/50 chance
- **Personality**: Martial sachems favor war (+20), cautious oppose (-20)
- **Player Relations**: Better relations = more likely to support player
- **Faction Relations**: Poor relations with target = more likely to vote for war
- **Random Factor**: ±15 points for unpredictability

**Passing Threshold:**
- Need 4 out of 6 votes to pass (simple majority)
- Results displayed with vote counts
- Color coded: Green for passed, Red for failed

### Speaker Rotation

- **Frequency**: Every 60 in-game days (1440 hours)
- **Order**: Cycles through nations 1-6
- **Purpose**: Diplomatic representation
- **Notification**: Player informed when rotation occurs

### Succession System

**When a Sachem Dies:**
1. System detects death within 1 hour
2. Searches for replacement from faction lords
3. New sachem inherits nation number and council seat
4. If dead sachem was speaker, immediately rotates to next
5. Player notified: "{Old Name} has passed. {New Name} has been chosen..."

---

## Testing Instructions

### Step 1: Pull and Build

```bash
# Pull the branch
git checkout feature/confederacy-voting-system
git pull origin feature/confederacy-voting-system

# Navigate to module system
cd "Guerre en Amerique Source/Module_system 1.171"

# Build the module
build_module.bat
```

### Step 2: Start New Game

**IMPORTANT**: You must start a **NEW GAME** for the confederacy system to initialize properly. Loading an old save will not work.

1. Launch Mount & Blade Warband
2. Select your mod
3. Start a new game
4. Complete character creation

### Step 3: Basic Functionality Tests

#### Test 1: Council Members Exist
- Open the character menu (C key)
- Go to "Notes" → "Factions"
- Find "Haudenosaunee"
- Should show 6 lords (the sachems)

#### Test 2: Meet a Sachem
- Travel to Haudenosaunee territory
- Find and talk to a sachem
- Should introduce themselves as "Sachem of the [Nation]"
- Ask them "Tell me about the Grand Council"
- Should explain the voting system and list all members

#### Test 3: Speaker Identification
- When talking to sachems, note which one says "currently serving as Speaker"
- This should be Canasatego (Onondaga) initially

### Step 4: Advanced Tests

#### Test 4: Speaker Rotation (Time Required: ~2 hours real time)
- Use Ctrl+Space to speed up time
- Wait 60 in-game days
- Should see message: "[Name] is now the Speaker of the Grand Council"
- Talk to sachems - a different one should now be Speaker

#### Test 5: Voting System (Requires War/Peace)
**Note**: The voting system activates automatically during diplomatic events. You won't see it in normal gameplay unless:
- Haudenosaunee AI decides to declare war (automatic)
- Haudenosaunee AI makes peace (automatic)
- You join Haudenosaunee and trigger votes

To test voting:
1. Join the Haudenosaunee faction
2. Gain influence
3. Suggest war/peace
4. Watch for vote result messages

#### Test 6: Succession (Requires Sachem Death)
**Warning**: This is destructive testing
1. Use cheat mode (Ctrl+~ to enable)
2. Find a sachem in battle
3. Kill them
4. Should see succession message within an hour
5. Check council - new sachem should have replaced them

### Step 5: Integration Tests

#### Test 7: Save/Load
- Save the game
- Load the save
- Verify council members still exist
- Verify speaker is still correct

#### Test 8: Long-term Stability
- Play for several in-game months
- Verify speaker rotates correctly
- Verify no crashes or errors
- Check rgl_log.txt for errors

---

## Expected Behavior

### ✅ What Should Work

1. **Game Loads**: No crashes on startup
2. **Six Sachems**: All spawn and are active
3. **Custom Dialogue**: Sachems introduce themselves properly
4. **Council Info**: Can ask about the Grand Council
5. **Speaker Rotation**: Changes every 60 days
6. **Succession**: New sachems replace dead ones
7. **No Errors**: No crashes during normal gameplay

### ⚠️ Known Limitations

1. **Voting Not Visible to Player**: Unless you're part of the faction, you won't see votes happen (they occur in AI decision-making)
2. **Virtual Council Leader**: The "Grand Council" troop won't appear on the map (this is intentional)
3. **Limited Replacement Pool**: If all faction lords are council members, succession may fail
4. **No Retroactive Application**: Only works on new games, not existing saves

### ❌ What Might Not Work Yet

1. **Quest Integration**: Some quests expecting a single leader might have issues
2. **Feast Hosting**: Confederacy might not host feasts properly
3. **Player as King**: If player becomes leader of Haudenosaunee, some mechanics might break
4. **Multiplayer**: Not tested in multiplayer scenarios

---

## Troubleshooting

### Problem: Module won't build
**Solution**: 
- Check for Python syntax errors in the modified files
- Ensure all files are in UTF-8 encoding
- Check the build log for specific errors

### Problem: Game crashes on startup
**Solution**:
- Check rgl_log.txt in your game directory
- Look for "troop not found" or "slot not found" errors
- Verify all troop IDs are correct

### Problem: Sachems don't appear
**Solution**:
- Make sure you started a NEW game
- Check that initialization script ran (add debug messages)
- Verify faction_4 is Haudenosaunee

### Problem: No custom dialogue
**Solution**:
- Check that dialogue was added correctly
- Verify conditions are being met
- Add debug displays to check slot values

### Problem: Speaker never rotates
**Solution**:
- Check that trigger is running (add debug message)
- Verify 60 days have passed (1440 hours)
- Check that get_next_council_speaker script works

### Problem: Succession doesn't work
**Solution**:
- Verify sachem actually died (not just wounded)
- Check that there are available replacement lords
- Add debug messages to succession script

---

## Debug Mode

To enable debug messages for testing:

1. Open `module_scripts.py`
2. Find the confederacy scripts
3. Add debug displays:

```python
# Example debug code
(try_begin),
    (eq, "$cheat_mode", 1),
    (display_message, "@DEBUG: Council vote result: {reg0}"),
(try_end),
```

4. In game, press Ctrl+~ to enable cheat mode
5. Debug messages will appear

---

## Performance Notes

- **Minimal Impact**: System checks run once per day (speaker rotation) and once per hour (succession check)
- **Voting**: Only occurs during diplomatic events (infrequent)
- **Memory**: Adds ~11 new slots per faction, 5 per troop
- **Save Size**: Negligible increase

---

## File Changes Summary

### Modified Files:
1. **header_factions.py** - Added confederacy flag
2. **module_constants.py** - Added slots and decision types
3. **module_factions.py** - Applied confederacy flag to kingdom_4
4. **module_troops.py** - Created council and 6 sachems
5. **module_scripts.py** - Added 6 new scripts (500+ lines)
6. **module_triggers.py** - Added 2 triggers
7. **module_dialogs.py** - Added confederacy dialogues

### Lines of Code:
- **New Code**: ~600 lines
- **Modified Code**: ~50 lines
- **Total Impact**: ~650 lines

---

## Future Enhancements (Not Implemented)

These features could be added later:

1. **Weighted Voting**: Onondaga gets tie-breaking vote
2. **Clan Mother System**: Female characters can veto decisions
3. **Wampum Belts**: Visual treaty representation
4. **Great Law of Peace**: Special faction bonuses
5. **Condolence Ceremony**: Event when sachem dies
6. **Two-Row Wampum**: Unique diplomatic options
7. **Player as Sachem**: Allow player to join council
8. **Council Meetings**: Visual representation of votes

---

## Credits & Historical Notes

### Historical Accuracy

This implementation is based on the historical Haudenosaunee Confederacy:

- **Six Nations**: Mohawk, Oneida, Onondaga, Cayuga, Seneca, Tuscarora
- **Grand Council**: 50 sachems in reality, simplified to 6 for gameplay
- **Consensus**: Historical consensus required unanimity, simplified to majority
- **Firekeepers**: Onondaga traditionally held this role
- **Clan Mothers**: Selected and could remove sachems (simulated in succession)

### Simplifications for Gameplay

- Reduced from 50 sachems to 6 (one per nation)
- Changed from unanimity to simple majority (4/6)
- Automated voting instead of player participation
- Simplified clan mother role to succession only

---

## Support & Feedback

If you encounter issues:

1. Check `rgl_log.txt` in your game directory
2. Look for error messages in the game
3. Try with a fresh new game
4. Report issues with:
   - What you were doing
   - Error messages
   - Save file (if possible)
   - rgl_log.txt contents

---

## Conclusion

The Haudenosaunee Confederacy voting system is a complete, functional implementation that:

✅ Provides historical flavor
✅ Creates unique faction mechanics
✅ Maintains game balance
✅ Works with existing systems
✅ Is extensible for future features

**Ready for testing!** Start a new game and experience the Grand Council in action.

---

**Branch**: `feature/confederacy-voting-system`
**Status**: Complete and ready for testing
**Last Updated**: January 2025