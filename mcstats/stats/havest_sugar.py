from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'harvest_sugar',
        {
            'title': '糖精',
            'desc': '收获的甘蔗',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:picked_up','minecraft:sugar_cane']),
            mcstats.StatReader(['minecraft:used','minecraft:sugar_cane'])
        )
    ))
