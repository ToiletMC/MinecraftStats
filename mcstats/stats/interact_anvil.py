from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_anvil',
        {
            'title': '工匠',
            'desc': '与铁砧的互动',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_anvil']),
        2219 # stat added in 1.15 Pre-Release 2
    ))
