from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_hoe',
        {
            'title': '农人',
            'desc': '犁过的方块',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['minecraft:.+_hoe'])
    ))
