from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_minecart',
        {
            'title': '公共交通',
            'desc': '用矿车行进的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:minecart_one_cm'])
    ))
