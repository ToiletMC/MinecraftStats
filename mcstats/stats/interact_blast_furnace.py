from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_blast_furnace',
        {
            'title': '冶炼师',
            'desc': '与高炉的互动',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_blast_furnace']),
        1919 # blast furnace usable since 18w50a
    ))
