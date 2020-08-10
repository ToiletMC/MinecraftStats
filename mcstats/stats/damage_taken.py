from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'damage_taken',
        {
            'title': '沙袋',
            'desc': '所承受的伤害',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:damage_taken'])
    ))
