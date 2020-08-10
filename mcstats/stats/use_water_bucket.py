from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_water_bucket',
        {
            'title': '南水北调',
            'desc': '水桶的倾倒',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:water_bucket'])
    ))
