from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'sleep',
        {
            'title': '瞌睡虫上身',
            'desc': '睡觉的次数',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:sleep_in_bed'])
    ))
