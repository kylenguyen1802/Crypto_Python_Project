import pandas as pd, pathlib
p = pathlib.Path("data/processed/test.parquet")
p.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame({"x":[1,2,3]}).to_parquet(p)
print("wrote:", p, "size:", p.stat().st_size, "bytes")
