from bbanalyze_passes_tests import bbanalyze

a = bbanalyze()

print(a)
print(a['record.count'])
print(a['complete.cases'])
print(a['years'])
print(a['player.count'])
print(a['team.count'])
print(a['league.count'])
print(a['nl'])
print(a['al'])
print(a['records'])

a = bbanalyze('bb2005.csv')

print(a)
print(a['record.count'])
print(a['complete.cases'])
print(a['years'])
print(a['player.count'])
print(a['team.count'])
print(a['league.count'])
print(a['nl'])
print(a['al'])
print(a['records'])

