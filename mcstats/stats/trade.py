from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'trade',
        {
            'title': '商人',
            'desc': '与村民交易的次数',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:traded_with_villager'])
    ))
