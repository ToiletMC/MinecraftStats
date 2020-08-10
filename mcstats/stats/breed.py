from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'breed',
        {
            'title': '农场主',
            'desc': '饲养的动物',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:animals_bred'])
    ))
