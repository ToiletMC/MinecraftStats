from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_ender_pearl',
        {
            'title': '空间能力者',
            'desc': '掷出的末影珍珠',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:ender_pearl'])
    ))
