from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'enchant',
        {
            'title': '魔法师',
            'desc': '附魔的物品',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:enchant_item'])
    ))
