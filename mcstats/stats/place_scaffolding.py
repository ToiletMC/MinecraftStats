from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_scaffolding',
        {
            'title': '建筑施工队',
            'desc': '脚手架的放置',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:scaffolding']),
        1908 # scaffolding added in 18w45a
    ))
