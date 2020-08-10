from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_respawn_anchor',
        {
            'title': '涅磐',
            'desc': '制作的重生锚',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:crafted','minecraft:respawn_anchor']),
        ]),
        2515 # introduced in 20w12a
    ))
