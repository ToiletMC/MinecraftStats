from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_brewing_stand',
        {
            'title': '酿造师',
            'desc': '与酿造台的互动',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_brewingstand']),
    ))
