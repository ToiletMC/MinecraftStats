from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_chorus_flower',
        {
            'title': '紫颂专业户',
            'desc': '紫颂花的种植',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:chorus_flower'])
    ))
