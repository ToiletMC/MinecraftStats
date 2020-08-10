from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'killed_by_creeper',
        {
            'title': 'SSSS，Boooom！',
            'desc': '被苦力怕杀死的次数',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:killed_by','minecraft:creeper'])
    ))
