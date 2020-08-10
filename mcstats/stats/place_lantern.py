from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_lantern',
        {
            'title': '黑暗之惧',
            'desc': '灯笼的放置',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatDiffReader(
                mcstats.StatReader(['minecraft:used','minecraft:lantern']),
                mcstats.StatReader(['minecraft:mined','minecraft:lantern']),
            ),
            mcstats.StatDiffReader(
                mcstats.StatReader(['minecraft:used','minecraft:soul_lantern']),
                mcstats.StatReader(['minecraft:mined','minecraft:soul_lantern']),
            ),
        ]),
        1910 # lanterns added in 18w46a
    ))
