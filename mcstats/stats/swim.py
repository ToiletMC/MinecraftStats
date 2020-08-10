from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'swim',
        {
            'title': '游泳健将',
            'desc': '游泳的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:swim_one_cm'])
    ))
