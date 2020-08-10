from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_strider',
        {
            'title': '熔岩地板又怎样？',
            'desc': '用炽足兽骑行的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:strider_one_cm']),
        2534 # added in 20w19a
    ))
