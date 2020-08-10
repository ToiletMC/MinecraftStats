from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_stonecutter',
        {
            'title': '泥瓦匠',
            'desc': '与切石机的互动',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_stonecutter']),
        1926 # stonecutters usable since 19w04a
    ))
