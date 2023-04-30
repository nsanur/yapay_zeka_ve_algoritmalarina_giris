#derin oncelikli arama (dfs)
grafik = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : [],
        'F' : [],
}

ziyaret = set()

def dfs(ziyaret, grafik, dugum):
    if dugum not in ziyaret:
        print(dugum)
        ziyaret.add(dugum)

        for komsu in grafik[dugum]:
            if komsu not in ziyaret:
                dfs(ziyaret, grafik, komsu)

dfs(ziyaret, grafik, 'A')