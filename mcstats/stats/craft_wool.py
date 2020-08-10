from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_wool',
        {
            'title': '布艺师',
            'desc': '制作或染过的羊毛和地毯',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                'minecraft:.+_wool',
                'minecraft:.+_carpet'
            ])
    ))
