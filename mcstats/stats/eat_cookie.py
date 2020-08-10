from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_cookie',
        {
            'title': '曲奇怪物',
            'desc': '吃下的曲奇',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:cookie'])
    ))
