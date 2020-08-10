from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_dirt',
        {
            'title': '灰头土脸',
            'desc': '泥土的放置',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:dirt'])
    ))
