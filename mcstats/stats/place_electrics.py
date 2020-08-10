from mcstats import mcstats

redstone_item_patterns = [
    'minecraft:redstone',
    'minecraft:redstone_torch',
    'minecraft:.+_button',
    'minecraft:daylight_detector.*',
    'minecraft:detector_rail',
    'minecraft:lever',
    'minecraft:observer',
    'minecraft:comparator',
    'minecraft:repeater',
    'minecraft:.+_pressure_plate',
    'minecraft:target',
]

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_electrics',
        {
            'title': '电工师傅',
            'desc': '红石物品的放置',
            'unit': 'int',
        },
        # subtract mined from placed
        mcstats.StatDiffReader(
            mcstats.StatSumMatchReader(['minecraft:used'], redstone_item_patterns),
            mcstats.StatSumMatchReader(['minecraft:mined'], redstone_item_patterns),
        )
    ))
