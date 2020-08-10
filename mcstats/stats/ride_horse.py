from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_horse',
        {
            'title': '马术老手',
            'desc': '用马骑行的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:horse_one_cm'])
    ))
