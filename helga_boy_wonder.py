from random import randint

from helga.plugins import match

EXPRESSIONS = [
    "Agility", "Almost", "Alphabet", "Alps", "Alter Ego", "Anagram", "Apparition",
    "Armadillo", "Armour Plate", "Ashtray", "Asp", "Astronomy", "Astringent Plum-like Fruit",
    "Audubon", "Backfire", "Ball And Chain", "Bank Balance", "Bankruptcy",
    "Banks", "Bargain Basements", "Barracuda", "Bat Logic", "Bat Trap", "Batman",
    "Benedict Arnold", "Bijou", "Bikini", "Bill Of Rights", "Birthday Cake",
    "Black Beard", "Blackout", "Blank Cartridge", "Blizzard", "Blonde Mackerel Ash",
    "Bluebeard", "Bouncing Boiler Plate", "Bowler", "Bullseye", "Bunions",
    "Caffeine", "Camouflage", "Captain Nemo", "Caruso", "Catastrophe", "Cat",
    "Cats", "Chicken Coop", "Chilblains", "Chocolate Eclair", "Cinderella",
    "Cinemascope", "Cliche", "Cliffhangers", "Clockwork", "Clockworks", "Cofax You Mean",
    "Coffin Nails", "Cold Creeps", "Complications", "Conflagration", "Contributing to the Delinquency of Minors",
    "Corpuscles", "Cosmos", "Costume Party", "Crack Up", "Crickets", "Crossfire",
    "Crucial Moment", "Cryptology", "D'artagnan", "Davy Jones", "Detonator",
    "Disappearing Act", "Distortion", "Diversionary Tactics", "Dr. Jekyll and Mr. Hyde",
    "Egg Shells", "Encore", "Endangered Species", "Epigrams", "Escape-hatch",
    "Explosion", "Fate-worse-than-death", "Felony", "Finishing-touches", "Fireworks",
    "Firing Squad", "Fishbowl", "Flight Plan", "Flip-flop", "Flood Gate", "Floor Covering",
    "Flypaper", "Fly Trap", "Fog", "Forecast", "Fork In The Road", "Fourth Amendment",
    "Fourth Of July", "Frankenstein", "Frankenstein It's Alive", "Fratricide",
    "Frogman", "Fruit Salad", "Frying Towels", "Funny Bone", "Gall", "Gambles",
    "Gemini", "Geography", "Ghost Writer", "Giveaways", "Glow Pot", "Golden Gate",
    "Graf Zeppelin", "Grammar", "Graveyards", "Greed", "Green Card", "Greetings-cards",
    "Guacamole", "Guadalcanal", "Gullibility", "Gunpowder", "Haberdashery",
    "Hailstorm", "Hairdo", "Hallelujah", "Halloween", "Hallucination", "Hamburger",
    "Hamlet", "Hamstrings", "Happenstance", "Hardest Metal In The World", "Harem",
    "Harshin", "Haziness", "Headache", "Headline", "Heart Failure", "Heartbreak",
    "Heidelberg", "Helmets", "Helplessness", "Here We Go Again", "Hi-fi", "Hieroglyphic",
    "High-wire", "Hijack", "Hijackers", "History", "Hoaxes", "Hole In A Donut",
    "Hollywood", "Holocaust", "Homecoming", "Homework", "Homicide", "Hoodwink",
    "Hoof Beats", "Hors D'Oeuvre", "Horseshoes", "Hostage", "Hot Foot", "Houdini",
    "Human Collectors Item", "Human Pearls", "Human Pressure Cookers", "Human Surfboards",
    "Hunting Horn", "Hurricane", "Hutzpa", "Hydraulics", "Hypnotism", "Hypodermics",
    "Ice Picks", "Ice Skates", "Iceberg", "Impossibility", "Impregnability",
    "Incantation", "Inquisition", "Interplanetary Yardstick", "Interruptions",
    "Iodine", "IT and T", "Jack In The Box", "Jackpot", "Jail Break", "Jaw Breaker",
    "Jelly Molds", "Jet Set", "Jigsaw Puzzles", "Jitter Bugs", "Joe", "Journey To The Center Of The Earth",
    "Jumble", "Jumpin' Jiminy", "Karats", "Key Hole", "Key Ring", "Kilowatts",
    "Kindergarten", "Knit One Purl Two", "Knock Out Drops", "Known Unknown Flying Objects",
    "Kofax", "Las Vegas", "Leopard", "Levitation", "Liftoff", "Living End",
    "Lodestone", "Long John Silver", "Looking Glass", "Love Birds", "Luther Burbank",
    "Madness", "Magic Lantern", "Magician", "Main Springs", "Marathon", "Mashed Potatoes",
    "Masquerade", "Matador", "Mechanical Armies", "Memory Bank", "Merlin Magician",
    "Mermaid", "Merry Go Around", "Mesmerism", "Metronome", "Miracles", "Miscast",
    "Missing Relatives", "Molars", "Mole Hill", "Mucilage", "Multitudes", "Murder",
    "Mush", "Naive", "New Year's Eve", "Nick Of Time", "Nightmare", "Non Sequiturs",
    "Oleo", "Olfactory", "One Track Bat Computer Mind", "Oversight", "Oxygen",
    "Paderewski", "Paraffin", "Perfect Pitch", "Pianola", "Pin Cushions", "Polar Front",
    "Polar Ice Sheet", "Polaris", "Popcorn", "Potluck", "Pressure Cooker",
    "Priceless Collection of Etruscan Snoods", "Pseudonym", "Purple Cannibals",
    "Puzzlers", "Rainbow", "Rats In A Trap", "Ravioli", "Razors Edge", "Recompense",
    "Red Herring", "Red Snapper", "Reincarnation", "Relief", "Remote Control Robot",
    "Reshevsky", "Return From Oblivion", "Reverse Polarity", "Rheostat", "Ricochet",
    "Rip Van Winkle", "Rising Hemlines", "Roadblocks", "Robert Louis Stevenson",
    "Rock Garden", "Rocking Chair", "Romeo And Juliet", "Rudder", "Safari",
    "Sarcophagus", "Sardine", "Scalding", "Schizophrenia", "Sedatives", "Self Service",
    "Semantics", "Serpentine", "Sewer Pipe", "Shamrocks", "Sherlock Holmes",
    "Show-Ups", "Showcase", "Shrinkage", "Shucks", "Skull Tap", "Sky Rocket",
    "Slipped Disc", "Smoke", "Smokes", "Smokestack", "Snowball", "Sonic Booms",
    "Special Delivery", "Spider Webs", "Split Seconds", "Squirrel Cage", "Stalactites",
    "Stampede", "Standstills", "Steam Valve", "Stew Pot", "Stomach Aches",
    "Stratosphere", "Stuffing", "Subliminal", "Sudden Incapacitation", "Sundials",
    "Surprise Party", "Switch A Roo", "Taj Mahal", "Tartars", "Taxation", "Taxidermy",
    "Tee Shot", "Ten Toes", "Terminology", "Time Bomb", "Tintinnabulation",
    "Tipoffs", "Titanic", "Tome", "Toreador", "Trampoline", "Transistors",
    "Travel Agent", "Trickery", "Triple Feature", "Trolls And Goblins", "Tuxedo",
    "Uncanny Photographic Mental Processes", "Understatements", "Underwritten Metropolis",
    "Unlikelihood", "Unrefillable Prescriptions", "Vat", "Venezuela", "Vertebrae",
    "Voltage", "Waste Of Energy", "Wayne Manor", "Weaponry", "Wedding Cake",
    "Wernher von Braun", "Whiskers", "Wigs", "Zorro",
]

HOLY = 'Holy'

SUFFIXES = [
    ', Batman!',
    ', Batman, what do we do now?',
    '!'
]


def holy_exclamation(message):
    """
    If message ends with exclamation point, return a random
    Robin the Boy Wonder expression.
    """
    if message.strip().endswith('!'):
        expression = ' '.join([HOLY, EXPRESSIONS[randint(0, len(EXPRESSIONS) - 1)]])

        # 20% chance of adding each suffix other than '!'
        suffix_index = randint(0, 4)
        if suffix_index < len(SUFFIXES) - 1:
            expression += SUFFIXES[suffix_index]
        else:
            expression += SUFFIXES[-1]
        return expression


@match(holy_exclamation, priority=0)
def boy_wonder(client, channel, nick, message, match):
    return match # pragma: no cover
