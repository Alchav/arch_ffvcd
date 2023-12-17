from BaseClasses import Location, LocationProgressType
from BaseClasses import ItemClassification, Item
# from .rom_addresses import rom_addresses
# from . import poke_data
loc_id_start = 342000000



class LocationData:
    def __init__(self, name, address = None, parent = None, area = None, event=False, type="Item"):
        self.name = name
        try:
            self.address = int(address, base=16) + loc_id_start
        except:
            print("No address for %s" % name)
            self.address = None
        self.address_hex = address
        self.parent = parent
        self.area = area
        self.event = event
        self.type = type

class FFVCDLocation(Location):
    game = "ffvcd"

    def __init__(self, player, location_data, parent=None):
        super(FFVCDLocation, self).__init__(
            player, location_data.name,
            location_data.address,
            parent
        )
        
        if location_data.type == "Key":
            # self.progress_type = LocationProgressType.PRIORITY
            pass
        else:
            # self.progress_type = LocationProgressType.DEFAULT
            self.item_rule = lambda item: item.classification != ItemClassification.progression
            pass
        
        
        # only allow kuzar to place this seed's items
        if location_data.area == "Kuzar":
            self.item_rule = lambda item: item.player == self.player and item.classification != ItemClassification.progression
        
        # disallow mua from being progression, both town (brave/chicken) and dungeon (non burning vs burning)
        if location_data.area == "Mua":
            self.item_rule = lambda item: item.player == self.player and item.classification != ItemClassification.progression
            
        # disallow lone wolf/under bal castle related checks for some weird progression problems
        if location_data.address in ['C0FB38', 'C0FB3A']:
            self.item_rule = lambda item: item.player == self.player and item.classification != ItemClassification.progression

        


def create_location(world, player, location_data, parent=None):
    return_location = FFVCDLocation(player, location_data, parent)
    return return_location

location_data = [

LocationData("Wind Shrine - Wind Crystal (Knight)", address = "C0FAB2", area = "Wind Shrine"),
LocationData("Wind Shrine - Wind Crystal (BlueMage)", address = "C0FAB4", area = "Wind Shrine"),
LocationData("Wind Shrine - Wind Crystal (BlackMage)", address = "C0FAB6", area = "Wind Shrine"),
LocationData("Wind Shrine - Wind Crystal (WhiteMage)", address = "C0FAB8", area = "Wind Shrine"),
LocationData("Wind Shrine - Wind Crystal (Monk)", address = "C0FABA", area = "Wind Shrine"),
LocationData("Wind Shrine - Wind Crystal (Thief)", address = "C0FABC", area = "Wind Shrine"),
LocationData("Karnak - Fire Crystal (Trainer)", address = "C0FABE", area = "Karnak"),
LocationData("Karnak - Fire Crystal (Geomancer)", address = "C0FAC0", area = "Karnak"),
LocationData("Karnak - Fire Crystal (Ninja)", address = "C0FAC2", area = "Karnak"),
LocationData("Crescent Island - Black Choco Crystals (Bard)", address = "C0FAC4", area = "Crescent Island"),
LocationData("Crescent Island - Black Choco Crystals (Hunter)", address = "C0FAC6", area = "Crescent Island"),
LocationData("Flying Lonka Ruins - Earth Crystal (Samurai)", address = "C0FAC8", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Earth Crystal (Dragoon)", address = "C0FACA", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Earth Crystal (Chemist)", address = "C0FACC", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Earth Crystal (Dancer)", address = "C0FACE", area = "Flying Lonka Ruins"),
LocationData("Istory Falls - Leviathan Esper (Levia)", address = "C0FAD0", area = "Istory Falls"),
LocationData("Karnak - Titan (Titan)", address = "C0FAD2", area = "Karnak"),
LocationData("Exdeath's Castle - Carbuncle (Crbnkl)", address = "C0FAD4", area = "Exdeath's Castle"),
LocationData("Pirate's Cave - Syldra (Syldra)", address = "C0FAD6", area = "Pirate's Cave"),
LocationData("Bal Castle - Odin (Odin)", address = "C0FAD8", area = "Bal Castle"),
LocationData("Phoenix Tower - Phoenix (Phenix)", address = "C0FADA", area = "Phoenix Tower"),
LocationData("Hiryuu Valley - Bahamut (Bahmut)", address = "C0FADC", area = "Hiryuu Valley"),
LocationData("Crescent Island - Life Song (Vitality)", address = "C0FADE", area = "Crescent Island"),
LocationData("Lix - Temptation Song at Lix (Charm)", address = "C0FAE0", area = "Lix"),
LocationData("Istory Falls - Love Song at Istory (Love)", address = "C0FAE2", area = "Istory Falls"),
LocationData("Kelb - Requiem Song at Kelb (Requiem)", address = "C0FAE4", area = "Kelb"),
LocationData("Surgate Castle - Speed Song at Surgate (Speed)", address = "C0FAE6", area = "Surgate Castle"),
LocationData("Ancient Library - Magic Song at Ancient Library (Magic)", address = "C0FAE8", area = "Ancient Library"),
LocationData("Crescent Island - Power Song from Crescent Town (Power)", address = "C0FAEA", area = "Crescent Island"),
LocationData("Crescent Island - Hero Song from Crescent Town (Hero)", address = "C0FAEC", area = "Crescent Island"),
LocationData("Fork Tower - Fork Tower, two Magics (Holy)", address = "C0FAEE", area = "Fork Tower"),
LocationData("Fork Tower - Fork Tower, two Magics (Flare)", address = "C0FAF0", area = "Fork Tower"),
LocationData("Great Trench - Meteo (Meteo)", address = "C0FAF2", area = "Great Trench"),
LocationData("Wind Shrine - 5 potions (from NPC) (Potion)", address = "C0FAF4", area = "Wind Shrine"),
LocationData("Pirate's Cave - 8 potions (from NPC) (Potion)", address = "C0FAF6", area = "Pirate's Cave"),
LocationData("Tycoon Castle - Chancellor at Tycoon (Healing Staff)", address = "C0FAF8", area = "Tycoon Castle"),
LocationData("North Mountain - Magisa & Forza (Mythril Helm)", address = "C0FAFA", area = "North Mountain"),
LocationData("Kelb - CornaJar at Kelb (CornaJar)", address = "C0FAFC", area = "Kelb"),
LocationData("Rugor - Ribbon from girl in Rugor (Ribbon)", address = "C0FAFE", area = "Rugor"),
LocationData("Kuzar - 12 Kuzar Events (Assassin)", address = "C0FB02", area = "Kuzar"),
LocationData("Kuzar - 12 Kuzar Events (Apollo's Harp)", address = "C0FB04", area = "Kuzar"),
LocationData("Kuzar - 12 Kuzar Events (Excalibur)", address = "C0FB06", area = "Kuzar"),
LocationData("Kuzar - 12 Kuzar Events (Flame Whip)", address = "C0FB08", area = "Kuzar"),
LocationData("Kuzar - 12 Kuzar Events (Earth Bell)", address = "C0FB0A", area = "Kuzar"),
LocationData("Kuzar - 12 Kuzar Events (Holy Lance)", address = "C0FB0C", area = "Kuzar"),
LocationData("Kuzar - 12 Kuzar Events (Masamune)", address = "C0FB0E", area = "Kuzar"),
LocationData("Kuzar - 12 Kuzar Events (Wizard Rod)", address = "C0FB10", area = "Kuzar"),
LocationData("Kuzar - 12 Kuzar Events (Rune Axe)", address = "C0FB12", area = "Kuzar"),
LocationData("Kuzar - 12 Kuzar Events (Sage's Staff)", address = "C0FB14", area = "Kuzar"),
LocationData("Kuzar - 12 Kuzar Events (Hardened Dagger)", address = "C0FB16", area = "Kuzar"),
LocationData("Kuzar - 12 Kuzar Events (Yoichi Bow)", address = "C0FB18", area = "Kuzar"),
LocationData("Walse - Shiva (Shiva)", address = "C0FB1A", area = "Walse"),
LocationData("Ancient Library - Ifrit (Ifrit)", address = "C0FB1C", area = "Ancient Library"),
LocationData("Walse - Water Crystal (Samurai)", address = "C0FB1E", area = "Walse"),
LocationData("Walse - Water Crystal (Berserker)", address = "C0FB20", area = "Walse"),
LocationData("Walse - Water Crystal (MysticKnight)", address = "C0FB22", area = "Walse"),
LocationData("Walse - Water Crystal (TimeMage)", address = "C0FB24", area = "Walse"),
LocationData("Walse - Water Crystal (Summoner)", address = "C0FB26", area = "Walse"),
LocationData("Mua - Brave Blade (Brave Blade)", address = "C0FB28", area = "Mua"),
LocationData("Mua - Chicken Knife (Chicken Knife)", address = "C0FB2A", area = "Mua"),
LocationData("Tycoon Castle - Tycoon Castle Cabin (Cabin (1))", address = "C0FB2C", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Cabin (Cabin (2))", address = "C0FB2E", area = "Tycoon Castle"),
LocationData("Walse - Walse Tower Chest (GoGo)", address = "C0FB30", area = "Walse"),
LocationData("Pyramid - Pyramid Top (Pyramid Tablet)", address = "C0FB32", area = "Pyramid"),
LocationData("Istory Falls - Toad Event (Toad)", address = "C0FB34", area = "Istory Falls"),
LocationData("Mua - Aegis Shield Chest (Aegis Shield)", address = "C0FB36", area = "Mua"),
LocationData("Carwen - Lone Wolf Barrel (Cabin)", address = "C0FB38", area = "Carwen"),
LocationData("Bal Castle - Lone Wolf Chest (Thunder Whip)", address = "C0FB3A", area = "Bal Castle"),
LocationData("Bal Castle - Moat Item (Epee)", address = "C0FB3C", area = "Bal Castle"),
LocationData("Bal Castle - Shop Backdoor (Lamia Harp)", address = "C0FB3E", area = "Bal Castle"),
LocationData("Istory Falls - Top of the Falls (Magic Lamp)", address = "C0FB40", area = "Istory Falls"),
LocationData("Wind Shrine - Wind Shrine Chest (Broadsword)", address = "D13212", area = "Wind Shrine"),
LocationData("Tule - Beginner's House Chest (Ether)", address = "D13216", area = "Tule"),
LocationData("Tule - Beginner's House Chest (100)", address = "D1321A", area = "Tule"),
LocationData("Tule - Beginner's House Chest (Potion)", address = "D1321E", area = "Tule"),
LocationData("Tule - Beginner's House Chest (Phoenix Down)", address = "D13222", area = "Tule"),
LocationData("Tule - Beginner's House Chest (Tent)", address = "D13226", area = "Tule"),
LocationData("Tule - Beginner's House Chest MIB 1 (Leather Shoes)", address = "D1322A", area = "Tule"),
LocationData("Pirate's Cave - Pirate's Cave Chest (Leather Cap)", address = "D1322E", area = "Pirate's Cave"),
LocationData("Pirate's Cave - Pirate's Cave Chest (Tent)", address = "D13232", area = "Pirate's Cave"),
LocationData("Pirate's Cave - Pirate's Cave Chest (Ether)", address = "D13236", area = "Pirate's Cave"),
LocationData("Pirate's Cave - Pirate's Cave Chest (300)", address = "D1323A", area = "Pirate's Cave"),
LocationData("Wind Shrine - Wind Shrine Chest (Tent)", address = "D1323E", area = "Wind Shrine"),
LocationData("Wind Shrine - Wind Shrine Chest (Leather Cap)", address = "D13242", area = "Wind Shrine"),
LocationData("Wind Shrine - Wind Shrine Chest (Staff)", address = "D13246", area = "Wind Shrine"),
LocationData("Tule - Tule Barrel (150)", address = "D1324A", area = "Tule"),
LocationData("Tule - Tule Box (Leather Shoes)", address = "D1324E", area = "Tule"),
LocationData("Tule - Tule Barrel (Potion)", address = "D13252", area = "Tule"),
LocationData("Tule - Tule Box (Tent)", address = "D13256", area = "Tule"),
LocationData("Tule - Tule Bush (Phoenix Down)", address = "D1325A", area = "Tule"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Flail)", address = "D1325E", area = "Ship Graveyard"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Phoenix Down (1))", address = "D13262", area = "Ship Graveyard"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Tent)", address = "D13266", area = "Ship Graveyard"),
LocationData("Ship Graveyard - Ship Graveyard Box (990)", address = "D1326A", area = "Ship Graveyard"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Potion)", address = "D1326E", area = "Ship Graveyard"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Antidote (1))", address = "D13272", area = "Ship Graveyard"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Antidote (2))", address = "D13276", area = "Ship Graveyard"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Phoenix Down (2))", address = "D1327A", area = "Ship Graveyard"),
LocationData("Carwen - Carwen Barrel (Antidote)", address = "D1327E", area = "Carwen"),
LocationData("Carwen - Carwen Box (Ice Rod)", address = "D13282", area = "Carwen"),
LocationData("Carwen - Carwen Pot (1000)", address = "D13286", area = "Carwen"),
LocationData("North Mountain - North Mountain Chest (Soft)", address = "D1328A", area = "North Mountain"),
LocationData("North Mountain - North Mountain Chest (Phoenix Down)", address = "D1328E", area = "North Mountain"),
LocationData("Walse - Walse Town Pot (Glasses)", address = "D13292", area = "Walse"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Hi-Potion)", address = "D13296", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Ether (1))", address = "D1329A", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Barrel (Elixir)", address = "D1329E", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Barrel (Phoenix Down)", address = "D132A2", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Barrel (Cabin)", address = "D132A6", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Ether 2)", address = "D132AA", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Elixir)", address = "D132AE", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Phoenix Down)", address = "D132B2", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Maiden's Kiss)", address = "D132B6", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Chest (Shuriken)", address = "D132BA", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Chest (Giyaman)", address = "D132BE", area = "Tycoon Castle"),
LocationData("Tycoon Castle - Tycoon Castle Chest (Katana)", address = "D132C2", area = "Tycoon Castle"),
LocationData("Walse - Walse Castle Chest (Elf Cape)", address = "D132C6", area = "Walse"),
LocationData("Walse - Walse Castle Pot (1000 (1))", address = "D132CA", area = "Walse"),
LocationData("Walse - Walse Castle Pot (Drag)", address = "D132CE", area = "Walse"),
LocationData("Walse - Walse Castle Pot (1000 (2))", address = "D132D2", area = "Walse"),
LocationData("Walse - Walse Castle Box (490)", address = "D132D6", area = "Walse"),
LocationData("Walse - Walse Castle Barrel (Tent)", address = "D132DA", area = "Walse"),
LocationData("Walse - Walse Castle Barrel (Phoenix Down)", address = "D132DE", area = "Walse"),
LocationData("Walse - Walse Tower Chest (Silk robe)", address = "D132E2", area = "Walse"),
LocationData("Walse - Walse Tower Chest (Maiden's Kiss)", address = "D132E6", area = "Walse"),
LocationData("Walse - Walse Tower Chest (Silver Armlet)", address = "D132EA", area = "Walse"),
LocationData("Walse - Walse Tower Chest (Ether)", address = "D132EE", area = "Walse"),
LocationData("Tycoon Castle - Tycoon Meteor Chest (Phoenix Down)", address = "D132F2", area = "Tycoon Castle"),
LocationData("Karnak - Karnak Castle Chest MIB 1 (Heavy Spear)", address = "D132F6", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest MIB 2 (Thunder Scroll)", address = "D132FA", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (2000 (1))", address = "D132FE", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest MIB 3 (Elixir)", address = "D13302", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (Elixir (1))", address = "D13306", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (Elixir (2))", address = "D1330A", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (2000 (2))", address = "D1330E", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (Elixir (3))", address = "D13312", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (Elixir (4))", address = "D13316", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (Ribbon)", address = "D1331A", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (Shuriken)", address = "D1331E", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (2000 (3))", address = "D13322", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (Elixir (5))", address = "D13326", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (Elf Cape)", address = "D1332A", area = "Karnak"),
LocationData("Karnak - Karnak Castle Chest (Guardian)", address = "D1332E", area = "Karnak"),
LocationData("Steamship - Karnak Town Barrel (Fire Rod)", address = "D13332", area = "Steamship"),
LocationData("Steamship - Steamship Chest (Cabin)", address = "D13336", area = "Steamship"),
LocationData("Steamship - Steamship Chest (Phoenix Down)", address = "D1333A", area = "Steamship"),
LocationData("Steamship - Steamship Chest (Elixir)", address = "D1333E", area = "Steamship"),
LocationData("Steamship - Steamship Chest (GrnBeret)", address = "D13342", area = "Steamship"),
LocationData("Steamship - Steamship Chest (Thief's Glove)", address = "D13346", area = "Steamship"),
LocationData("Steamship - Steamship Chest (Elixir)", address = "D1334A", area = "Steamship"),
LocationData("Ancient Library - Ancient Library Chest (Ether)", address = "D1334E", area = "Ancient Library"),
LocationData("Ancient Library - Ancient Library Chest (Phoenix Down)", address = "D13352", area = "Ancient Library"),
LocationData("Ancient Library - Ancient Library Chest (Stealth Suit)", address = "D13356", area = "Ancient Library"),
LocationData("Jacole - Jacole Cave Chest (Shuriken)", address = "D1335A", area = "Jacole"),
LocationData("Jacole - Jacole Cave Chest (Tent)", address = "D1335E", area = "Jacole"),
LocationData("Ruined City - Ruined City Chest (Shuriken)", address = "D13362", area = "Ruined City"),
LocationData("Ruined City - Ruined City Chest (Shuriken)", address = "D13366", area = "Ruined City"),
LocationData("Ruined City - Ruined City Chest (Size)", address = "D1336A", area = "Ruined City"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Golden Armor)", address = "D1336E", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Elixir)", address = "D13372", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Phoenix Down)", address = "D13376", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Golden Shield)", address = "D1337A", area = "Flying Lonka Ruins"),
LocationData("Steamship - Steamship Chest (Mythril Glove)", address = "D1337E", area = "Steamship"),
LocationData("Steamship - Steamship Chest (Elixir)", address = "D13382", area = "Steamship"),
LocationData("Steamship - Steamship Chest (Full Moon)", address = "D13386", area = "Steamship"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Hi-Potion)", address = "D1338A", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (5000)", address = "D1338E", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Shuriken)", address = "D13392", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Ancient Sword)", address = "D13396", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Full Moon)", address = "D1339A", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Power Wrist)", address = "D1339E", area = "Flying Lonka Ruins"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Ether)", address = "D133A2", area = "Flying Lonka Ruins"),
LocationData("Exdeath's Castle - Flying Lonka Ruins Chest (Cabin)", address = "D133A6", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Ether)", address = "D133AA", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Diamond Shield)", address = "D133AE", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Ice Shield)", address = "D133B2", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Ether)", address = "D133B6", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Elixir)", address = "D133BA", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Gale Bow)", address = "D133BE", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (IceBrand)", address = "D133C2", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Kotetsu)", address = "D133C6", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (9900)", address = "D133CA", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Elixir)", address = "D133CE", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (8000)", address = "D133D2", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (DblLance)", address = "D133D6", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Partisan)", address = "D133DA", area = "Exdeath's Castle"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Pinwheel)", address = "D133DE", area = "Exdeath's Castle"),
LocationData("Moogle Village - Moogle Cave Chest (4400)", address = "D133E2", area = "Moogle Village"),
LocationData("Moogle Village - Moogle Cave Chest (Phoenix Down)", address = "D133E6", area = "Moogle Village"),
LocationData("Moogle Village - Moogle Village Chest (Cabin)", address = "D133EA", area = "Moogle Village"),
LocationData("Moogle Village - Moogle Village Chest (Dancing Dagger)", address = "D133EE", area = "Moogle Village"),
LocationData("Moogle Village - Moogle Village Chest (1)", address = "D133F2", area = "Moogle Village"),
LocationData("Moogle Village - Moogle Village Chest (10000)", address = "D133F6", area = "Moogle Village"),
LocationData("Moogle Village - Moogle Village Chest (Phoenix Down)", address = "D133FA", area = "Moogle Village"),
LocationData("Moogle Village - Moogle Village Chest (Ether)", address = "D133FE", area = "Moogle Village"),
LocationData("Moogle Village - Moogle Village Chest (Elf Cape)", address = "D13402", area = "Moogle Village"),
LocationData("Bal Castle - Bal Castle Chest (Angel Gwn)", address = "D13406", area = "Bal Castle"),
LocationData("Bal Castle - Bal Castle Chest (Hero Drink)", address = "D1340A", area = "Bal Castle"),
LocationData("Bal Castle - Bal Castle Chest (Exit)", address = "D1340E", area = "Bal Castle"),
LocationData("Hiryuu Valley - Hiryuu Valley Skull (Bone Mail)", address = "D13412", area = "Hiryuu Valley"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (5000)", address = "D13416", area = "Hiryuu Valley"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Cabin)", address = "D1341A", area = "Hiryuu Valley"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (7000)", address = "D1341E", area = "Hiryuu Valley"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Hypno Helm)", address = "D13422", area = "Hiryuu Valley"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Air Blade)", address = "D13426", area = "Hiryuu Valley"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Phoenix Down)", address = "D1342A", area = "Hiryuu Valley"),
LocationData("Surgate Castle - Surgate Castle Chest (5000)", address = "D1342E", area = "Surgate Castle"),
LocationData("Surgate Castle - Surgate Castle Chest (Float)", address = "D13432", area = "Surgate Castle"),
LocationData("Barrier Tower - Barrier Tower Chest MIB 1 (Drain Sword)", address = "D13436", area = "Barrier Tower"),
LocationData("Barrier Tower - Barrier Tower Chest (9000)", address = "D1343A", area = "Barrier Tower"),
LocationData("Barrier Tower - Barrier Tower Chest (18000)", address = "D1343E", area = "Barrier Tower"),
LocationData("Barrier Tower - Barrier Tower Chest MIB 2 (Gold Hairpin)", address = "D13442", area = "Barrier Tower"),
LocationData("Mua - Mua Town Barrel (Guardian)", address = "D13446", area = "Mua"),
LocationData("Mua - Mua Forest Chest (2500)", address = "D1344A", area = "Mua"),
LocationData("Mua - Mua Forest Chest (Ether)", address = "D1344E", area = "Mua"),
LocationData("Mua - Mua Forest Chest (4900)", address = "D13452", area = "Mua"),
LocationData("Mua - Mua Forest Chest (Phoenix Down)", address = "D13456", area = "Mua"),
LocationData("Mua - Mua Forest Chest (9500)", address = "D1345A", area = "Mua"),
LocationData("Mua - Mua Forest Chest (Soot)", address = "D1345E", area = "Mua"),
LocationData("Mua - Mua Forest Chest (Flametongue)", address = "D13462", area = "Mua"),
LocationData("Mua - Mua Forest Chest (Cabin)", address = "D13466", area = "Mua"),
LocationData("Mua - Mua Forest Chest (Giant Drink)", address = "D1346A", area = "Mua"),
LocationData("Mua - Mua Forest Chest (Elixir)", address = "D1346E", area = "Mua"),
LocationData("Mua - Mua Forest Chest (Morning Star)", address = "D13472", area = "Mua"),
LocationData("Solitary Island - Solitary Island Chest (Ether)", address = "D13476", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest (DragonFang)", address = "D1347A", area = "Solitary Island"),
LocationData("Pyramid - Pyramid Chest (Elixir)", address = "D1347E", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Elixir)", address = "D13482", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest MIB 1 (Black Robe)", address = "D13486", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Thornlet)", address = "D1348A", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest MIB 2 (DarkMatter)", address = "D1348E", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest MIB 3 (Crystal Armor)", address = "D13492", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Cursed Ring)", address = "D13496", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Ice Shield)", address = "D1349A", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Flame Shield)", address = "D1349E", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (DarkMatter)", address = "D134A2", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (White Robe)", address = "D134A6", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (DarkSuit)", address = "D134AA", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (DarkMatter)", address = "D134AE", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (DarkMatter)", address = "D134B2", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (DarkMatter)", address = "D134B6", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (9000)", address = "D134BA", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (8000)", address = "D134BE", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Earth Hammer)", address = "D134C2", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (10000)", address = "D134C6", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Cabin)", address = "D134CA", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Elixir)", address = "D134CE", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (12000)", address = "D134D2", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (DarkMatter)", address = "D134D6", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Elixir)", address = "D134DA", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (DarkMatter)", address = "D134DE", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Guard Ring)", address = "D134E2", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Ribbon)", address = "D134E6", area = "Pyramid"),
LocationData("Pyramid - Pyramid Chest (Gold Hairpin)", address = "D134EA", area = "Pyramid"),
LocationData("Solitary Island - Solitary Island Chest (12000)", address = "D134EE", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest (Hi-Potion)", address = "D134F2", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest (Protect Drink)", address = "D134F6", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest (BeastKiller)", address = "D134FA", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest MIB 1 (RisingSun)", address = "D134FE", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest (Ether)", address = "D13502", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest MIB 2 (Guard Ring)", address = "D13506", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest (Crystal Helm)", address = "D1350A", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest (9000)", address = "D1350E", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest (Elixir)", address = "D13512", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest (DarkMatter)", address = "D13516", area = "Solitary Island"),
LocationData("Solitary Island - Solitary Island Chest (Circlet)", address = "D1351A", area = "Solitary Island"),
LocationData("Fork Tower - Fork Tower L. Chest (Ether)", address = "D1351E", area = "Fork Tower"),
LocationData("Fork Tower - Fork Tower L. Chest (Wonder Wand)", address = "D13522", area = "Fork Tower"),
LocationData("Fork Tower - Fork Tower R. Chest (Hi-Potion)", address = "D13526", area = "Fork Tower"),
LocationData("Fork Tower - Fork Tower R. Chest (Defender Sword)", address = "D1352A", area = "Fork Tower"),
LocationData("Great Trench - Great Trench Chest (Water Scroll)", address = "D1352E", area = "Great Trench"),
LocationData("Great Trench - Great Trench Chest (Flame Ring)", address = "D13532", area = "Great Trench"),
LocationData("Great Trench - Great Trench Chest (DragonFang)", address = "D13536", area = "Great Trench"),
LocationData("Great Trench - Great Trench Chest (Ether)", address = "D1353A", area = "Great Trench"),
LocationData("Great Trench - Great Trench Chest (Phoenix Down)", address = "D1353E", area = "Great Trench"),
LocationData("Istory Falls - Great Trench Chest (Kaiser Knuckles)", address = "D13542", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (Ether)", address = "D13546", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (TurtleShell)", address = "D1354A", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (Air Knife)", address = "D1354E", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (Giant Drink)", address = "D13552", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (RuneEdge)", address = "D13556", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (Guard Ring)", address = "D1355A", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (Wall Ring)", address = "D1355E", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (Phoenix Down)", address = "D13562", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (Enhancer)", address = "D13566", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (12000)", address = "D1356A", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (Artemis Bow)", address = "D1356E", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (Pinwheel)", address = "D13572", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (Aegis Shield)", address = "D13576", area = "Istory Falls"),
LocationData("Istory Falls - Istory Falls Chest (Giant's Axe)", address = "D1357A", area = "Istory Falls"),
LocationData("Phoenix Tower - Phoenix Tower Pot (5000)", address = "D1357E", area = "Phoenix Tower"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down)", address = "D13582", area = "Phoenix Tower"),
LocationData("Phoenix Tower - Phoenix Tower Pot (10000)", address = "D13586", area = "Phoenix Tower"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down)", address = "D1358A", area = "Phoenix Tower"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down)", address = "D1358E", area = "Phoenix Tower"),
LocationData("Phoenix Tower - Phoenix Tower Pot (15000)", address = "D13592", area = "Phoenix Tower"),
LocationData("Phoenix Tower - Phoenix Tower Pot (20000)", address = "D13596", area = "Phoenix Tower"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down)", address = "D1359A", area = "Phoenix Tower"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Avis Killer)", address = "D1359E", area = "Phoenix Tower"),
LocationData("Phoenix Tower - Phoenix Tower Pot (25000)", address = "D135A2", area = "Phoenix Tower"),
LocationData("Mirage Village - Mirage Village Barrel (Thief Knife)", address = "D135A6", area = "Mirage Village"),
LocationData("Rift - Rift (Ruins) Chest (Ether)", address = "D135AA", area = "Rift"),
LocationData("Rift - Rift (Ruins) Chest (Cabin)", address = "D135AE", area = "Rift"),
LocationData("Rift - Rift (Ruins) Chest (Elixir)", address = "D135B2", area = "Rift"),
LocationData("Rift - Rift (Ruins) Chest (DarkMatter)", address = "D135B6", area = "Rift"),
LocationData("Rift - Rift (Ruins) Chest (Elixir)", address = "D135BA", area = "Rift"),
LocationData("Rift - Rift (Ruins) Chest (Drain Sword)", address = "D135BE", area = "Rift"),
LocationData("Rift - Rift (Forest) Chest (DragonFang)", address = "D135C2", area = "Rift"),
LocationData("Rift - Rift (Forest) Chest (Ribbon)", address = "D135C6", area = "Rift"),
LocationData("Rift - Rift (Forest) Chest (Enhancer)", address = "D135CA", area = "Rift"),
LocationData("Rift - Rift (Forest) Chest (Lillith Rod)", address = "D135CE", area = "Rift"),
LocationData("Rift - Rift (Cave) Chest (Angel Ring)", address = "D135D2", area = "Rift"),
LocationData("Rift - Rift (Cave) Chest (Coral Ring)", address = "D135D6", area = "Rift"),
LocationData("Rift - Rift (Castle) Chest (Thor Hammer)", address = "D135DA", area = "Rift"),
LocationData("Rift - Rift (Castle) Chest (Running Shoes)", address = "D135DE", area = "Rift"),
LocationData("Rift - Rift (Castle) Chest (Red Shoes)", address = "D135E2", area = "Rift"),
LocationData("Rift - Rift (Castle) Chest (Rainbow Dress)", address = "D135E6", area = "Rift"),
LocationData("Rift - Rift (Castle) Chest (ManEater)", address = "D135EA", area = "Rift"),
LocationData("Void - The Void Chest (Pinwheel)", address = "D135EE", area = "Void"),
LocationData("Void - The Void Chest (Pinwheel)", address = "D135F2", area = "Void"),
LocationData("Void - The Void Chest (Elixir)", address = "D135F6", area = "Void"),
LocationData("Void - The Void Chest (Ragnarok)", address = "D135FA", area = "Void"),
LocationData("Void - The Void Chest (Pinwheel)", address = "D135FE", area = "Void"),
LocationData("Ancient Library - Byblos (Boss)", address = "C0FB70", area = "Ancient Library", type="Key"),
LocationData("Wind Shrine - WingRaptor (Boss)", address = "C0FB72", area = "Wind Shrine",type="Key"),
LocationData("Torna Canal - Karlabos (Boss)", address = "C0FB74", area = "Torna Canal",type="Key"),
LocationData("Ship Graveyard - Siren (Boss)", address = "C0FB76", area = "Ship Graveyard",type="Key"),
LocationData("North Mountain - Magisa & Forza (Boss)", address = "C0FB78", area = "North Mountain",type="Key"),
LocationData("Walse Tower - Galura (Boss)", address = "C0FB7A", area = "Walse Tower",type="Key"),
LocationData("Steamship - LiquiFlame (Boss)", address = "C0FB7C", area = "Steamship",type="Key"),
LocationData("Karnak - Sergeant & DeathClaw (Boss)", address = "C0FB7E", area = "Karnak",type="Key"),
LocationData("Desert of Shifting Sands - Sandworm (Boss)", address = "C0FB80", area = "Desert of Shifting Sands",type="Key"),
LocationData("Tycoon Meteor - AdamanTiMi (Boss)", address = "C0FB82", area = "Tycoon Meteor",type="Key"),
LocationData("Flying Lonka Ruins - Sol Cannon (Boss)", address = "C0FB84", area = "Flying Lonka Ruins",type="Key"),
LocationData("Flying Lonka Ruins - ArchaeAvis (Boss)", address = "C0FB86", area = "Flying Lonka Ruins",type="Key"),
LocationData("Lonka Meteor - Chim.Brain (Boss)", address = "C0FB88", area = "Lonka Meteor",type="Key"),
LocationData("Walse Meteor - Puroboros (Boss)", address = "C0FB8A", area = "Walse Meteor",type="Key"),
LocationData("Karnak Meteor - Titan (Boss)", address = "C0FB8C", area = "Karnak Meteor",type="Key"),
LocationData("Ancient Library - Ifrit (Boss)", address = "C0FBB6", area = "Ancient Library",type="Key"),
LocationData("Walse Kingdom - Shiva (Boss)", address = "C0FBB8", area = "Walse Kingdom",type="Key"),
LocationData("Catapult - Crayclaw (Boss)", address = "C0FBBA", area = "Catapult",type="Key"),
LocationData("Exdeath's Castle - Gilgamesh 1 (Boss)", address = "C0FB8E", area = "Exdeath's Castle",type="Key"),
LocationData("Big Bridge - Gilgamesh 2 (Boss)", address = "C0FB90", area = "Big Bridge",type="Key"),
LocationData("Moogle Waterway - Tyrasaurus (Boss)", address = "C0FB92", area = "Moogle Waterway",type="Key"),
LocationData("Bal Castle - Abductor (Boss)", address = "C0FB94", area = "Bal Castle",type="Key"),
LocationData("Hiryuu Valley - HiryuuPlant (Boss)", address = "C0FB96", area = "Hiryuu Valley",type="Key"),
LocationData("Zeza Fleet - Gilgamesh 3 & Enkidou (Boss)", address = "C0FB98", area = "Zeza Fleet",type="Key"),
LocationData("Barrier Tower - Atmos (Boss)", address = "C0FB9A", area = "Barrier Tower",type="Key"),
LocationData("Mua Forest - Guardians (Boss)", address = "C0FB9C", area = "Mua Forest",type="Key"),
LocationData("Exdeath's Castle - Carbunkle (Boss)", address = "C0FB9E", area = "Exdeath's Castle",type="Key"),
LocationData("Exdeath's Castle - Gilgamesh 4 (Boss)", address = "C0FBA0", area = "Exdeath's Castle",type="Key"),
LocationData("Tule Pass - Antlion (Boss)", address = "C0FBA2", area = "Tule Pass",type="Key"),
LocationData("Pyramid - Merugene (Boss)", address = "C0FBA4", area = "Pyramid",type="Key"),
LocationData("Bal Castle - Odin (Boss)", address = "C0FBA6", area = "Bal Castle",type="Key"),
LocationData("Great Trench - Triton, Neregeid & Phobos (Boss)", address = "C0FBA8", area = "Great Trench",type="Key"),
LocationData("Fork Tower - Omniscient (Boss)", address = "C0FBAA", area = "Fork Tower",type="Key"),
LocationData("Fork Tower - Minotauros (Boss)", address = "C0FBAC", area = "Fork Tower",type="Key"),
LocationData("Istory Falls - Leviathan (Boss)", address = "C0FBAE", area = "Istory Falls",type="Key"),
LocationData("Solitary Island - Stalker (Boss)", address = "C0FBB0", area = "Solitary Island",type="Key"),
LocationData("Walse Tower - GoGo (Boss)", address = "C0FBB2", area = "Walse Tower",type="Key"),
LocationData("North Mountain Upper - Bahamut (Boss)", address = "C0FBB4", area = "North Mountain Upper", type="Key")
]