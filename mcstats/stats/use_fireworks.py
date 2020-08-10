from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_fireworks',
        {
            'title': '烟火设计师',
            'desc': '燃放的烟花火箭',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:firework_rocket'])
    ))
