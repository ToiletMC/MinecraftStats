from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_stone',
        {
            'title': '石匠',
            'desc': '挖掘的石头',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:stone']),
            mcstats.StatReader(['minecraft:mined','minecraft:diorite']),
            mcstats.StatReader(['minecraft:mined','minecraft:andesite']),
            mcstats.StatReader(['minecraft:mined','minecraft:granite']),
            mcstats.StatReader(['minecraft:mined','minecraft:basalt']),
            mcstats.StatReader(['minecraft:mined','minecraft:blackstone']),
        ])
    ))
