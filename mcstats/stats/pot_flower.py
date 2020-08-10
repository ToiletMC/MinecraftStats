from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'pot_flower',
        {
            'title': '花店老板',
            'desc': '栽植于花盆的鲜花',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:pot_flower'])
    ))
