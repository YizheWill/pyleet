def updateDict(dict, points, teamName):
    if teamName not in dict:
        dict[teamName] = 0
    dict[teamName] += points


def tournamentWinner(competitions, results):
    currentWinner = ""
    res = {currentWinner: 0}
    for idx, compArray in enumerate(competitions):
        result = results[idx]
        home, away = compArray
        winnerTeam = home if result == 1 else away
        updateDict(res, 3, winnerTeam)
        if res[winnerTeam] > res[currentWinner]:
            currentWinner = winnerTeam
    return currentWinner
