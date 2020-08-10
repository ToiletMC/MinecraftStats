from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'collect_berries',
        {
            'title': '浆果爱好者',
            'desc': '收集到的甜浆果',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:picked_up','minecraft:sweet_berries']),
        1916 # berries introduced in 18w49a
    ))
