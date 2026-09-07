from google_play_scraper import reviews, Sort
import pandas as pd

result, continuation_token = reviews(
    'com.adakami.dana.kredit.pinjaman',
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=1000
)

print("Jumlah data yang berhasil diambil:", len(result))

df = pd.DataFrame(result)

df.to_csv(
    'ulasan_adakami_3.csv',
    index=False,
    encoding='utf-8-sig',
    sep=';'
)

print(df[['content', 'score']].head())