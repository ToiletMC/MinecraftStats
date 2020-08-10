from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'aviate',
        {
            'title': '飞行员',
            'desc': '用鞘翅飞行的距离',
            'icon': 'items/elytra.png',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:aviate_one_cm'])
    ))
