import pandas as pd
from pathlib import Path

current_dir = Path(__file__).resolve().parent
comment_csv = current_dir.parent / "comment_data.csv"
video_csv = current_dir.parent / "video_data.csv"
comment_df = pd.read_csv(comment_csv)
video_df = pd.read_csv(video_csv)

print("comment_data.csv的.head()：")
print(comment_df.head())
print()

print("video_data.csv的.head()：")
print(video_df.head())
print()

print("comment_data.csv的.columns：")
print(comment_df.columns)
print()

print("video_data.csv的.columns：")
print(video_df.columns)
