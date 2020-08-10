from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'harvest_nether_wart',
        {
            'title': '下界农人',
            'desc': '收获的下界疣',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:picked_up','minecraft:nether_wart']),
            mcstats.StatReader(['minecraft:used','minecraft:nether_wart'])
        )
    ))
