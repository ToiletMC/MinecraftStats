from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_wood',
        {
            'title': '樵夫',
            'desc': '砍下的木块',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:mined'],['minecraft:.+_log', 'minecraft:.+_stem'])
    ))
