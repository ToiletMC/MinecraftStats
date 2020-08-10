from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_armor',
        {
            'title': '装甲师',
            'desc': '制作的盔甲',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                'minecraft:.+_helmet',
                'minecraft:.+_leggings',
                'minecraft:.+_boots',
                'minecraft:.+_chestplate',
                'minecraft:shield',
            ])
    ))
