from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_ender_eye',
        {
            'title': '要塞探险者',
            'desc': '掷出的末影之眼',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:ender_eye'])
    ))
