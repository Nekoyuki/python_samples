## ディレクトリの中のファイルを取得してまわす。

```
import pandas as pd
from pathlib import Path
p = Path(".")
for i in p.glob("*.csv"):
    print(i.name)
    print(i.cwd())
    df = pd.read_csv(i)
```

## ファイルを読み込む。
```
with open('aaa.csv', 'r') as f:
    r = f.readline()
    while(r):
        print(r, end='')
        r = f.readline()
```

## 16進数
```
int('10', 16)
```
