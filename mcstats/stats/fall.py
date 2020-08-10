from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'fall',
        {
            'title': '极限跳伞运动员',
            'desc': '跌落的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:fall_one_cm'])
    ))
