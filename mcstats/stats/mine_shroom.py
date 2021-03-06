from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_shroom',
        {
            'title': '采蘑菇的小家伙',
            'desc': '采集的蘑菇',
            'unit': 'int',
        },
        # subtract placed from mined
        mcstats.StatSumReader([
            mcstats.StatDiffReader(
                mcstats.StatReader(['minecraft:mined','minecraft:red_mushroom']),
                mcstats.StatReader(['minecraft:used','minecraft:red_mushroom']),
            ),
            mcstats.StatDiffReader(
                mcstats.StatReader(['minecraft:mined','minecraft:brown_mushroom']),
                mcstats.StatReader(['minecraft:used','minecraft:brown_mushroom']),
            ),
            mcstats.StatDiffReader(
                mcstats.StatReader(['minecraft:mined','minecraft:crimson_fungus']),
                mcstats.StatReader(['minecraft:used','minecraft:crimson_fungus']),
            ),
            mcstats.StatDiffReader(
                mcstats.StatReader(['minecraft:mined','minecraft:warped_fungus']),
                mcstats.StatReader(['minecraft:used','minecraft:warped_fungus']),
            ),
        ]),
    ))
