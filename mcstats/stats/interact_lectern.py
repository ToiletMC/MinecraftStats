from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_lectern',
        {
            'title': '牧师',
            'desc': '与讲台的互动',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_stonecutter']),
        1921 # lecterns usable since 19w02a
    ))
