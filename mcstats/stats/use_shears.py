from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_shears',
        {
            'title': '薅羊毛',
            'desc': '剪刀的使用',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:shears'])
    ))
