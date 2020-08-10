from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'trigger_raid',
        {
            'title': '不祥之兆',
            'desc': '袭击的触发',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:raid_trigger']),
        1912 # raids added in 18w47a
    ))
