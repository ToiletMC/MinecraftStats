from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_banner',
        {
            'title': '城市牛皮癣',
            'desc': '旗帜的放置',
            'unit': 'int',
        },
        # subtract mined from placed
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(
                ['minecraft:used'],
                ['minecraft:.*banner']),
            mcstats.StatSumMatchReader(
                ['minecraft:mined'],
                ['minecraft:.*banner'])),
    ))
