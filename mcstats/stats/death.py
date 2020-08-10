from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'death',
        {
            'title': '阴间常客',
            'desc': '死亡的次数',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:deaths'])
    ))
