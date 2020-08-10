from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_beacon',
        {
            'title': '信标工程师',
            'desc': '制作的信标',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:beacon']),
    ))
