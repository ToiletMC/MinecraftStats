from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'noteblock',
        {
            'title': '音乐家',
            'desc': '与音符盒的互动',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:custom','minecraft:tune_noteblock']),
            mcstats.StatReader(['minecraft:custom','minecraft:play_noteblock'])])
    ))
