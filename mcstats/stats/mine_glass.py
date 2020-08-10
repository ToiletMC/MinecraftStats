from mcstats import mcstats
mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_glass',
        {
            'title': '玻璃粉碎机',
            'desc': '破坏的玻璃',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:mined'],
            ['minecraft:glass','minecraft:.*glass_pane','minecraft:.*stained_glass']),
    ))
