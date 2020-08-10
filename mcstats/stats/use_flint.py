from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_flint',
        {
            'title': '纵火狂',
            'desc': '点燃物品',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:flint_and_steel'])
    ))
