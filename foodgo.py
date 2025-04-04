import pandas as pd
import random
import uuid
from tabulate import tabulate

# -------- 模擬參數 -------- #
num_samples = 500

# 訂單價格與距離分布
price_distribution = [
    (100, 200, 0.25),
    (200, 350, 0.50),
    (350, 450, 0.16),
    (450, 500, 0.08),
    (500, 1000, 0.01)
]

distance_distribution = [
    (1, 3, 0.50),
    (3, 5, 0.30),
    (5, 7, 0.15),
    (7, 10, 0.05)
]

def weighted_random_choice(choices):
    ranges = [c[:2] for c in choices]
    weights = [c[2] for c in choices]
    selected_range = random.choices(ranges, weights=weights)[0]
    return round(random.uniform(selected_range[0], selected_range[1]), 1)

def generate_samples(n):
    data = []
    for _ in range(n):
        order_price = round(weighted_random_choice(price_distribution), 2)
        distance = round(weighted_random_choice(distance_distribution), 1)
        is_rainy = random.choice([True, False])
        has_uniform = random.choice([True, False])

        base_salary = 35
        ad_bonus = 5 if has_uniform else 0
        rain_bonus = 7 if is_rainy else 0

        if distance <= 3:
            distance_bonus = round(10 * distance, 2)
        elif 3 < distance <= 5:
            distance_bonus = round(10 * 3 + 12 * (distance - 3), 2)
        elif 5 < distance <= 10:
            distance_bonus = round(10 * 3 + 12 * 2 + 15 * (distance - 5), 2)
        else:
            distance_bonus = 0

        salary = round(base_salary + distance_bonus + ad_bonus + rain_bonus, 2)
        salary_threshold = round(order_price * 0.30, 2)
        over_threshold = salary > salary_threshold
        platform_burden = max(0, round(salary - salary_threshold, 2))

        if distance < 3:
            mileage_fee = 9
        elif distance < 5:
            mileage_fee = 19
        elif distance < 7:
            mileage_fee = 29
        elif distance < 10:
            mileage_fee = 39
        else:
            mileage_fee = 0

        if order_price > 1000:
            commission_rate = 0.10
        elif order_price > 750:
            commission_rate = 0.07
        elif order_price > 500:
            commission_rate = 0.05
        else:
            commission_rate = 0.035
        commission = round(order_price * commission_rate, 2)

        revenue = mileage_fee + commission
        profit = revenue - platform_burden

        data.append({
            "訂單金額": order_price,
            "距離(km)": distance,
            "下雨": is_rainy,
            "穿制服": has_uniform,
            "外送員薪資": salary,
            "薪資門檻(30%)": salary_threshold,
            "超過門檻": over_threshold,
            "平台負擔金額": platform_burden,
            "運費": mileage_fee,
            "手續費": commission,
            "平台收入": revenue,
            "平台利潤": profit
        })
    return pd.DataFrame(data)

# 生成資料與平均值
df = generate_samples(num_samples)
avg = df.mean(numeric_only=True).round(2)
avg_row = {col: avg[col] if col in avg else '' for col in df.columns}
df.loc["平均"] = avg_row

# 顯示為漂亮的格子表格
from tabulate import tabulate
print(tabulate(df, headers='keys', tablefmt='grid', showindex=True))

