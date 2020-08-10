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
                'desc': '杀死的' + mobText,
                'unit': 'int',
            },
            mcstats.StatReader(['minecraft:killed','minecraft:' + mobId]),
            minVersion,
            maxVersion
        ))

# Hostiles
create_kill_stat('blaze','灭火器','烈焰人')
create_kill_stat('creeper','拆弹专家','苦力怕')
create_kill_stat('endermite','鼠辈终结','末影螨')
create_kill_stat('ender_dragon','屠龙者','末影龙')
create_kill_stat('ghast','饮泣者','恶魂')
create_kill_stat('magma_cube','火山泥面膜','岩浆怪')
create_kill_stat('phantom','幻翼射手','幻翼',1467) # added in 18w07a
# Note: Ravagers had been added as Illager Beats in 18w43a (1901)
# support for that snapshot may be added on demand
create_kill_stat('ravager','打砸抢烧！','劫掠兽',1930) # changed in 19w05a
create_kill_stat('shulker','潜影贝天敌','潜影贝')
create_kill_stat('silverfish','恶心的小家伙……','蠹虫')
create_kill_stat('slime','沼泽伏击者','史莱姆')
create_kill_stat('vex','恼鬼猎人','恼鬼')
create_kill_stat('witch','猎巫行动','女巫')
create_kill_stat('wither_skeleton','凋不凋','凋灵骷髅')

# Neutrals
create_kill_stat('bee','蜂飞飞','蜜蜂',2200) # added in 19w34a
create_kill_stat('dolphin','海豚捕手','海豚',1482) # added in 18w15a
create_kill_stat('enderman','末影人之末','末影人')
create_kill_stat('iron_golem','失守了！','铁傀儡')
create_kill_stat('panda','五年起步','熊猫',1901) # added in 18w43a
create_kill_stat('piglin','死猪不怕开水烫','猪灵', 2506) # added in 20w07a
create_kill_stat('polar_bear','极地猎人','北极熊')
create_kill_stat('snow_golem','抗霜冻','雪傀儡')
create_kill_stat('zombie_pigman','下界帮派战','僵尸猪人',0,2510) # renamed to Zombified Piglin in 20w09a
create_kill_stat('zombified_piglin','生化危机','僵尸猪灵',2510)   # added in 20w09a

# Passives
create_kill_stat('bat','不是我的错','蝙蝠')
create_kill_stat('chicken','鸡串烤场','鸡')
create_kill_stat('cow','庖丁再世','牛')
create_kill_stat('horse','吁～','马')
create_kill_stat('fox','狐狸怎么叫？','狐狸',1932) # added in 19w07a
create_kill_stat('mooshroom','哞～','哞菇')
create_kill_stat('parrot','蠢鸟！','鹦鹉')
create_kill_stat('pig','咸猪手','猪')
create_kill_stat('rabbit','怎么可以杀兔兔 :(','兔子')
create_kill_stat('sheep','大恶狼','羊')
create_kill_stat('squid','池塘清洁工','鱿鱼')
create_kill_stat('strider','火云邪神','炽足兽',2520) # added in 20w13a
create_kill_stat('turtle','龟龟','海龟',1467) # added in 18w07a
create_kill_stat('villager','恶霸','村民')
create_kill_stat('wandering_trader','贸易制裁','流浪商人',1930) # added in 19w05a
create_kill_stat('wolf','坏狗狗！','狼与狗')

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
