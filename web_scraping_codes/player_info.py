from crawl4ai import stage, navigate, next_stage, parse, collect, input, parser, $

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
    players = parse().get("playersData")
    for obj in players:
        name = obj["name"]
        team = obj["team"]
        url = obj["link"]
        next_stage(input={"name": name, "team": team, "url": url})

@parser()
def parse_stage2():
    players_links = []

    match_sections = $('div').filter(
        lambda el: $(el).find('span > span > span').text() == "Match Details"
    ).siblings()

    team1 = $(match_sections.eq(0)).find('span > span > span').text().replace(" Innings", "")
    team2 = $(match_sections.eq(1)).find('span > span > span').text().replace(" Innings", "")

    batting_tables = $('div > table.ci-scorecard-table')
    first_innings_rows = $(batting_tables.eq(0)).find('tbody > tr').filter(
        lambda i, el: $(el).find("td").length >= 8
    )
    second_innings_rows = $(batting_tables.eq(1)).find('tbody > tr').filter(
        lambda i, el: $(el).find("td").length >= 8
    )

    for row in first_innings_rows:
        tds = $(row).find('td')
        players_links.append({
            "name": $(tds.eq(0)).find('a > span > span').text().replace(' ', ''),
            "team": team1,
            "link": "https://www.espncricinfo.com" + $(tds.eq(0)).find('a').attr('href')
        })

    for row in second_innings_rows:
        tds = $(row).find('td')
        players_links.append({
            "name": $(tds.eq(0)).find('a > span > span').text().replace(' ', ''),
            "team": team2,
            "link": "https://www.espncricinfo.com" + $(tds.eq(0)).find('a').attr('href')
        })

    bowling_tables = $('div > table.ds-table')
    first_bowl_rows = $(bowling_tables.eq(1)).find('tbody > tr').filter(
        lambda i, el: $(el).find("td").length >= 11
    )
    second_bowl_rows = $(bowling_tables.eq(3)).find('tbody > tr').filter(
        lambda i, el: $(el).find("td").length >= 11
    )

    for row in first_bowl_rows:
        tds = $(row).find('td')
        players_links.append({
            "name": $(tds.eq(0)).find('a > span').text().replace(' ', ''),
            "team": team2,
            "link": "https://www.espncricinfo.com" + $(tds.eq(0)).find('a').attr('href')
        })

    for row in second_bowl_rows:
        tds = $(row).find('td')
        players_links.append({
            "name": $(tds.eq(0)).find('a > span').text().replace(' ', ''),
            "team": team1,
            "link": "https://www.espncricinfo.com" + $(tds.eq(0)).find('a').attr('href')
        })

    return {"playersData": players_links}

@stage()
def interaction_stage3():
    navigate(input["url"])
    final_data = parse()
    collect({
        "name": input["name"],
        "team": input["team"],
        "battingStyle": final_data["battingStyle"],
        "bowlingStyle": final_data["bowlingStyle"],
        "playingRole": final_data["playingRole"],
        "description": final_data["content"]
    })

@parser()
def parse_stage3():
    batting = $('div.ds-grid > div').filter(
        lambda i, el: $(el).find('p').first().text() == "Batting Style"
    )
    bowling = $('div.ds-grid > div').filter(
        lambda i, el: $(el).find('p').first().text() == "Bowling Style"
    )
    role = $('div.ds-grid > div').filter(
        lambda i, el: $(el).find('p').first().text() == "Playing Role"
    )

    return {
        "battingStyle": batting.find('span').text(),
        "bowlingStyle": bowling.find('span').text(),
        "playingRole": role.find('span').text(),
        "content": $('div.ci-player-bio-content').find('p').first().text()
    }
