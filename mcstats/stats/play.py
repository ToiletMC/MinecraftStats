from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'play',
        {
            'title': '网瘾患者',
            'desc': '总游戏时间',
            'unit': 'ticks',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:play_one_minute'])
    ))
