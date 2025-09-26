import pandas as pd

# 读 CSV
df = pd.read_csv("~/COMP370-HW4/pony_data/clean_dialog.csv")

# 五个角色
ponies = ["Twilight Sparkle", "Rarity", "Pinkie Pie", "Rainbow Dash", "Fluttershy"]

total_lines = len(df) - 1  # 去掉表头
results = []

for pony in ponies:
    count = df['pony'].eq(pony).sum()
    percent = round(count / total_lines * 100, 2)
    results.append([pony, count, percent])

# 保存结果
out = pd.DataFrame(results, columns=["pony_name", "total_line_count", "percent_all_lines"])
out.to_csv("~/COMP370-HW4/Line_percentages.csv", index=False)
