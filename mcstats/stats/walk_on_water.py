from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'walk_on_water',
        {
            'title': '轻功水上漂',
            'desc': '水上行走的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:walk_on_water_one_cm'])
    ))
