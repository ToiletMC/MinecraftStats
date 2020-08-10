from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ride_pig',
        {
            'title': '猪王',
            'desc': '用猪骑行的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:pig_one_cm'])
    ))
