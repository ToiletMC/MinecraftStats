from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_egg',
        {
            'title': '接住它！',
            'desc': '掷出的鸡蛋',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:egg'])
    ))
