import sys
import sqlparse
import io

with open(sys.argv[1], "r", encoding="utf-8") as f:
    # print(";\n".join(map(lambda x: sqlparse.format(x, reindent=True),sqlparse.split(f.read()))), end="")
    list = sqlparse.split(f.read())
    res = []
    for x in list:
        if "create table" in x:
            res.append(sqlparse.format(x))
            continue
        s = sqlparse.format(x, reindent=True)
        if len(s) > 1:
            res.append(s.replace("\n\n", "\n"))
    print("\n\n".join(res), end="")
