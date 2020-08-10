from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_any',
        {
            'title': '杀戮狂欢！',
            'desc': '杀死生物的总数',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:mob_kills'])
    ))

def create_kill_stat(mobId, title, mobText, minVersion = 0, maxVersion = float("inf")):
    mcstats.registry.append(
        mcstats.MinecraftStat(
            'kill_' + mobId,
            {
                'title': title,
                'desc': mobText + ' killed',
                'unit': 'int',
            },
            mcstats.StatReader(['minecraft:killed','minecraft:' + mobId]),
            minVersion,
            maxVersion
        ))

# Hostiles
create_kill_stat('blaze','Extinguisher','Blazes')
create_kill_stat('creeper','Creeper Creep','Creepers')
create_kill_stat('endermite','End Ratter','Endermite')
create_kill_stat('ender_dragon','Dragon Hunter','Ender Dragons')
create_kill_stat('ghast','Tear Drinker','Ghasts')
create_kill_stat('magma_cube','Magma Cream','Magma Cubes')
create_kill_stat('phantom','Phantom Shooter','Phantoms',1467) # added in 18w07a
# Note: Ravagers had been added as Illager Beats in 18w43a (1901)
# support for that snapshot may be added on demand
create_kill_stat('ravager','Ravaging!','Ravagers',1930) # changed in 19w05a
create_kill_stat('shulker','Shulker Cracker','Shulkers')
create_kill_stat('silverfish','Nasty Little...','Silverfish')
create_kill_stat('slime','Swamp Lurker','Slimes')
create_kill_stat('vex','Vex Hunter','Vexes')
create_kill_stat('witch','Witch Hunter','Witches')
create_kill_stat('wither_skeleton','Wither Or Not','Wither Skeletons')

# Neutrals
create_kill_stat('bee','Beegone!','Bees',2200) # added in 19w34a
create_kill_stat('dolphin','Dolphin Hunter','Dolphins',1482) # added in 18w15a
create_kill_stat('enderman','Enderman Ender','Endermen')
create_kill_stat('iron_golem','Defense Down!','Iron Golems')
create_kill_stat('panda','Kung FU! Panda','Pandas',1901) # added in 18w43a
create_kill_stat('piglin','Die, Pig!','Piglins', 2506) # added in 20w07a
create_kill_stat('polar_bear','Polar Hunter','Polar Bears')
create_kill_stat('snow_golem','AntiFrosty','Snow Golems')
create_kill_stat('zombie_pigman','Nether Gang War','Zombie Pigmen',0,2510) # renamed to Zombified Piglin in 20w09a
create_kill_stat('zombified_piglin','Nether Gang War','Zombified Piglins',2510)   # added in 20w09a

# Passives
create_kill_stat('bat','Bat Flap','Bats')
create_kill_stat('chicken','Chicken Griller','Chickens')
create_kill_stat('cow','Cow Tipper','Cows')
create_kill_stat('horse','Horse Hater','Horses')
create_kill_stat('fox','What Does The Fox Say?','Foxes',1932) # added in 19w07a
create_kill_stat('mooshroom','Mycelium Cowboy','Mooshrooms')
create_kill_stat('parrot','Stupid Bird!','Parrots')
create_kill_stat('pig','Pork Chopper','Pigs')
create_kill_stat('rabbit','Bunny Killer :(','Rabbits')
create_kill_stat('sheep','Big Bad Wolf','Sheep')
create_kill_stat('squid','Pool Cleaner','Squids')
create_kill_stat('strider','Lava Pool Cleaner','Striders',2520) # added in 20w13a
create_kill_stat('turtle','Super Mario','Turtles',1467) # added in 18w07a
create_kill_stat('villager','Bully','Villagers')
create_kill_stat('wandering_trader','Trade Sanctions','Wandering Traders',1930) # added in 19w05a
create_kill_stat('wolf','Bad Dog!','Wolves and Dogs')

# Cats (including ozelots)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_ocelot',
        {
            'title': '猫咪杀手',
            'desc': '杀死的猫和豹猫',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:cat']),
            mcstats.StatReader(['minecraft:killed','minecraft:ocelot']),
        ])
    ))

# Llamas (including trader llamas)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_llama',
        {
            'title': '商队匪徒',
            'desc': '杀死的羊驼',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:llama']),
            mcstats.StatReader(['minecraft:killed','minecraft:trader_llama']),
        ])
    ))

# Zombies (including Husks and Zombie Villagers)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_zombie',
        {
            'title': '僵尸绞杀机',
            'desc': '杀死的僵尸/尸壳/溺尸',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:husk']),
            mcstats.StatReader(['minecraft:killed','minecraft:drowned']),
            mcstats.StatReader(['minecraft:killed','minecraft:zombie']),
            mcstats.StatReader(['minecraft:killed','minecraft:zombie_villager']),
        ])
    ))

# Skeletons (including Strays)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_skeleton',
        {
            'title': '骨头收藏家',
            'desc': '杀死的骷髅/流浪者',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:skeleton']),
            mcstats.StatReader(['minecraft:killed','minecraft:stray']),
        ])
    ))

# Spiders (including Cave Spiders)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_spider',
        {
            'title': '蜘蛛恐惧症',
            'desc': '杀死的蜘蛛',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:spider']),
            mcstats.StatReader(['minecraft:killed','minecraft:cave_spider']),
        ])
    ))

# Guardians (including Elder Guardians)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_guardian',
        {
            'title': '深海寻宝者',
            'desc': '杀死的守卫者',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:guardian']),
            mcstats.StatReader(['minecraft:killed','minecraft:elder_guardian']),
        ])
    ))

# Illagers (all types)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_illagers',
        {
            'title': '去污粉',
            'desc': '杀死的灾厄村民',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:evoker']),
            mcstats.StatReader(['minecraft:killed','minecraft:vindicator']),
            mcstats.StatReader(['minecraft:killed','minecraft:pillager']),
            mcstats.StatReader(['minecraft:killed','minecraft:illusioner']),
            mcstats.StatReader(['minecraft:killed','minecraft:illager_beast']),
        ])
    ))

# Hoglins and Zoglins (all types)
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_hoglins',
        {
            'title': '哼唧哼唧',
            'desc': '杀死的疣猪兽和僵尸疣猪兽',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:hoglin']),
            mcstats.StatReader(['minecraft:killed','minecraft:zoglin']),
        ]),
        2504 # added in 20w06a
    ))

# Fish mobs
mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_fish',
        {
            'title': '捕鱼大师',
            'desc': '杀死的鱼',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','minecraft:cod']),
            mcstats.StatReader(['minecraft:killed','minecraft:salmon']),
            mcstats.StatReader(['minecraft:killed','minecraft:pufferfish']),
            mcstats.StatReader(['minecraft:killed','minecraft:tropical_fish']),
        ]),
        1471 # fish mobs added in 18w08b
    ))
