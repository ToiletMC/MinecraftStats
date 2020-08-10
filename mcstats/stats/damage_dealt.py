from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'damage_dealt',
        {
            'title': '暴力狂！',
            'desc': '所造成的伤害',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:damage_dealt'])
    ))
