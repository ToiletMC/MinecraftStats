from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_book',
        {
            'title': '畅销书作家',
            'desc': '撰写的书籍',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:writable_book'])
    ))
