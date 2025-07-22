from crawl4ai import stage, navigate, next_stage, parse, $, parser, collect, input

@stage()
def interaction_stage1():
    navigate('https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament')
    links = parse().get("playersLinks")
    for url in links:
        next_stage(input={"url": url})

@parser()
def parse_stage1():
    links = []
    rows = $('table.engineTable > tbody > tr.data1')
    for row in rows:
        tds = $(row).find('td')
        href = $(tds[6]).find('a').attr('href')
        full_url = "https://www.espncricinfo.com" + href
        links.append(full_url)
    return {"playersLinks": links}

@stage()
def interaction_stage2():
    navigate(input["url"])
    collect(parse())

@parser()
def parse_stage2():
    match_sections = $('div').filter(
        lambda el: $(el).find('span > span > span').text() == "Match Details"
    ).siblings()
    team1 = $(match_sections.eq(0)).find('span > span > span').text().replace(" Innings", "")
    team2 = $(match_sections.eq(1)).find('span > span > span').text().replace(" Innings", "")
    match_info = f"{team1} Vs {team2}"

    tables = $('div > table.ds-table')
    first_innings_rows = $(tables.eq(1)).find('tbody > tr').filter(
        lambda i, el: $(el).find("td").length >= 11
    )
    second_innings_rows = $(tables.eq(3)).find('tbody > tr').filter(
        lambda i, el: $(el).find("td").length >= 11
    )

    bowling_summary = []

    for idx, row in enumerate(first_innings_rows):
        tds = $(row).find('td')
        bowling_summary.append({
            "match": match_info,
            "bowlingTeam": team2,
            "bowlerName": $(tds.eq(0)).find('a > span').text().replace(' ', ''),
            "overs": $(tds.eq(1)).text(),
            "maiden": $(tds.eq(2)).text(),
            "runs": $(tds.eq(3)).text(),
            "wickets": $(tds.eq(4)).text(),
            "economy": $(tds.eq(5)).text(),
            "0s": $(tds.eq(6)).text(),
            "4s": $(tds.eq(7)).text(),
            "6s": $(tds.eq(8)).text(),
            "wides": $(tds.eq(9)).text(),
            "noBalls": $(tds.eq(10)).text()
        })

    for idx, row in enumerate(second_innings_rows):
        tds = $(row).find('td')
        bowling_summary.append({
            "match": match_info,
            "bowlingTeam": team1,
            "bowlerName": $(tds.eq(0)).find('a > span').text().replace(' ', ''),
            "overs": $(tds.eq(1)).text(),
            "maiden": $(tds.eq(2)).text(),
            "runs": $(tds.eq(3)).text(),
            "wickets": $(tds.eq(4)).text(),
            "economy": $(tds.eq(5)).text(),
            "0s": $(tds.eq(6)).text(),
            "4s": $(tds.eq(7)).text(),
            "6s": $(tds.eq(8)).text(),
            "wides": $(tds.eq(9)).text(),
            "noBalls": $(tds.eq(10)).text()
        })

    return {"bowlingSummary": bowling_summary}
