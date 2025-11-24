routes = [
    "NorthLine", "SouthExpress", "EastTrack", "WestCargo",
    "NairobiRoute", "NakuruLink", "MombasaRun", "KisumuDrive",
    "NanyukiPath", "NyeriTrail"
]

routes.append("KerichoDelivery")
routes.remove("EastTrack")

routes.sort()
routes.reverse()
print(routes)

count_n = sum(1 for r in routes if r.startswith("N"))
print(count_n)

long_routes = [r for r in routes if len(r) > 10]
print(long_routes)
