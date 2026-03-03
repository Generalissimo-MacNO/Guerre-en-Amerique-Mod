# Guerre en Amérique — Mod Development Advisory
### September 1st, 1758 | French and Indian War
*A comprehensive analysis and improvement roadmap based on the current repository state*

---

## Executive Summary of Current State

After a full review of the repository, here is what the mod currently has:

- **17 active factions** (kingdom_1 through kingdom_17), with kingdom_18–20 unused/reserved
- **3 European powers**: British America, Nouvelle-France, Nueva España
- **14 Native nations**: Haudenosaunee (Iroquois), Ani-Yvwiya (Cherokee), Wabanaki, Kanien'keha:ka (Mohawk), Wyandot (Huron), Lenape, Miami, Shawnee, Odawa, Ojibwe, Potawatomi, Choctaw, Chickasaw, Creek
- **34 towns/cities** and a large number of castles (forts) and villages across the map
- **Troop trees** that are still using Gekokujo (Japanese Sengoku) placeholder IDs and equipment — the names have been changed (e.g. "Mohawk Warrior") but the underlying items are still katanas, yumi bows, and samurai armour
- **Freelancer system** integrated (players can enlist in faction armies)
- **Diplomacy system** (dplmc) integrated
- A **Caribbean and Gulf of Mexico** theatre is present (Nassau, Kingston, Havana, Santo Domingo, Veracruz, Cap-Français, Saint Pierre)
- The map covers an enormous area from the Great Lakes to the Caribbean and from the Atlantic to Mexico

The three ideas you've raised are all excellent and historically grounded. Below is a detailed analysis of each, followed by additional recommendations drawn directly from what I found in the code.

---

## 1. The Seven Nations of Canada (Replacing the Mohawk/Iroquois Split)

### The Historical Case

Your instinct here is exactly right. By September 1758, the political landscape of Native diplomacy in the northeast was defined not by individual nations acting alone, but by confederacies and alliance blocs. The **Seven Nations of Canada** (Sept Nations du Canada) — also called the Seven Fires of Caughnawaga — were a distinct confederacy centred around the St. Lawrence valley and closely allied with New France. They included:

1. **Kahnawake** (Mohawk of the Sault)
2. **Akwesasne** (Mohawk of St. Regis)
3. **Kanesetake** (Oka — Algonquin, Nipissing, and Mohawk)
4. **Odanak** (Abenaki — already your `kingdom_6` Wabanaki capital)
5. **Wôlinak** (Bécancour Abenaki)
6. **Wendake** (Huron-Wendat of Lorette — your `kingdom_8` Wyandot)
7. **Kahnawake Mohawk** (sometimes Oswegatchie is listed as the 7th instead)

Meanwhile, the **Haudenosaunee Confederacy** (your `kingdom_4`) represents the Six Nations of the Iroquois League proper — Mohawk, Oneida, Onondaga, Cayuga, Seneca, and Tuscarora — whose capital at Onondaga you already have placed correctly.

### The Problem with the Current Setup

Right now `kingdom_4` (Haudenosaunee) and `kingdom_7` (Kanien'keha:ka/Mohawk) are separate factions with a high positive relation (`+0.9`) to each other, essentially making the Mohawk a vassal-state of the Iroquois. This is historically awkward because the Mohawk *are* the Iroquois — they are the easternmost and most prominent nation of the Haudenosaunee Confederacy. Having them as a separate faction implies a political independence they did not have.

### The Recommended Solution

**Merge `kingdom_7` (Kanien'keha:ka) into `kingdom_4` (Haudenosaunee)** and repurpose `kingdom_7` as the **Sept Nations du Canada**. This is a much more historically meaningful distinction because the Seven Nations were genuinely a separate political body from the Iroquois League, allied to France rather than playing both sides as the League proper did.

**In `module_factions.py`, change:**
```python
# BEFORE
("kingdom_4", "Haudenosaunee", 0, 0.9, [..., ("kingdom_7", +0.9)], [], 0x8502F7),  # Iroquois
("kingdom_7", "Kanien'keha:ka", 0, 0.9, [..., ("kingdom_4", +0.9)], [], 0x5e3000),  # Mohawk

# AFTER
("kingdom_4", "Haudenosaunee", 0, 0.9, [("outlaws",-0.05),("deserters",-0.02),
    ("kingdom_2", -0.3),  # Iroquois lean British but are neutral — tense with France
    ("kingdom_1", +0.1),  # Lean British
    ("kingdom_7", -0.2)], [], 0x8502F7),  # Iroquois Confederacy (Six Nations)
("kingdom_7", "Sept Nations du Canada", 0, 0.9, [("outlaws",-0.05),("deserters",-0.02),
    ("kingdom_2", +0.6),  # Strongly allied to France
    ("kingdom_1", -0.4),  # Hostile to British
    ("kingdom_4", -0.2)], [], 0x5e3000),  # Seven Nations of Canada
```

**In `module_parties.py`, reassign:**
- `town_23` ("Nowdaga") — currently the Mohawk capital — should become **Kahnawake** (near Montréal, coordinates roughly `-105, -230`) for the Seven Nations
- The Haudenosaunee keep `town_20` (Onondaga) as their sole capital, which is historically correct — Onondaga was the seat of the Grand Council

**Troop tree implications:** The Mohawk troop tree (currently `fac_kingdom_7`) should be redesigned as the Seven Nations troop tree, emphasising their role as French-allied raiders and scouts operating out of the St. Lawrence valley. They should have access to French trade muskets at higher tiers, reflecting their close relationship with New France.

**Diplomatic ripple effects:** At the start of 1758, the Iroquois League was in a deeply uncomfortable position — officially neutral but with the Mohawk (under Sir William Johnson's influence) leaning British, and the Seneca and Onondaga leaning French. You could model this by giving `kingdom_4` a near-zero relation with both `kingdom_1` and `kingdom_2`, making them a genuinely unpredictable swing faction. The Seven Nations (`kingdom_7`) should start with a strong French alliance.

---

## 2. Naval System from Viking Conquest

### Why This Mod Needs It More Than Almost Any Other

Looking at your `module_parties.py`, you have towns at Nassau, Kingston, Havana, Santo Domingo, Veracruz, Cap-Français, and Saint Pierre — an entire Caribbean theatre. You also have Louisbourg, Halifax, Boston, Newport, and New York on the Atlantic seaboard. The French and Indian War was not just a land war in the forests; the Royal Navy's dominance of the Atlantic was arguably the decisive strategic factor. The fall of Louisbourg in 1758 (which happened just two months before your start date, on July 26th) was a naval operation. This system is not a luxury — it is essential to the mod's historical authenticity.

### What Viking Conquest's Naval System Provides

Viking Conquest implemented ships as mobile parties on the world map that can carry troops, engage in sea battles, and dock at port settlements. The core components you would need to port are:

**From Viking Conquest's module system:**
- `module_scene_props.py` — ship prop definitions (the physical vessel in battle scenes)
- `module_mission_templates.py` — the sea battle mission template and boarding mechanics
- `module_scripts.py` — ship spawning, movement, and docking scripts
- `module_party_templates.py` — ship party templates with troop capacity slots
- `module_map_icons.py` — ship icons for the world map

### Implementation Plan

**Phase 1 — World Map Ships**

Add ship party types to `module_party_templates.py`. You need at minimum three classes reflecting the period:

```python
# Sloop of War (small, fast — used by all factions for coastal patrol)
("ship_sloop", "Sloop of War", 0, [...], fac_neutral, [...], ai_bhvr_patrol_close, ...)

# Frigate (medium — the workhorse of the Royal Navy and Marine Royale)  
("ship_frigate", "Frigate", 0, [...], fac_neutral, [...], ai_bhvr_patrol_close, ...)

# Ship of the Line (large, slow — strategic asset, rare)
("ship_ship_of_the_line", "Ship of the Line", 0, [...], fac_neutral, [...], ai_bhvr_hold, ...)
```

**Phase 2 — Port Designation**

In `module_parties.py`, your coastal towns already exist. You need to add a `slot_center_is_port` flag (or equivalent constant in `module_constants.py`) and mark the following as ports:
- British: Halifax, Boston, Newport, New York, Nassau, Kingston
- French: Louisbourg, Québec (river port), Cap-Français, Saint Pierre
- Spanish: St. Augustine, Havana, Santo Domingo, Veracruz

**Phase 3 — The St. Lawrence River**

This is the most strategically important waterway in the entire theatre. The St. Lawrence connects Québec to Montréal and is the lifeline of New France. You should implement river travel as a restricted naval lane — ships can move along it but only certain vessel types (bateaux, canoes) can navigate the upper river. This would make the siege of Québec (which happens in 1759, just one year after your start date) a genuinely naval-dependent operation if the player is playing as the British.

**Phase 4 — Canoe Travel for Native Factions**

Critically, the Native nations should have their own watercraft — the birchbark canoe. This should be a fast, low-capacity vessel that can navigate rivers the European ships cannot. This gives Native factions a unique strategic mobility advantage on the map that reflects their historical role as the masters of the interior waterways.

### Historical Flavour Note

By September 1758, the Royal Navy had already demonstrated its dominance. The British player should start with naval superiority in the Atlantic but face French resistance on the St. Lawrence and in the Caribbean. The Spanish are neutral until 1762 (Family Compact), so their Caribbean ports should be off-limits to British attack at game start — a diplomatic trigger could open war with Spain later.

---

## 3. Player-Founded Settlements and the Colonization System

### The Historical Context

1758 is a fascinating moment for colonization mechanics. The British colonies are already well-established and pushing westward over the Appalachians (in violation of various treaties). The French are desperately trying to hold the Ohio Valley with a chain of forts. The Spanish are consolidating their hold on Louisiana and the Gulf Coast. A player-founded settlement system would let the player participate in this frontier expansion directly.

### Design Philosophy

The key design decision is: **what kind of settlement can the player found, and for whom?** I recommend three distinct settlement types, each with different mechanics:

**Type 1: The Trading Post** (cheapest, fastest, available to all factions)
A simple fortified trading post that generates income and improves relations with nearby Native factions. Historically, trading posts like those of the Hudson's Bay Company or the French *postes du pays d'en haut* were the primary interface between European and Native economies. This should cost around 3,000–5,000 denars and require the player to be in a wilderness region away from existing settlements.

**Type 2: The Frontier Fort** (medium cost, requires faction membership)
A palisaded fort that functions as a castle — it can garrison troops, serves as a respawn point for the owning faction's armies, and projects military power into the surrounding region. This mirrors the historical reality of Fort Duquesne, Fort Necessity, Fort Ticonderoga, and dozens of others. Cost: 8,000–15,000 denars. Requires the player to hold a lordship rank within their faction.

**Type 3: The Colonial Town** (most expensive, late-game, requires significant political standing)
A full settlement that can grow into a town, generate tax income, and eventually have its own village dependencies. This is the most ambitious feature and represents the player establishing a genuine colonial presence. Cost: 25,000+ denars. Should require the player to be a high-ranking lord or independent ruler.

### Technical Implementation

The cleanest way to implement this in Warband's module system is to use the **pre-placed disabled parties** approach. Looking at your `module_parties.py`, you already have a pattern of disabled parties (`pf_disabled`) that get activated by scripts. You have `village_f` through `village_s` as disabled native villages. You can extend this pattern:

**In `module_parties.py`, add a block of pre-placed disabled settlement slots:**
```python
# Player-founded settlement slots (activated by colonization scripts)
("player_settlement_1", "Unnamed Settlement", icon_wood_fort|pf_disabled|pf_is_static|pf_always_visible, 
    no_menu, pt_none, fac_player_faction, 0, ai_bhvr_hold, 0, (0,0), []),
("player_settlement_2", "Unnamed Settlement", icon_wood_fort|pf_disabled|pf_is_static|pf_always_visible, 
    no_menu, pt_none, fac_player_faction, 0, ai_bhvr_hold, 0, (0,0), []),
# ... up to player_settlement_5 or so
```

**In `module_game_menus.py`, add a "Found Settlement" option** that appears when the player is in a valid wilderness location (not too close to existing settlements, not in enemy territory):

```python
("found_settlement_menu", "You survey the land around you...", [...],
    [("found_trading_post", [...], "Establish a Trading Post (3,000 gold)", [...]),
     ("found_frontier_fort", [...], "Build a Frontier Fort (10,000 gold)", [...]),
     ("found_colonial_town", [...], "Establish a Colonial Town (25,000 gold)", [...])])
```

**In `module_scripts.py`, add a validation script** that checks:
1. Player is not within 15 map units of an existing settlement
2. Player has sufficient gold
3. Player has the required political rank
4. The location is not in a region claimed by a hostile Native faction (or if it is, triggers a diplomatic consequence)

**The Colonization Consequence System** — this is what makes the feature historically meaningful rather than just a gold sink. When the player founds a settlement in or near Native territory, it should:
- Reduce relations with the nearest Native faction by a significant amount (-0.15 to -0.25)
- Potentially trigger a raid event from that faction
- Improve relations with the player's European faction (+0.05)
- Generate a news event visible to all lords

This models the historical reality that colonial expansion was the *root cause* of the French and Indian War — the British push into the Ohio Valley directly provoked the French-Native alliance that started the conflict.

---

## 4. Additional Recommendations Based on Code Review

### 4a. URGENT: Replace Gekokujo Placeholder Equipment

This is the most pressing issue in the entire codebase. Every single Native troop — Mohawk Warriors, Iroquois spearmen, Cherokee hunters — is currently equipped with **katanas, yumi bows, samurai armour, and arquebus from a Japanese Sengoku mod**. The troop names have been changed but the `itm_` references are all Gekokujo items. This needs to be addressed before any other feature work, as it affects every faction from `kingdom_4` through `kingdom_17`.

You need a dedicated Native American equipment set in `module_items.py` covering:
- **Melee weapons**: Tomahawk (`itm_tomahawk`), war club (`itm_war_club`), scalping knife (`itm_scalping_knife`), spear (`itm_native_spear`)
- **Ranged weapons**: Longbow (`itm_native_longbow`), arrows (`itm_native_arrows`), trade musket (`itm_trade_musket`) for higher-tier troops
- **Armour**: Breechcloth, leggings, moccasins, war paint (cosmetic), deer hide shirt, bear fur cloak for northern nations
- **Shields**: Rawhide shield for some nations

The `.brf` resource file `0_uniform_4native.brf` already exists in your Assets — this is where the 3D meshes should live. The items just need to be properly referenced.

### 4b. The Ohio Valley — A Missing Strategic Theatre

Looking at your map and party placements, the **Ohio Valley** (modern-day western Pennsylvania, Ohio, Kentucky) is conspicuously underpopulated. This is historically the most contested region of the entire war. Fort Duquesne (modern Pittsburgh) was the strategic prize that triggered the conflict. You should add:

- **Fort Duquesne** (French, coordinates approximately `(55, -115)`) — the key French stronghold
- **Fort Pitt** — this should replace Fort Duquesne when the British capture it (a scripted event for 1758–1759)
- **Fort Ligonier** (British, `(30, -110)`) — the British forward base for the Forbes Expedition
- Several Ohio Valley Native villages for the Lenape, Shawnee, and Miami factions, which are currently underrepresented despite being the most active Native participants in the Ohio theatre

### 4c. Diplomatic Starting Conditions Need Historical Calibration

The current faction relations in `module_factions.py` are largely uniform — most Native factions have identical relation values (`-0.05` to outlaws, `-0.02` to deserters) with no differentiation between their actual historical alignments. By September 1758, the diplomatic situation was:

- **Strongly French-allied**: Wyandot, Odawa, Ojibwe, Potawatomi, Lenape (western bands), Shawnee, Seven Nations of Canada
- **Strongly British-allied**: Cherokee (until 1758 breakdown), Chickasaw, Creek (eastern bands)
- **Genuinely neutral/contested**: Haudenosaunee (Six Nations), Miami, Choctaw
- **Shifting**: The Lenape were in the process of switching sides in 1758 due to the Treaty of Easton (October 1758) — this could be a dynamic diplomatic event

I recommend a full pass through `module_factions.py` to set historically accurate starting relations between all Native factions and the three European powers.

### 4d. The Freelancer System — Thematic Opportunity

You already have the Freelancer mod integrated. In the context of 1758, this system maps perfectly onto the historical practice of **ranging companies** and **provincial regiments**. Rather than the generic "enlist as a soldier" framing, consider renaming the Freelancer options to:

- **"Enlist in a Provincial Regiment"** (British colonies — Massachusetts, Virginia, Pennsylvania regiments)
- **"Join the Troupes de la Marine"** (French colonial regulars — distinct from the metropolitan Troupes de Terre)
- **"Serve as a Ranger"** (Rogers' Rangers equivalent — a special high-pay, high-risk option available only to British-aligned players with high Pathfinding skill)
- **"Become a Coureur des Bois"** (French-aligned wilderness scout — available to players with high Tracking and Pathfinding)

### 4e. The Caribbean Theatre — Underutilised

You have six Caribbean towns (Nassau, Kingston, Havana, Santo Domingo, Cap-Français, Saint Pierre) and two Mexican cities (Veracruz, Ciudad de México). This is a significant investment in map real estate that currently seems disconnected from the main northern theatre. Consider:

- **Sugar trade economy**: The Caribbean colonies were the most economically valuable possessions of all three European powers. A trade route system connecting Caribbean ports to Atlantic seaboard cities would give the naval system (proposal #2) an economic purpose beyond just troop transport.
- **Privateering**: A piracy/privateer mechanic using the existing `woku_pirates` faction (currently named "Acadiens") could represent the endemic Caribbean privateering of the period.
- **The Spanish Neutrality Problem**: Spain doesn't enter the war until 1762. Their Caribbean ports (Havana, Santo Domingo, Veracruz) should be neutral but accessible for trade, creating an interesting diplomatic tension.

### 4f. Unused Faction Slots — The Neutral Nations

You have `kingdom_18`, `kingdom_19`, and `kingdom_20` marked as "Unused." Given the historical period, strong candidates for these slots include:

- **The Illinois Confederacy** — a loose alliance of Algonquian-speaking peoples in the Illinois Country, allied to France and important for the Mississippi/Louisiana theatre where you already have New Orleans
- **The Catawba Nation** — a British-allied nation in the Carolinas, near your existing Charlestowne settlement, who provided scouts and warriors to the British
- **The Neutral Nations / Mississauga** — groups in the Great Lakes region who tried to stay out of the conflict

---

## 5. Recommended Development Priority Order

Given the scope of what needs to be done, here is a suggested order of work that builds each feature on a stable foundation:

**Priority 1 — Foundation (Do First)**
Replace all Gekokujo `itm_` references in the Native troop trees with period-appropriate items. Nothing else will feel right until the troops look and fight correctly.

**Priority 2 — Faction Restructuring**
Implement the Seven Nations of Canada as described in Section 1. Calibrate all starting diplomatic relations historically. This affects every system downstream.

**Priority 3 — Ohio Valley Expansion**
Add Fort Duquesne, Fort Ligonier, and the missing Ohio Valley settlements. This fills the most historically important gap in the current map.

**Priority 4 — Colonization System**
Implement the player-founded settlement system (Section 3). This is self-contained enough to develop in parallel with other work and provides a unique gameplay hook.

**Priority 5 — Naval System**
Port the Viking Conquest naval system (Section 2). This is the most technically complex feature and should be tackled after the faction and troop foundations are solid.

**Priority 6 — Caribbean Integration**
Connect the Caribbean theatre to the main game through trade routes and the naval system.

---

## 6. A Note on the Mod's Identity

What makes *Guerre en Amérique* genuinely distinctive — and what should guide every design decision — is that it is set at a moment of profound historical contingency. September 1758 is the turning point of the war. Louisbourg has just fallen. The Forbes Expedition is marching on Fort Duquesne. The Iroquois are watching carefully to see which way the wind blows. The Cherokee alliance is about to fracture. The player is dropped into a world where the outcome is genuinely uncertain, where Native diplomacy matters as much as European military power, and where the wilderness itself is a strategic factor.

Every feature you add should ask: *does this make the player feel the weight of that moment?* The Seven Nations confederacy makes Native politics feel real. The naval system makes the Atlantic and the St. Lawrence feel like the strategic arteries they were. The colonization system makes the player complicit in the very process that caused the war. These are not just gameplay features — they are historical arguments.

---

*Advisory prepared based on full review of module_factions.py, module_parties.py, module_troops.py, module_scripts.py, module_constants.py, and associated asset files in the Guerre en Amérique repository.*