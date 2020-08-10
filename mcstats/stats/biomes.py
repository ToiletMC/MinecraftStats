from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'biomes',
        {
            'title': '探险家',
            'desc': '已踏足的生物群落',
            'unit': 'int',
        },
        mcstats.StatListLengthReader([
            'advancements',
            'minecraft:adventure/adventuring_time',
            'criteria'
        ])
    ))
