from crawl4ai import stage, navigate, collect, parse, parser, $

@stage()
def interaction_stage1():
    navigate('https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament')
    collect(parse())

@parser()
def parse_stage1():
    match_summary = []
    rows = $('table.engineTable > tbody > tr.data1')
    for row in rows:
        tds = $(row).find('td')
        match_summary.append({
            "team1": $(tds[0]).text(),
            "team2": $(tds[1]).text(),
            "winner": $(tds[2]).text(),
            "margin": $(tds[3]).text(),
            "ground": $(tds[4]).text(),
            "matchDate": $(tds[5]).text(),
            "scorecard": $(tds[6]).text()
        })
    return {"matchSummary": match_summary}
