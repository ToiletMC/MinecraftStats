from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_fish',
        {
            'title': '鱼之美食家',
            'desc': '吃下的鱼',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:cooked_salmon']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_cod']),
            mcstats.StatReader(['minecraft:used','minecraft:salmon']),
            mcstats.StatReader(['minecraft:used','minecraft:cod']),
            mcstats.StatReader(['minecraft:used','minecraft:clownfish']),
            mcstats.StatReader(['minecraft:used','minecraft:tropical_fish']),
        ])
    ))
