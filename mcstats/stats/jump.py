from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'jump',
        {
            'title': '跳跳兔',
            'desc': '跳跃的次数',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:jump'])
    ))
