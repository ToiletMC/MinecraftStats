from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'harvest_bamboo',
        {
            'title': '大熊猫',
            'desc': '收获的竹子',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:picked_up','minecraft:bamboo']),
        1901 # bamboo added in 18w43a
    ))
