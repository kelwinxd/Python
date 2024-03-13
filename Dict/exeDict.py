deceased_a = {
    "Wolfgang Amadeus Mozart": {"idade": 35, "estilo": "Clássico"},
    "Louis Armstrong": {"idade": 69, "estilo": "Jazz"},
    "Frederic Chopin": {"idade": 39, "estilo": "Romântico"},
    "Billie Holiday": {"idade": 89, "estilo": "Blues/Jazz"},
}
more = []
max_value = max(a["idade"] for a in deceased_a.values())
for a in deceased_a.values():
    if a["idade"] == max_value:
        print(a) 