from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_ender_chest',
        {
            'title': '四次元口袋',
            'desc': '制作的末影箱',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:ender_chest']),
    ))
