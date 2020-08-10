from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_tnt',
        {
            'title': '坏心眼',
            'desc': '制作的TNT',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:tnt'])
    ))
