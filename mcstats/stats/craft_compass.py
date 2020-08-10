from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_compass',
        {
            'title': '航海家',
            'desc': '制作的指南针',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:compass']),
    ))
