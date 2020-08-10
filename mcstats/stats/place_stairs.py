from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_stairs',
        {
            'title': '上上下下',
            'desc': '搭建的楼梯',
            'unit': 'int',
        },
        # subtract mined from placed
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:.+_stairs']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:.+_stairs'])),
    ))
