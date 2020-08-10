from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_glass',
        {
            'title': '玻璃工人',
            'desc': '玻璃的放置',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['minecraft:glass','minecraft:.*glass_pane','minecraft:.*stained_glass']),
    ))
