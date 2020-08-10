from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'play_record',
        {
            'title': '如果我是DJ',
            'desc': '播放的唱片',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:play_record'])
    ))
