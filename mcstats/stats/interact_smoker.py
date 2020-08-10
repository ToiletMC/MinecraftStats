from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_smoker',
        {
            'title': '厨师长',
            'desc': '与烟熏炉的互动',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_smoker']),
        1919 # smokers usable since 18w50a
    ))
