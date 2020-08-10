from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_clock',
        {
            'title': '时间管理大师',
            'desc': '制作的时钟',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:clock']),
    ))
