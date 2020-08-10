from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_tools',
        {
            'title': '工坊',
            'desc': '制作的工具',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                'minecraft:.+_axe',
                'minecraft:.+_hoe',
                'minecraft:.+_pickaxe',
                'minecraft:.+_shovel',
                'minecraft:fishing_rod',
                'minecraft:flint_and_steel',
                'minecraft:shears',
            ])
    ))
