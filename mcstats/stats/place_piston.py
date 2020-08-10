from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_piston',
        {
            'title': '机械工',
            'desc': '活塞的放置',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:.*piston']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:.*piston'])),
    ))
