from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_potion',
        {
            'title': '炼金术士',
            'desc': '药水的使用',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:lingering_potion']),
            mcstats.StatReader(['minecraft:used','minecraft:potion']),
            mcstats.StatReader(['minecraft:used','minecraft:splash_potion'])
        ])
    ))
