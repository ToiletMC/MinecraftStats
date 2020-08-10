from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_rails',
        {
            'title': '铁路公司',
            'desc': '铁轨的放置',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['minecraft:.*rail'])
    ))
