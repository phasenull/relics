import random
import time
config = {
    "min_seed": 50,
    "max_seed": 1000,
    "grid_size": 1000,
}
abc = ""
abc += "qwertyuopasdfghjklizxcvbnm"
abc = abc + abc.upper()
abc += '''*-!'^+&/()=?_>£#$[]| .,:'''
abc += "0123456789"

def get_index_of_character(character: str):
    return abc.find(character)

def generate_random_string(length: int):
    random_string = ""
    for i in range(0,length):
        random_string += abc[random.randint(0,len(abc)-1)]
    return random_string
def obfuscate_character(character: str,x : int):
    long = abc*int(x)
    return generate_random_string(x-1) + long[long.find(character)+x]

def get_character_with_seed(character:str,seed:int):
    long = abc*int(seed)
    return long[seed]

def deobfuscate_character(character: str,x : int):
    long = abc*int(x)
    return long[long.find(character)-x]

def obfuscate_string(string:str,seed:int):
    if seed < config["min_seed"] or seed > config["max_seed"]:
        raise Exception(f"""Seed "{seed}" is invalid, the seed must be between {config["min_seed"]} and {config["max_seed"]}""")
    i = 0
    for character in string:
        if abc.find(character) == None:
            raise Exception(f"Unsupported character {character} at {i}")
        i +=1
    long = abc * seed
    date = "created_at:"+ ("0"   *  (30-len(    str(int(time.time()))    ))    + str(int(time.time())))
    target_grid = ((len(string) + 41)*seed) // config["grid_size"] + 1
    grid_diff = target_grid - ((len(string) + 41)*seed)
    string += date
    obfuscated = ""
    for character in string:
        obfuscated += obfuscate_character(character,seed)
    return str(obfuscated)
def get_clear_string(string:str,seed:int):
    i = 0
    clear = ""
    for char in string:
        i += 1
        if i % seed == 0:
            i = 0
            clear += char
    return clear
def get_unix_time_from_obfuscated_string(string:str,seed:int):
    if seed < config["min_seed"] or seed > config["max_seed"]:
        raise Exception(f"""Seed "{seed}" is invalid, the seed must be between {config["min_seed"]} and {config["max_seed"]}""")
    i = 0
    for character in get_clear_string(string,seed):
        if abc.find(character) == None:
            raise Exception(f"Unsupported character {character} at {i}")
        i +=1
    long = abc * seed
    unixtime = ""
    for character in get_clear_string(string,seed):
        unixtime += deobfuscate_character(character,seed)
    unixtime = str(int(unixtime[-30:]))
    return unixtime

def deobfuscate_string(string:str,seed:int):
    if seed < config["min_seed"] or seed > config["max_seed"]:
        raise Exception(f"""Seed "{seed}" is invalid, the seed must be between {config["min_seed"]} and {config["max_seed"]}""")
    i = 0
    for character in get_clear_string(string,seed):
        if abc.find(character) == None:
            raise Exception(f"Unsupported character {character} at {i}")
        i +=1
    long = abc * seed
    deobfuscated = ""
    for character in get_clear_string(string,seed):
        deobfuscated += deobfuscate_character(character,seed)
    deobfuscated = deobfuscated[:-41]
    return str(deobfuscated)