from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'dive',
        {
            'title': '潜水员',
            'desc': '潜水的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:walk_under_water_one_cm'])
    ))
