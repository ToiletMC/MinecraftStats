from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_lava_bucket',
        {
            'title': '一生只能喝一次',
            'desc': '岩浆桶的倾倒',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:lava_bucket'])
    ))
