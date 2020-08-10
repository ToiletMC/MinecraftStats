from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'walk',
        {
            'title': '行者',
            'desc': '行走的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:walk_one_cm'])
    ))
