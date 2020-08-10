from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_grass',
        {
            'title': '除草机',
            'desc': '移除的草',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:grass']),
            mcstats.StatReader(['minecraft:mined','minecraft:tall_grass']),
        ])
    ))
