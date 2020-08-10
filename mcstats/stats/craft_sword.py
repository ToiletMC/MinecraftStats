from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_sword',
        {
            'title': '铁匠',
            'desc': '制作的剑',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_sword'])
    ))
