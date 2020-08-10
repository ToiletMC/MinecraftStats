from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'drop',
        {
            'title': '投手',
            'desc': '掷下的物品',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:drop'])
    ))
