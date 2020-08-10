from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_campfire',
        {
            'title': '原始技艺',
            'desc': '与营火的互动',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_campfire']),
        1921 # campfires added in 19w02a
    ))
