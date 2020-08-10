from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'drink_milk',
        {
            'title': '乳臭未干',
            'desc': '酗奶',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:milk_bucket'])
    ))
