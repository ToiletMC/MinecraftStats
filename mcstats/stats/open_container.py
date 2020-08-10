from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'open_container',
        {
            'title': '货栈',
            'desc': '打开容器的次数',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:custom','minecraft:open_chest']),
            mcstats.StatReader(['minecraft:custom','minecraft:open_shulker_box']),
            mcstats.StatReader(['minecraft:custom','minecraft:open_enderchest']),
            mcstats.StatReader(['minecraft:custom','minecraft:trigger_trapped_chest']),
        ])
    ))
