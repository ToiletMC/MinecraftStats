from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_obsidian',
        {
            'title': '黑曜石矿工',
            'desc': '挖掘的黑曜石',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:obsidian'])
    ))
