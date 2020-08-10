from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'crouch',
        {
            'title': '鬼鬼祟祟',
            'desc': '潜行的距离',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:crouch_one_cm'])
    ))
