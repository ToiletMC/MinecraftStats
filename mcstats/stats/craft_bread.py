from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_bread',
        {
            'title': '烘焙师',
            'desc': '制作的面包，蛋糕和曲奇',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:crafted','minecraft:bread']),
            mcstats.StatReader(['minecraft:crafted','minecraft:cake']),
            mcstats.StatReader(['minecraft:crafted','minecraft:cookie']),
        ])
    ))
