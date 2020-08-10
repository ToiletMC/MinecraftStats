from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_bars',
        {
            'title': '狱卒',
            'desc': '铁栏杆和锁链的放置',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:iron_bars']),
            mcstats.StatReader(['minecraft:used','minecraft:chain']),
        ])
    ))
