import pandas as pd
import time

df = pd.DataFrame({"First": []})

for i in range(100):
    print(i)
    df = pd.concat([df, pd.DataFrame({"First": [i]})], axis=0, ignore_index=True)
    df.to_csv("./out.csv", index=False)
    time.sleep(0.1)
    