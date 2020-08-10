from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_nether_foliage',
        {
            'title': '下界除草机',
            'desc': '移除的下界苗和菌索',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:crimson_roots']),
            mcstats.StatReader(['minecraft:mined','minecraft:warped_roots']),
            mcstats.StatReader(['minecraft:mined','minecraft:nether_sprouts']),
        ]),
        2504 # added in 20w06a
    ))
