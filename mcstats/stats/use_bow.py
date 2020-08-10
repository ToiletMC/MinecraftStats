from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_bow',
        {
            'title': '弓箭手',
            'desc': '射出的箭',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:bow'])
    ))
