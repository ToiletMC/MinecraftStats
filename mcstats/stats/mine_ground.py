from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_ground',
        {
            'title': '挖掘机',
            'desc': '挖掘的泥土和沙子等等',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:dirt']),
            mcstats.StatReader(['minecraft:mined','minecraft:coarse_dirt']),
            mcstats.StatReader(['minecraft:mined','minecraft:farmland']),
            mcstats.StatReader(['minecraft:mined','minecraft:grass']),
            mcstats.StatReader(['minecraft:mined','minecraft:grass_path']),
            mcstats.StatReader(['minecraft:mined','minecraft:gravel']),
            mcstats.StatReader(['minecraft:mined','minecraft:mycelium']),
            mcstats.StatReader(['minecraft:mined','minecraft:podzol']),
            mcstats.StatReader(['minecraft:mined','minecraft:red_sand']),
            mcstats.StatReader(['minecraft:mined','minecraft:sand']),
            mcstats.StatReader(['minecraft:mined','minecraft:soul_sand']),
            mcstats.StatReader(['minecraft:mined','minecraft:soul_soil']),
        ])
    ))
