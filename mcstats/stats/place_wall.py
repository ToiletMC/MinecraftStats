from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_wall',
        {
            'title': '柏林墙',
            'desc': '墙的构筑',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['minecraft:glass','minecraft:.*_wall']),
    ))
