from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_cartography',
        {
            'title': '制图师',
            'desc': '与制图台的互动',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_cartography_table']),
        1921 # stonecutters usable since 19w02a
    ))
