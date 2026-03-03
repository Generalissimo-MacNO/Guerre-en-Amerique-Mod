# -*- coding: utf-8 -*-
from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

# -----------------------------------------------------------------------
# HISTORICAL NOTES — September 1, 1758
# -----------------------------------------------------------------------
# The French and Indian War (Seven Years' War in North America) is at a
# turning point. Louisbourg fell to the British on July 26, 1758.
# The Forbes Expedition is marching on Fort Duquesne. The Iroquois
# League is watching carefully. The Cherokee alliance with Britain is
# beginning to fracture. The Ohio Valley nations are shifting toward
# the British following the Treaty of Easton (October 1758, imminent).
#
# FACTION ALIGNMENT SUMMARY:
#   Strongly French:  Nouvelle-France, Sept Nations du Canada, Wyandot,
#                     Odawa, Ojibwe, Potawatomi, Shawnee (western bands),
#                     Lenape (western bands), Choctaw
#   Strongly British: British America, Cherokee (for now), Chickasaw
#   Neutral/Spain:    Nueva España (neutral until Family Compact, 1762)
#   Swing/Contested:  Haudenosaunee (Six Nations), Miami, Creek,
#                     Lenape (eastern bands shifting via Treaty of Easton)
#   Wabanaki:         Allied to France but war-weary after Louisbourg
# -----------------------------------------------------------------------

# Generic bandit/outlaw relations shared by all kingdoms
default_kingdom_relations = [("outlaws",-0.05),("deserters", -0.05),("acadiens", -0.02),("frontiersmen", -0.02)]

factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game and their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",   "{!}culture_1", 0, 0.9, [], []),
  ("culture_2",   "{!}culture_2", 0, 0.9, [], []),
  ("culture_3",   "{!}culture_3", 0, 0.9, [], []),
  ("culture_4",   "{!}culture_4", 0, 0.9, [], []),
  ("culture_5",   "{!}culture_5", 0, 0.9, [], []),
  ("culture_6",   "{!}culture_6", 0, 0.9, [], []),
  ("culture_7",   "{!}culture_7", 0, 0.9, [], []),
  ("culture_8",   "{!}culture_8", 0, 0.9, [], []),
  ("culture_9",   "{!}culture_9", 0, 0.9, [], []),
  ("culture_10",  "{!}culture_10", 0, 0.9, [], []),
  ("culture_11",  "{!}culture_11", 0, 0.9, [], []),
  ("culture_12",  "{!}culture_12", 0, 0.9, [], []),
  ("culture_13",  "{!}culture_13", 0, 0.9, [], []),
  ("culture_14",  "{!}culture_14", 0, 0.9, [], []),
  ("culture_15",  "{!}culture_15", 0, 0.9, [], []),
  ("culture_16",  "{!}culture_16", 0, 0.9, [], []),
  ("culture_17",  "{!}culture_17", 0, 0.9, [], []),
  ("culture_18",  "{!}culture_18", 0, 0.9, [], []),
  ("culture_19",  "{!}culture_19", 0, 0.9, [], []),
  ("culture_20",  "{!}culture_20", 0, 0.9, [], []),
  ("culture_player",  "{!}culture_player", 0, 0.9, [], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9,
      [("player_faction",1.00),("outlaws",-0.05),("deserters",-0.02),
       ("acadiens",0.0),("frontiersmen",-0.02)], [], 0xFF4433),

  # -----------------------------------------------------------------------
  # EUROPEAN POWERS
  # -----------------------------------------------------------------------

  # kingdom_1 — British America
  # The thirteen colonies plus Nova Scotia, Newfoundland, and the Caribbean
  # possessions. At war with France. Neutral with Spain (for now).
  # Allied with Cherokee (fragile), Chickasaw, Creek (eastern bands).
  # Hostile to the Sept Nations, Wabanaki, Wyandot, and Ohio Valley nations.
  ("kingdom_1", "British America",       0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.60),("frontiersmen",-0.10),
       ("kingdom_2", -0.90),  # At war with France
       ("kingdom_3", +0.05),  # Neutral with Spain — Family Compact not yet signed
       ("kingdom_4", +0.10),  # Cautious friendship with Iroquois League (Johnson's influence)
       ("kingdom_5", +0.35),  # Allied with Cherokee — but alliance is fraying
       ("kingdom_6", -0.50),  # Hostile to Wabanaki — long history of conflict
       ("kingdom_7", -0.60),  # Hostile to Sept Nations — French-allied raiders
       ("kingdom_8", -0.40),  # Hostile to Wyandot — French allies
       ("kingdom_9", -0.20),  # Tense with Lenape — Treaty of Easton imminent
       ("kingdom_10",-0.30),  # Hostile to Miami — Ohio Valley conflict
       ("kingdom_11",-0.35),  # Hostile to Shawnee — Ohio Valley raids
       ("kingdom_12",-0.30),  # Hostile to Odawa — French allies
       ("kingdom_13",-0.25),  # Hostile to Ojibwe — French allies
       ("kingdom_14",-0.20),  # Tense with Potawatomi
       ("kingdom_15",-0.10),  # Neutral-tense with Choctaw
       ("kingdom_16",+0.40),  # Allied with Chickasaw — long-standing British alliance
       ("kingdom_17",+0.20),  # Friendly with Creek (eastern bands)
       ("kingdom_18",+0.15),  # Catawba — British scouts and allies
       ("kingdom_19",-0.10),  # Illinois — French-allied
       ("kingdom_20", 0.00),  # Mississauga — neutral
      ], [], 0x993333),

  # kingdom_2 — Nouvelle-France
  # New France: Quebec, Acadia remnants, Louisiana, Illinois Country.
  # At war with Britain. Neutral with Spain. Strongly allied with most
  # Native nations of the St. Lawrence, Great Lakes, and Ohio Valley.
  # Louisbourg has just fallen (July 26, 1758) — France is on the defensive.
  ("kingdom_2", "Nouvelle-France",       0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",+0.60),("frontiersmen",-0.30),
       ("kingdom_1", -0.90),  # At war with Britain
       ("kingdom_3", +0.10),  # Friendly with Spain — Bourbon family connection
       ("kingdom_4", -0.15),  # Tense with Iroquois — League leans British
       ("kingdom_5", -0.30),  # Hostile to Cherokee — British allies
       ("kingdom_6", +0.65),  # Strongly allied with Wabanaki
       ("kingdom_7", +0.75),  # Strongly allied with Sept Nations du Canada
       ("kingdom_8", +0.70),  # Strongly allied with Wyandot (Huron of Lorette)
       ("kingdom_9", +0.45),  # Allied with Lenape (western bands)
       ("kingdom_10",+0.40),  # Allied with Miami
       ("kingdom_11",+0.50),  # Allied with Shawnee
       ("kingdom_12",+0.65),  # Strongly allied with Odawa
       ("kingdom_13",+0.60),  # Allied with Ojibwe
       ("kingdom_14",+0.50),  # Allied with Potawatomi
       ("kingdom_15",+0.35),  # Friendly with Choctaw
       ("kingdom_16",-0.40),  # Hostile to Chickasaw — British allies
       ("kingdom_17",-0.10),  # Tense with Creek
       ("kingdom_18",-0.30),  # Hostile to Catawba
       ("kingdom_19",+0.55),  # Allied with Illinois Confederacy
       ("kingdom_20",+0.20),  # Friendly with Mississauga
      ], [], 0x003168),

  # kingdom_3 — Nueva España
  # New Spain: Florida, Cuba, Hispaniola, Mexico. Officially neutral in
  # 1758 — the Family Compact (entering the war) is not signed until 1762.
  # Spain watches the conflict carefully, protecting its Caribbean interests.
  ("kingdom_3", "Nueva España",          0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.05),
       ("kingdom_1", +0.05),  # Neutral with Britain — wary but not hostile
       ("kingdom_2", +0.10),  # Friendly with France — Bourbon family connection
       ("kingdom_4", +0.00),  # Neutral with Iroquois
       ("kingdom_5", +0.10),  # Mildly friendly with Cherokee (trade)
       ("kingdom_6", +0.00),  # Neutral with Wabanaki
       ("kingdom_7", +0.00),  # Neutral with Sept Nations
       ("kingdom_8", +0.00),  # Neutral with Wyandot
       ("kingdom_9", +0.00),  # Neutral with Lenape
       ("kingdom_10",+0.00),  # Neutral with Miami
       ("kingdom_11",+0.00),  # Neutral with Shawnee
       ("kingdom_12",+0.00),  # Neutral with Odawa
       ("kingdom_13",+0.00),  # Neutral with Ojibwe
       ("kingdom_14",+0.00),  # Neutral with Potawatomi
       ("kingdom_15",+0.15),  # Mildly friendly with Choctaw (Gulf Coast trade)
       ("kingdom_16",-0.05),  # Slightly tense with Chickasaw
       ("kingdom_17",+0.10),  # Mildly friendly with Creek (Florida border trade)
       ("kingdom_18",+0.00),  # Neutral with Catawba
       ("kingdom_19",+0.10),  # Friendly with Illinois (Mississippi trade)
       ("kingdom_20",+0.00),  # Neutral with Mississauga
      ], [], 0xFFD700),

  # -----------------------------------------------------------------------
  # NATIVE NATIONS
  # -----------------------------------------------------------------------

  # kingdom_4 — Haudenosaunee (Six Nations Iroquois Confederacy)
  # The Iroquois League: Mohawk, Oneida, Onondaga, Cayuga, Seneca, Tuscarora.
  # Capital: Onondaga (Grand Council fire). Officially neutral but leaning
  # British under Sir William Johnson's influence. The Seneca lean French.
  # This is the most politically complex Native faction — a genuine swing vote.
  # NOTE: The Mohawk are part of this confederacy, NOT a separate faction.
  # The separate "Mohawk" faction (kingdom_7) represents the SEPT NATIONS
  # DU CANADA — a distinct St. Lawrence confederacy that includes the
  # Kahnawake Mohawk but is politically separate from the Iroquois League.
  ("kingdom_4", "Haudenosaunee",         0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.10),("frontiersmen",-0.05),
       ("kingdom_1", +0.10),  # Lean British — Johnson's influence, trade ties
       ("kingdom_2", -0.15),  # Tense with France — but Seneca lean French
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_5", -0.10),  # Historical rivalry with Cherokee
       ("kingdom_6", -0.20),  # Rivalry with Wabanaki — old conflicts
       ("kingdom_7", -0.25),  # Tense with Sept Nations — political split of Mohawk
       ("kingdom_8", -0.30),  # Old rivalry with Wyandot (Huron-Iroquois wars)
       ("kingdom_9", -0.15),  # Tense with Lenape — Iroquois claimed suzerainty
       ("kingdom_10",-0.10),  # Tense with Miami
       ("kingdom_11",-0.10),  # Tense with Shawnee
       ("kingdom_12",-0.05),  # Neutral-tense with Odawa
       ("kingdom_13",-0.05),  # Neutral with Ojibwe
       ("kingdom_14",-0.05),  # Neutral with Potawatomi
       ("kingdom_15", 0.00),  # Neutral with Choctaw (distant)
       ("kingdom_16", 0.00),  # Neutral with Chickasaw (distant)
       ("kingdom_17", 0.00),  # Neutral with Creek (distant)
       ("kingdom_18",+0.05),  # Mildly friendly with Catawba
       ("kingdom_19",-0.10),  # Tense with Illinois
       ("kingdom_20",+0.10),  # Friendly with Mississauga
      ], [], 0x8502F7),

  # kingdom_5 — Ani-Yvwiya (Cherokee Nation)
  # The Cherokee are the largest Native nation in the southeast. They have
  # been British allies since the 1730s, but the alliance is under severe
  # strain in 1758. British settlers are encroaching on Cherokee land, and
  # the Anglo-Cherokee War will break out in 1758-1761. Starting relations
  # reflect a fragile, deteriorating alliance.
  ("kingdom_5", "Ani-Yvwiya",            0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.15),
       ("kingdom_1", +0.35),  # Allied with Britain — but fraying
       ("kingdom_2", -0.30),  # Hostile to France
       ("kingdom_3", +0.10),  # Mildly friendly with Spain (Florida trade)
       ("kingdom_4", -0.10),  # Historical rivalry with Iroquois
       ("kingdom_6", -0.05),  # Neutral with Wabanaki (distant)
       ("kingdom_7", -0.20),  # Hostile to Sept Nations (French allies)
       ("kingdom_8", -0.15),  # Hostile to Wyandot (French allies)
       ("kingdom_9", -0.05),  # Neutral with Lenape
       ("kingdom_10",-0.05),  # Neutral with Miami
       ("kingdom_11",-0.10),  # Tense with Shawnee (Ohio Valley competition)
       ("kingdom_12",-0.10),  # Tense with Odawa
       ("kingdom_13",-0.05),  # Neutral with Ojibwe
       ("kingdom_14",-0.05),  # Neutral with Potawatomi
       ("kingdom_15",-0.20),  # Hostile to Choctaw — long-standing rivalry
       ("kingdom_16",+0.15),  # Friendly with Chickasaw — common British alliance
       ("kingdom_17",-0.15),  # Tense with Creek — territorial rivalry
       ("kingdom_18",+0.20),  # Friendly with Catawba — southeastern alliance
       ("kingdom_19",-0.10),  # Hostile to Illinois
       ("kingdom_20", 0.00),  # Neutral with Mississauga
      ], [], 0xF28305),

  # kingdom_6 — Wabana'ki Mawuhkacik (Wabanaki Confederacy)
  # The Wabanaki (Abenaki, Penobscot, Maliseet, Mi'kmaq, Passamaquoddy)
  # are long-standing French allies and have raided British settlements
  # in New England for decades. War-weary after the fall of Louisbourg,
  # but still firmly in the French camp. Capital: Odanak (St. Francis).
  ("kingdom_6", "Wabana'ki Mawuhkacik",  0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",+0.40),("frontiersmen",-0.10),
       ("kingdom_1", -0.50),  # Hostile to Britain — generations of conflict
       ("kingdom_2", +0.65),  # Strongly allied with France
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_4", -0.20),  # Rivalry with Iroquois
       ("kingdom_5", -0.05),  # Neutral with Cherokee (distant)
       ("kingdom_7", +0.50),  # Allied with Sept Nations — shared French alliance
       ("kingdom_8", +0.30),  # Friendly with Wyandot
       ("kingdom_9", +0.20),  # Friendly with Lenape
       ("kingdom_10",+0.10),  # Mildly friendly with Miami
       ("kingdom_11",+0.15),  # Friendly with Shawnee
       ("kingdom_12",+0.20),  # Friendly with Odawa
       ("kingdom_13",+0.15),  # Friendly with Ojibwe
       ("kingdom_14",+0.10),  # Mildly friendly with Potawatomi
       ("kingdom_15", 0.00),  # Neutral with Choctaw (distant)
       ("kingdom_16",-0.10),  # Tense with Chickasaw
       ("kingdom_17", 0.00),  # Neutral with Creek
       ("kingdom_18",-0.15),  # Tense with Catawba
       ("kingdom_19",+0.20),  # Friendly with Illinois
       ("kingdom_20",+0.15),  # Friendly with Mississauga
      ], [], 0x28694B),

  # kingdom_7 — Sept Nations du Canada (Seven Nations of Canada)
  # A DISTINCT confederacy from the Haudenosaunee. Based on the St. Lawrence
  # valley, centred at Kahnawake (near Montreal). Includes:
  #   - Kahnawake Mohawk (Sault St. Louis)
  #   - Akwesasne Mohawk (St. Regis)
  #   - Kanesetake (Oka — Algonquin, Nipissing, Mohawk)
  #   - Wendake (Huron of Lorette — shared with Wyandot kingdom_8)
  #   - Oswegatchie (Onondaga mission)
  # Firmly allied to France. Provide the most effective Native auxiliary
  # forces for the French army — raiders, scouts, and ambush specialists.
  # Capital: Kahnawake (coordinates near Montreal, ~-105, -230)
  ("kingdom_7", "Sept Nations du Canada", 0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",+0.30),("frontiersmen",-0.20),
       ("kingdom_1", -0.60),  # Hostile to Britain — active raiders
       ("kingdom_2", +0.75),  # Strongly allied with France
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_4", -0.25),  # Tense with Iroquois League — political split
       ("kingdom_5", -0.20),  # Hostile to Cherokee (British allies)
       ("kingdom_6", +0.50),  # Allied with Wabanaki
       ("kingdom_8", +0.55),  # Allied with Wyandot — shared French mission culture
       ("kingdom_9", +0.30),  # Friendly with Lenape
       ("kingdom_10",+0.20),  # Friendly with Miami
       ("kingdom_11",+0.25),  # Friendly with Shawnee
       ("kingdom_12",+0.35),  # Friendly with Odawa
       ("kingdom_13",+0.30),  # Friendly with Ojibwe
       ("kingdom_14",+0.20),  # Friendly with Potawatomi
       ("kingdom_15", 0.00),  # Neutral with Choctaw (distant)
       ("kingdom_16",-0.20),  # Hostile to Chickasaw
       ("kingdom_17",-0.05),  # Neutral with Creek
       ("kingdom_18",-0.20),  # Hostile to Catawba
       ("kingdom_19",+0.30),  # Friendly with Illinois
       ("kingdom_20",+0.20),  # Friendly with Mississauga
      ], [], 0x5e3000),

  # kingdom_8 — Wyandot (Huron-Wendat)
  # The Wyandot (Huron) are among France's oldest and most loyal Native
  # allies. The Huron of Lorette (Wendake, near Quebec) are deeply
  # integrated into French colonial society. The Wyandot of the Great
  # Lakes region (around Detroit/Sandusky) are also French-allied.
  # Capital: Sunyendeand (near Lake Erie/Detroit area)
  ("kingdom_8", "Wyandot",               0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",+0.10),("frontiersmen",-0.15),
       ("kingdom_1", -0.40),  # Hostile to Britain
       ("kingdom_2", +0.70),  # Strongly allied with France
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_4", -0.30),  # Old rivalry with Iroquois (Huron-Iroquois wars)
       ("kingdom_5", -0.15),  # Hostile to Cherokee
       ("kingdom_6", +0.30),  # Friendly with Wabanaki
       ("kingdom_7", +0.55),  # Allied with Sept Nations
       ("kingdom_9", +0.20),  # Friendly with Lenape
       ("kingdom_10",+0.30),  # Friendly with Miami
       ("kingdom_11",+0.25),  # Friendly with Shawnee
       ("kingdom_12",+0.40),  # Friendly with Odawa — Great Lakes alliance
       ("kingdom_13",+0.35),  # Friendly with Ojibwe
       ("kingdom_14",+0.25),  # Friendly with Potawatomi
       ("kingdom_15", 0.00),  # Neutral with Choctaw
       ("kingdom_16",-0.15),  # Tense with Chickasaw
       ("kingdom_17", 0.00),  # Neutral with Creek
       ("kingdom_18",-0.10),  # Tense with Catawba
       ("kingdom_19",+0.30),  # Friendly with Illinois
       ("kingdom_20",+0.20),  # Friendly with Mississauga
      ], [], 0xa6d5ff),

  # kingdom_9 — Lenapehoking (Lenape / Delaware)
  # The Lenape are in a pivotal transitional moment in September 1758.
  # Western Lenape bands have been raiding British settlements in
  # Pennsylvania and Virginia. However, the Treaty of Easton (October 1758)
  # is imminent — the British are about to promise to stop western expansion,
  # which will flip the Lenape toward neutrality/British alignment.
  # Starting relations reflect the pre-Easton hostile stance.
  ("kingdom_9", "Lenapehoking",          0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.20),
       ("kingdom_1", -0.20),  # Tense with Britain — raids ongoing, Easton imminent
       ("kingdom_2", +0.45),  # Allied with France (western bands)
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_4", -0.15),  # Tense with Iroquois — Iroquois claimed suzerainty
       ("kingdom_5", -0.05),  # Neutral with Cherokee
       ("kingdom_6", +0.20),  # Friendly with Wabanaki
       ("kingdom_7", +0.30),  # Friendly with Sept Nations
       ("kingdom_8", +0.20),  # Friendly with Wyandot
       ("kingdom_10",+0.25),  # Friendly with Miami — Ohio Valley neighbors
       ("kingdom_11",+0.35),  # Allied with Shawnee — close Ohio Valley alliance
       ("kingdom_12",+0.15),  # Friendly with Odawa
       ("kingdom_13",+0.10),  # Mildly friendly with Ojibwe
       ("kingdom_14",+0.15),  # Friendly with Potawatomi
       ("kingdom_15", 0.00),  # Neutral with Choctaw
       ("kingdom_16",-0.05),  # Neutral with Chickasaw
       ("kingdom_17", 0.00),  # Neutral with Creek
       ("kingdom_18",-0.05),  # Neutral with Catawba
       ("kingdom_19",+0.20),  # Friendly with Illinois
       ("kingdom_20",+0.10),  # Friendly with Mississauga
      ], [], 0xe0ba81),

  # kingdom_10 — Myaamia (Miami Nation)
  # The Miami control the Wabash River valley and the upper Ohio.
  # Fort Miamis (near modern Fort Wayne) is a key French post in their
  # territory. They are French-allied but pragmatic — they will deal with
  # whoever controls the Ohio Valley trade routes.
  ("kingdom_10", "Myaamia",              0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.10),
       ("kingdom_1", -0.30),  # Hostile to Britain — Ohio Valley conflict
       ("kingdom_2", +0.40),  # Allied with France
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_4", -0.10),  # Tense with Iroquois
       ("kingdom_5", -0.05),  # Neutral with Cherokee
       ("kingdom_6", +0.10),  # Mildly friendly with Wabanaki
       ("kingdom_7", +0.20),  # Friendly with Sept Nations
       ("kingdom_8", +0.30),  # Friendly with Wyandot
       ("kingdom_9", +0.25),  # Friendly with Lenape
       ("kingdom_11",+0.30),  # Friendly with Shawnee — Ohio Valley neighbors
       ("kingdom_12",+0.25),  # Friendly with Odawa
       ("kingdom_13",+0.20),  # Friendly with Ojibwe
       ("kingdom_14",+0.30),  # Friendly with Potawatomi — close neighbors
       ("kingdom_15", 0.00),  # Neutral with Choctaw
       ("kingdom_16",-0.05),  # Neutral with Chickasaw
       ("kingdom_17", 0.00),  # Neutral with Creek
       ("kingdom_18", 0.00),  # Neutral with Catawba
       ("kingdom_19",+0.25),  # Friendly with Illinois — Mississippi valley ties
       ("kingdom_20",+0.10),  # Friendly with Mississauga
      ], [], 0xffff80),

  # kingdom_11 — Shaawana (Shawnee)
  # The Shawnee are among the most active Native participants in the Ohio
  # Valley war. They have been raiding British settlements in Virginia and
  # Pennsylvania since 1755. Strongly French-allied in 1758, though some
  # bands are beginning to reconsider after Braddock's defeat proved the
  # French could not hold the Ohio indefinitely.
  ("kingdom_11", "Shaawana",             0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.20),
       ("kingdom_1", -0.35),  # Hostile to Britain — active raiding
       ("kingdom_2", +0.50),  # Strongly allied with France
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_4", -0.10),  # Tense with Iroquois
       ("kingdom_5", -0.10),  # Tense with Cherokee — Ohio Valley competition
       ("kingdom_6", +0.15),  # Friendly with Wabanaki
       ("kingdom_7", +0.25),  # Friendly with Sept Nations
       ("kingdom_8", +0.25),  # Friendly with Wyandot
       ("kingdom_9", +0.35),  # Allied with Lenape — close Ohio Valley alliance
       ("kingdom_10",+0.30),  # Friendly with Miami
       ("kingdom_12",+0.20),  # Friendly with Odawa
       ("kingdom_13",+0.15),  # Friendly with Ojibwe
       ("kingdom_14",+0.20),  # Friendly with Potawatomi
       ("kingdom_15", 0.00),  # Neutral with Choctaw
       ("kingdom_16",-0.10),  # Tense with Chickasaw
       ("kingdom_17", 0.00),  # Neutral with Creek
       ("kingdom_18",-0.05),  # Neutral with Catawba
       ("kingdom_19",+0.20),  # Friendly with Illinois
       ("kingdom_20",+0.10),  # Friendly with Mississauga
      ], [], 0xff4444),

  # kingdom_12 — Nishnaabe (Odawa / Ottawa)
  # The Odawa are the dominant trading nation of the Great Lakes and among
  # France's most important Native allies. Pontiac (who will lead the 1763
  # uprising) is an Odawa war leader. Their capital Waawiyaatanong is near
  # modern Detroit, a key French post.
  ("kingdom_12", "Nishnaabe",            0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.10),
       ("kingdom_1", -0.30),  # Hostile to Britain
       ("kingdom_2", +0.65),  # Strongly allied with France
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_4", -0.05),  # Neutral-tense with Iroquois
       ("kingdom_5", -0.10),  # Tense with Cherokee
       ("kingdom_6", +0.20),  # Friendly with Wabanaki
       ("kingdom_7", +0.35),  # Friendly with Sept Nations
       ("kingdom_8", +0.40),  # Friendly with Wyandot — Great Lakes alliance
       ("kingdom_9", +0.15),  # Friendly with Lenape
       ("kingdom_10",+0.25),  # Friendly with Miami
       ("kingdom_11",+0.20),  # Friendly with Shawnee
       ("kingdom_13",+0.45),  # Allied with Ojibwe — Anishinaabe kinship
       ("kingdom_14",+0.40),  # Allied with Potawatomi — Anishinaabe kinship
       ("kingdom_15", 0.00),  # Neutral with Choctaw
       ("kingdom_16",-0.10),  # Tense with Chickasaw
       ("kingdom_17", 0.00),  # Neutral with Creek
       ("kingdom_18", 0.00),  # Neutral with Catawba
       ("kingdom_19",+0.25),  # Friendly with Illinois
       ("kingdom_20",+0.30),  # Friendly with Mississauga — Great Lakes neighbors
      ], [], 0xc5a43d),

  # kingdom_13 — Anishinaabe (Ojibwe / Chippewa)
  # The Ojibwe are the largest Anishinaabe nation, controlling the northern
  # Great Lakes from Lake Superior to Lake Huron. French-allied through
  # the fur trade. Their capital Zhaagawaamikong is at Chequamegon Bay
  # on Lake Superior.
  ("kingdom_13", "Anishinaabe",          0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.10),
       ("kingdom_1", -0.25),  # Hostile to Britain
       ("kingdom_2", +0.60),  # Allied with France
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_4", -0.05),  # Neutral with Iroquois
       ("kingdom_5", -0.05),  # Neutral with Cherokee
       ("kingdom_6", +0.15),  # Friendly with Wabanaki
       ("kingdom_7", +0.30),  # Friendly with Sept Nations
       ("kingdom_8", +0.35),  # Friendly with Wyandot
       ("kingdom_9", +0.10),  # Mildly friendly with Lenape
       ("kingdom_10",+0.20),  # Friendly with Miami
       ("kingdom_11",+0.15),  # Friendly with Shawnee
       ("kingdom_12",+0.45),  # Allied with Odawa — Anishinaabe kinship
       ("kingdom_14",+0.50),  # Allied with Potawatomi — Anishinaabe kinship
       ("kingdom_15", 0.00),  # Neutral with Choctaw
       ("kingdom_16",-0.05),  # Neutral with Chickasaw
       ("kingdom_17", 0.00),  # Neutral with Creek
       ("kingdom_18", 0.00),  # Neutral with Catawba
       ("kingdom_19",+0.20),  # Friendly with Illinois
       ("kingdom_20",+0.35),  # Friendly with Mississauga — northern neighbors
      ], [], 0x336699),  # Changed from 0x000000 (black) — invisible on dark map

  # kingdom_14 — Neshnabek (Potawatomi)
  # The Potawatomi control the southern Lake Michigan shoreline and the
  # Chicago portage — a critical link between the Great Lakes and the
  # Mississippi. French-allied through the fur trade and mission system.
  ("kingdom_14", "Neshnabek",            0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.10),
       ("kingdom_1", -0.20),  # Tense with Britain
       ("kingdom_2", +0.50),  # Allied with France
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_4", -0.05),  # Neutral with Iroquois
       ("kingdom_5", -0.05),  # Neutral with Cherokee
       ("kingdom_6", +0.10),  # Mildly friendly with Wabanaki
       ("kingdom_7", +0.20),  # Friendly with Sept Nations
       ("kingdom_8", +0.25),  # Friendly with Wyandot
       ("kingdom_9", +0.15),  # Friendly with Lenape
       ("kingdom_10",+0.30),  # Friendly with Miami — close neighbors
       ("kingdom_11",+0.20),  # Friendly with Shawnee
       ("kingdom_12",+0.40),  # Allied with Odawa — Anishinaabe kinship
       ("kingdom_13",+0.50),  # Allied with Ojibwe — Anishinaabe kinship
       ("kingdom_15", 0.00),  # Neutral with Choctaw
       ("kingdom_16",-0.05),  # Neutral with Chickasaw
       ("kingdom_17", 0.00),  # Neutral with Creek
       ("kingdom_18", 0.00),  # Neutral with Catawba
       ("kingdom_19",+0.30),  # Friendly with Illinois — Mississippi valley ties
       ("kingdom_20",+0.20),  # Friendly with Mississauga
      ], [], 0x680000),

  # kingdom_15 — Chatah (Choctaw Nation)
  # The Choctaw are the largest nation in the southeast after the Cherokee.
  # They have historically been French-allied through the Louisiana trade,
  # but a civil war in the 1740s (the Choctaw Revolt) left them divided.
  # In 1758 they are nominally French-allied but internally fractured.
  ("kingdom_15", "Chatah",               0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.10),
       ("kingdom_1", -0.10),  # Tense with Britain — but some pro-British factions
       ("kingdom_2", +0.35),  # Allied with France — but weakened by civil war
       ("kingdom_3", +0.15),  # Mildly friendly with Spain (Gulf Coast)
       ("kingdom_4", 0.00),   # Neutral with Iroquois (distant)
       ("kingdom_5", -0.20),  # Hostile to Cherokee — long-standing rivalry
       ("kingdom_6", 0.00),   # Neutral with Wabanaki
       ("kingdom_7", +0.10),  # Mildly friendly with Sept Nations
       ("kingdom_8", +0.10),  # Mildly friendly with Wyandot
       ("kingdom_9", 0.00),   # Neutral with Lenape
       ("kingdom_10", 0.00),  # Neutral with Miami
       ("kingdom_11", 0.00),  # Neutral with Shawnee
       ("kingdom_12", 0.00),  # Neutral with Odawa
       ("kingdom_13", 0.00),  # Neutral with Ojibwe
       ("kingdom_14", 0.00),  # Neutral with Potawatomi
       ("kingdom_16",-0.30),  # Hostile to Chickasaw — long-standing war
       ("kingdom_17",-0.10),  # Tense with Creek
       ("kingdom_18",-0.05),  # Neutral with Catawba
       ("kingdom_19",+0.20),  # Friendly with Illinois — Mississippi valley
       ("kingdom_20", 0.00),  # Neutral with Mississauga
      ], [], 0x2e1891),

  # kingdom_16 — Chikasha (Chickasaw Nation)
  # The Chickasaw are the most consistently British-allied Native nation
  # in the southeast. They have fought France and its allies for decades,
  # repelling two French invasions (1736, 1739). Small in number but
  # formidable warriors. Key British allies in the Mississippi valley.
  ("kingdom_16", "Chikasha",             0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.20),("frontiersmen",-0.05),
       ("kingdom_1", +0.40),  # Strongly allied with Britain
       ("kingdom_2", -0.40),  # Hostile to France — decades of conflict
       ("kingdom_3", -0.05),  # Slightly tense with Spain
       ("kingdom_4", 0.00),   # Neutral with Iroquois (distant)
       ("kingdom_5", +0.15),  # Friendly with Cherokee — common British alliance
       ("kingdom_6", -0.10),  # Tense with Wabanaki
       ("kingdom_7", -0.20),  # Hostile to Sept Nations
       ("kingdom_8", -0.15),  # Hostile to Wyandot
       ("kingdom_9", -0.05),  # Neutral with Lenape
       ("kingdom_10",-0.05),  # Neutral with Miami
       ("kingdom_11",-0.10),  # Tense with Shawnee
       ("kingdom_12",-0.10),  # Tense with Odawa
       ("kingdom_13",-0.05),  # Neutral with Ojibwe
       ("kingdom_14",-0.05),  # Neutral with Potawatomi
       ("kingdom_15",-0.30),  # Hostile to Choctaw — long-standing war
       ("kingdom_17",-0.05),  # Neutral-tense with Creek
       ("kingdom_18",+0.10),  # Mildly friendly with Catawba
       ("kingdom_19",-0.20),  # Hostile to Illinois — Mississippi valley conflict
       ("kingdom_20", 0.00),  # Neutral with Mississauga
      ], [], 0xe4af3b),

  # kingdom_17 — Este Mvskokvlke (Muscogee Creek Confederacy)
  # The Creek Confederacy is divided between Upper Creek (more pro-French)
  # and Lower Creek (more pro-British). In 1758 they are attempting to
  # maintain neutrality and play both sides — a classic Creek strategy.
  # Starting relations reflect this careful balancing act.
  ("kingdom_17", "Este Mvskokvlke",      0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.10),
       ("kingdom_1", +0.20),  # Friendly with Britain (Lower Creek)
       ("kingdom_2", +0.10),  # Mildly friendly with France (Upper Creek)
       ("kingdom_3", +0.10),  # Mildly friendly with Spain (Florida border)
       ("kingdom_4", 0.00),   # Neutral with Iroquois
       ("kingdom_5", -0.15),  # Tense with Cherokee — territorial rivalry
       ("kingdom_6", 0.00),   # Neutral with Wabanaki
       ("kingdom_7", -0.05),  # Neutral with Sept Nations
       ("kingdom_8", 0.00),   # Neutral with Wyandot
       ("kingdom_9", 0.00),   # Neutral with Lenape
       ("kingdom_10", 0.00),  # Neutral with Miami
       ("kingdom_11", 0.00),  # Neutral with Shawnee
       ("kingdom_12", 0.00),  # Neutral with Odawa
       ("kingdom_13", 0.00),  # Neutral with Ojibwe
       ("kingdom_14", 0.00),  # Neutral with Potawatomi
       ("kingdom_15",-0.10),  # Tense with Choctaw
       ("kingdom_16",-0.05),  # Neutral-tense with Chickasaw
       ("kingdom_18",+0.10),  # Mildly friendly with Catawba
       ("kingdom_19", 0.00),  # Neutral with Illinois
       ("kingdom_20", 0.00),  # Neutral with Mississauga
      ], [], 0x60b33b),

  # kingdom_18 — Katawba (Catawba Nation)
  # The Catawba are a British-allied nation in the Carolinas, near
  # Charlestowne. Decimated by smallpox in the 1750s but still providing
  # scouts and warriors to the British. A small but loyal British ally
  # in the southeast.
  ("kingdom_18", "Katawba",              0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.15),("frontiersmen",-0.05),
       ("kingdom_1", +0.40),  # Strongly allied with Britain
       ("kingdom_2", -0.30),  # Hostile to France
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_4", +0.05),  # Mildly friendly with Iroquois
       ("kingdom_5", +0.20),  # Friendly with Cherokee — southeastern alliance
       ("kingdom_6", -0.15),  # Tense with Wabanaki
       ("kingdom_7", -0.20),  # Hostile to Sept Nations
       ("kingdom_8", -0.10),  # Tense with Wyandot
       ("kingdom_9", -0.05),  # Neutral with Lenape
       ("kingdom_10", 0.00),  # Neutral with Miami
       ("kingdom_11",-0.05),  # Neutral with Shawnee
       ("kingdom_12", 0.00),  # Neutral with Odawa
       ("kingdom_13", 0.00),  # Neutral with Ojibwe
       ("kingdom_14", 0.00),  # Neutral with Potawatomi
       ("kingdom_15",-0.05),  # Neutral with Choctaw
       ("kingdom_16",+0.10),  # Friendly with Chickasaw
       ("kingdom_17",+0.10),  # Friendly with Creek
       ("kingdom_19",-0.10),  # Tense with Illinois
       ("kingdom_20", 0.00),  # Neutral with Mississauga
      ], [], 0xC8A882),

  # kingdom_19 — Inoka (Illinois Confederacy)
  # The Illinois (Inoka) are a loose confederacy of Algonquian-speaking
  # peoples in the Illinois Country — the Kaskaskia, Peoria, Cahokia,
  # Michigamea, and Tamaroa. Strongly French-allied, their territory
  # straddles the Mississippi and connects Louisiana to the Great Lakes.
  # Severely weakened by the Fox Wars and Iroquois raids but still
  # important to French strategic communications.
  ("kingdom_19", "Inoka",                0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.10),
       ("kingdom_1", -0.30),  # Hostile to Britain
       ("kingdom_2", +0.55),  # Strongly allied with France
       ("kingdom_3", +0.10),  # Mildly friendly with Spain (Mississippi trade)
       ("kingdom_4", -0.10),  # Tense with Iroquois — Iroquois raids in past
       ("kingdom_5", -0.10),  # Tense with Cherokee
       ("kingdom_6", +0.20),  # Friendly with Wabanaki
       ("kingdom_7", +0.30),  # Friendly with Sept Nations
       ("kingdom_8", +0.30),  # Friendly with Wyandot
       ("kingdom_9", +0.20),  # Friendly with Lenape
       ("kingdom_10",+0.25),  # Friendly with Miami — Mississippi valley
       ("kingdom_11",+0.20),  # Friendly with Shawnee
       ("kingdom_12",+0.25),  # Friendly with Odawa
       ("kingdom_13",+0.20),  # Friendly with Ojibwe
       ("kingdom_14",+0.30),  # Friendly with Potawatomi — close neighbors
       ("kingdom_15",+0.20),  # Friendly with Choctaw
       ("kingdom_16",-0.20),  # Hostile to Chickasaw — Mississippi conflict
       ("kingdom_17", 0.00),  # Neutral with Creek
       ("kingdom_18",-0.10),  # Tense with Catawba
       ("kingdom_20",+0.15),  # Friendly with Mississauga
      ], [], 0x8B4513),

  # kingdom_20 — Mississauga (Mississauga Ojibwe)
  # The Mississauga occupy the northern shore of Lake Ontario and the
  # lands between the Great Lakes and the Ottawa River. They moved into
  # this territory after the Huron-Iroquois wars. Loosely French-allied
  # but relatively uninvolved in the main conflict — they serve mainly
  # as a buffer and trade intermediary between the Great Lakes nations
  # and the St. Lawrence valley.
  ("kingdom_20", "Mississauga",          0, 0.9,
      [("outlaws",-0.05),("deserters",-0.02),("acadiens",-0.05),("frontiersmen",-0.05),
       ("kingdom_1", -0.10),  # Tense with Britain
       ("kingdom_2", +0.20),  # Mildly allied with France
       ("kingdom_3", +0.00),  # Neutral with Spain
       ("kingdom_4", +0.10),  # Mildly friendly with Iroquois — Lake Ontario neighbors
       ("kingdom_5", 0.00),   # Neutral with Cherokee
       ("kingdom_6", +0.15),  # Friendly with Wabanaki
       ("kingdom_7", +0.20),  # Friendly with Sept Nations
       ("kingdom_8", +0.20),  # Friendly with Wyandot
       ("kingdom_9", +0.10),  # Mildly friendly with Lenape
       ("kingdom_10",+0.10),  # Mildly friendly with Miami
       ("kingdom_11",+0.10),  # Mildly friendly with Shawnee
       ("kingdom_12",+0.30),  # Friendly with Odawa — Great Lakes neighbors
       ("kingdom_13",+0.35),  # Friendly with Ojibwe — Anishinaabe kinship
       ("kingdom_14",+0.20),  # Friendly with Potawatomi
       ("kingdom_15", 0.00),  # Neutral with Choctaw
       ("kingdom_16", 0.00),  # Neutral with Chickasaw
       ("kingdom_17", 0.00),  # Neutral with Creek
       ("kingdom_18", 0.00),  # Neutral with Catawba
       ("kingdom_19",+0.15),  # Friendly with Illinois
      ], [], 0x7FAACC),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  # Placeholder factions retained for engine compatibility
  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1),("acadiens",0.00)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),

  # Acadiens — displaced Acadian refugees and smugglers operating in the
  # Gulf of St. Lawrence and Maritime regions. Hostile to British authority,
  # loosely allied with French interests but not under French command.
  # (Replaces woku_pirates — internal id kept for save compatibility)
  ("woku_pirates","Acadiens", 0, 0.5,
      [("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),
       ("player_faction",0.0),("kingdom_1",-0.40),("kingdom_2",+0.20)], [], 0x4A6741),

  # Frontiersmen — lawless backcountry settlers, land speculators, and
  # rogue traders operating beyond colonial authority. Hostile to Native
  # nations and colonial governments alike.
  # (Replaces shinano_rebel — internal id kept for save compatibility)
  ("shinano_rebel","Frontiersmen", 0, 0.5,
      [("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),
       ("player_faction",-0.15),("kingdom_4",-0.20),("kingdom_5",-0.10),
       ("kingdom_9",-0.25),("kingdom_11",-0.25)], [], 0x8B7355),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("shinano_rebels","{!}Shinano Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
]

##diplomacy start+ Define these for convenience
dplmc_factions_begin = 1 #As mentioned in the notes above, this is hardcoded and shouldn't be altered.  Deliberately excludes "no faction".
dplmc_non_generic_factions_begin = [x[0] for x in enumerate(factions) if x[1][0] == "merchants"][0] + 1
dplmc_factions_end   = len(factions)
##diplomacy end+

# modmerger_start version=201 type=4
try:
    component_name = "factions"
    var_set = { "factions":factions,"default_kingdom_relations":default_kingdom_relations, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end