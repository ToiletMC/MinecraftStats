from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_sponge',
        {
            'title': '海绵宝宝',
            'desc': '烘干的海绵',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:sponge'])
    ))
