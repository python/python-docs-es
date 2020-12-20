from pprint import pprint

results = {}

# page-requests-20200504-20200510.txt
# is a file containing stats from pageviews on the official Python documentation
# (including different versions and languages)
# grep -E '\.html$' page-requests-20200504-20200510.txt | grep -v tutorial | sed 's/3\..\///g' | sed 's/3\///g' | sed 's/2\///g' > pageviews.txt
pages = open('pageviews.txt').readlines()[:-1]
for p in pages:
    count, key = int(p.split()[0]), p.split()[-1].strip()
    if key in results:
        results[key] += count
    else:
        results[key] = count

for p in sorted(list(results.items()), key=lambda x: x[1], reverse=True)[50:100]:
    print(p[1], p[0][1:])
