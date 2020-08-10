from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_glowstone',
        {
            'title': '灯光师',
            'desc': '制作的荧石',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:glowstone']),
    ))
