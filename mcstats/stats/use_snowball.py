from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_snowball',
        {
            'title': '打雪仗！',
            'desc': '掷出的雪球',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:snowball'])
    ))
