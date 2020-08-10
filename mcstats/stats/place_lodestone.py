from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_lodestone',
        {
            'title': '带磁面包屑的小径',
            'desc': '磁石的放置',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:used','minecraft:lodestone']),
            mcstats.StatReader(['minecraft:mined','minecraft:lodestone']),
        ),
        2520 # added in 20w13a
    ))
