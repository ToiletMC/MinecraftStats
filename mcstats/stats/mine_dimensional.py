from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_dimensional',
        {
            'title': '地貌勘探者',
            'desc': '挖掘的下界岩和末地石',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:end_stone']),
            mcstats.StatReader(['minecraft:mined','minecraft:netherrack'])
        ])
    ))
