from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_cactus',
        {
            'title': '仙人掌专业户',
            'desc': '仙人掌的种植',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:cactus'])
    ))
