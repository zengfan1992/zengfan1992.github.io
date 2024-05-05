import sys
import sqlparse
import io

with open(sys.argv[1], "r", encoding="utf-8") as f:
    print(sqlparse.format(f.read(), reindent=True), end="")
