from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_bookshelf',
        {
            'title': '图书管理员',
            'desc': '制作的书架',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','minecraft:bookshelf'])
    ))
