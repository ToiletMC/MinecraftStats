from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_soup',
        {
            'title': '嗜汤者',
            'desc': '吃/喝下的炖菜汤品',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:mushroom_stew']),
            mcstats.StatReader(['minecraft:used','minecraft:beetroot_soup']),
            mcstats.StatReader(['minecraft:used','minecraft:rabbit_stew']),
            mcstats.StatReader(['minecraft:used','minecraft:suspicious_stew']),
        ])
    ))
