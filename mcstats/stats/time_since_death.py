from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'time_since_death',
        {
            'title': '生还者',
            'desc': '距离最后一次死亡',
            'unit': 'ticks',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:time_since_death'])
    ))
