from mcstats import mcstats

def create_ore_stat(title, oreId, oreName, minVersion = 0):
    mcstats.registry.append(
        mcstats.MinecraftStat(
            'mine_' + oreId,
            {
                'title': title,
                'desc': '挖掘的' + oreName,
                'unit': 'int',
            },
            mcstats.StatReader(['minecraft:mined','minecraft:' + oreId]),
            minVersion
        ))

create_ore_stat('考古学家', 'ancient_debris', '远古残骸', 2504) # added in 20w06a
create_ore_stat('黑金', 'coal_ore', '煤矿石')
create_ore_stat('铁石心肠', 'iron_ore', '铁矿石')
create_ore_stat('钻石！', 'diamond_ore', '钻石矿石')
create_ore_stat('山地矿工', 'emerald_ore', '绿宝石矿石')
create_ore_stat('蓝', 'lapis_ore', '青金石矿石')
create_ore_stat('红石矿工', 'redstone_ore', '红石矿石')
create_ore_stat('白白的', 'nether_quartz_ore', '下界石英矿石')

# gold ore
mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_gold_ore',
        {
            'title': '淘金者',
            'desc': '挖掘的金矿石',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:gold_ore']),
            mcstats.StatReader(['minecraft:mined','minecraft:nether_gold_ore']),
        ])
    ))
