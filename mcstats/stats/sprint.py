from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'sprint',
        {
            'title': '短跑运动员',
            'desc': '疾跑的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:sprint_one_cm'])
    ))
