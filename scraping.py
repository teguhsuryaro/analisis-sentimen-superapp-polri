"""Download Google Play Store reviews to a semicolon-separated CSV."""

import argparse
from pathlib import Path

import pandas as pd
from google_play_scraper import Sort, reviews


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-id", default="superapps.polri.presisi.presisi",
                        help="Google Play app ID (default: Superapp Polri)")
    parser.add_argument("--language", default="id", help="Review language (default: id)")
    parser.add_argument("--country", default="id", help="Play Store country (default: id)")
    parser.add_argument("--count", type=int, default=1000,
                        help="Maximum number of reviews to request (default: 1000)")
    parser.add_argument("--output", type=Path,
                        help="CSV output path (default: data/ulasan_<app-id>.csv)")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.count < 1:
        raise SystemExit("--count harus lebih besar dari 0")

    default_name = (
        "ulasan_superapp_polri.csv"
        if args.app_id == "superapps.polri.presisi.presisi"
        else f"ulasan_{args.app_id}.csv"
    )
    output = args.output or Path("data") / default_name
    result, _ = reviews(
        args.app_id,
        lang=args.language,
        country=args.country,
        sort=Sort.NEWEST,
        count=args.count,
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(result)
    df.to_csv(output, index=False, encoding="utf-8-sig", sep=";")

    print(f"Jumlah data yang berhasil diambil: {len(df)}")
    print(f"File tersimpan di: {output}")
    if {"content", "score"}.issubset(df.columns):
        print(df[["content", "score"]].head())


if __name__ == "__main__":
    main()
