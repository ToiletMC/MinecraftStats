mcstats.showHof = function() {
    var tbody = '';

    var rank = 1;
    mcstats.hof.forEach(function(entry) {
        var rankWidget = mcstats.rankWidget(rank++, 'crown');
        var playerWidget = mcstats.playerWidget(entry.uuid);
        var value = entry.value;

        tbody += `
            <tr>
                <td class="text-right">${rankWidget}</th>
                <td>${playerWidget}</td>
                <td class="text-data text-center">${value[1]}</td>
                <td class="text-data text-center">${value[2]}</td>
                <td class="text-data text-center">${value[3]}</td>
                <td class="text-data text-right">${value[0]}</td>
            </tr>
        `;
    });

    mcstats.viewContent.innerHTML = `
        <div class="mcstats-entry p-1">
        <div class="round-box p-1">
            <table class="table table-responsive-xs table-hover table-sm">
            <thead>
                <th scope="col" class="text-right text-shadow">排名</th>
                <th scope="col" class="text-shadow">玩家</th>
                <th scope="col" class="text-center"><img class="img-textsize-2" title="Gold Medals" src="img/fatcow/medal_award_gold.png"/></th>
                <th scope="col" class="text-center"><img class="img-textsize-2" title="Silver Medals" src="img/fatcow/medal_award_silver.png"/></th>
                <th scope="col" class="text-center"><img class="img-textsize-2" title="Bronze Medals" src="img/fatcow/medal_award_bronze.png"/></th>
                <th scope="col" class="text-right text-shadow">总分</th>
            </thead>
            <tbody>${tbody}</tbody>
            </table>
        </div>
        </div>
    `;

    var crown = mcstats.info.crown;
    var formatCrown = function(x) {
        return wordSmallInt(x) + ' 分' + ((x > 1) ? '' : '');
    };

    // show
    mcstats.showView(
        '名人堂',
        '奖牌得分排名',
        `
            最高分由玩家持有的奖牌数量计算得出。<br/>
            一个金牌可得 <span class="rank-1">${formatCrown(crown[0])}</span>，
            一个银牌可得 <span class="rank-2">${formatCrown(crown[1])}</span>，
            一个铜牌可得 <span class="rank-3">${formatCrown(crown[2])}</span>。
        `,
        false);
}
