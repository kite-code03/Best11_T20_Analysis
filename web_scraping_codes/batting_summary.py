from crawl4ai import stage, navigate, next_stage, parse, $, parser, collect, input

@stage()
def interaction_stage1():
    navigate('https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament')
    links = parse().get("matchSummaryLinks")
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
    return {"matchSummaryLinks": links}

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

    tables = $('div > table.ci-scorecard-table')
    first_innings_rows = $(tables.eq(0)).find('tbody > tr').filter(
        lambda i, el: $(el).find("td").length >= 8
    )
    second_innings_rows = $(tables.eq(1)).find('tbody > tr').filter(
        lambda i, el: $(el).find("td").length >= 8
    )

    batting_summary = []

    for idx, row in enumerate(first_innings_rows):
        tds = $(row).find('td')
        batting_summary.append({
            "match": match_info,
            "teamInnings": team1,
            "battingPos": idx + 1,
            "batsmanName": $(tds.eq(0)).find('a > span > span').text().replace(' ', ''),
            "dismissal": $(tds.eq(1)).find('span > span').text(),
            "runs": $(tds.eq(2)).find('strong').text(),
            "balls": $(tds.eq(3)).text(),
            "4s": $(tds.eq(5)).text(),
            "6s": $(tds.eq(6)).text(),
            "SR": $(tds.eq(7)).text()
        })

    for idx, row in enumerate(second_innings_rows):
        tds = $(row).find('td')
        batting_summary.append({
            "match": match_info,
            "teamInnings": team2,
            "battingPos": idx + 1,
            "batsmanName": $(tds.eq(0)).find('a > span > span').text().replace(' ', ''),
            "dismissal": $(tds.eq(1)).find('span > span').text(),
            "runs": $(tds.eq(2)).find('strong').text(),
            "balls": $(tds.eq(3)).text(),
            "4s": $(tds.eq(5)).text(),
            "6s": $(tds.eq(6)).text(),
            "SR": $(tds.eq(7)).text()
        })

    return {"battingSummary": batting_summary}
