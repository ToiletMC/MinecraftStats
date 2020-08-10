from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_spawner',
        {
            'title': '啊，不！',
            'desc': '移除的刷怪笼',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:spawner'])
    ))
