from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_junkfood',
        {
            'title': '简·拉基·茨德',
            'desc': '吃下的垃圾食品',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:rotten_flesh']),
            mcstats.StatReader(['minecraft:used','minecraft:spider_eye']),
            mcstats.StatReader(['minecraft:used','minecraft:poisonous_potato']),
        ])
    ))
