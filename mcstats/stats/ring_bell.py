from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ring_bell',
        {
            'title': '铃儿响叮当',
            'desc': '撞钟的次数',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:bell_ring']),
        1907 # bells added in 18w44a
    ))
