from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_totem',
        {
            'title': '九条命',
            'desc': '不死图腾的使用',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:totem_of_undying'])
    ))
