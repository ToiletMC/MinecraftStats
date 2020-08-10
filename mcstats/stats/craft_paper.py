from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_paper',
        {
            'title': '送报员',
            'desc': '制作的纸',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:paper'])
    ))
