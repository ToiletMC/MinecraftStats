from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_ice',
        {
            'title': '碎冰机',
            'desc': '破坏的冰',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:ice']),
            mcstats.StatReader(['minecraft:mined','minecraft:packed_ice']),
            mcstats.StatReader(['minecraft:mined','minecraft:blue_ice']),
            mcstats.StatReader(['minecraft:mined','minecraft:frosted_ice']),
        ])
    ))
