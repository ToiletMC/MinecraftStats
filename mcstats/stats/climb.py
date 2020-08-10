from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'climb',
        {
            'title': '一起爬山吗',
            'desc': '攀登的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:climb_one_cm'])
    ))
