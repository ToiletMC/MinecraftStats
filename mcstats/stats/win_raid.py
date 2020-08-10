from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'win_raid',
        {
            'title': '英雄',
            'desc': '袭击胜利',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:raid_win']),
        1912 # raids added in 18w47a
    ))
