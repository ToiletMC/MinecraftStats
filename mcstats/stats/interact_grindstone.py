from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_grindstone',
        {
            'title': '我能修好它！',
            'desc': '与砂轮的互动',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_grindstone']),
        2219 # stat added in 1.15 Pre-Release 2
    ))
