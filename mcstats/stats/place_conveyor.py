from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_conveyor',
        {
            'title': '输送机',
            'desc': '漏斗和投掷器的放置',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:hopper','minecraft:dropper']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:hopper','minecraft:dropper']),
        )
    ))
