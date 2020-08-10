from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_snow',
        {
            'title': '推雪车',
            'desc': '移除的雪',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:snow']),
            mcstats.StatReader(['minecraft:mined','minecraft:snow_block']),
        ])
    ))
