import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
#引入datatime函数获得当前时间
#设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# API基础地址
API_BASE = "https://api.frankfurter.app"
# 获取汇率数据
def get_exchange_rate(from_cur: str, to_cur: str, days: int = 30):
    # 计算起始和结束日期
    end_date = date.today()
    start_date = end_date - timedelta(days=days)
    url = f"{API_BASE}/{start_date}..{end_date}"
    # 设置请求参数,Params的作用是“定位资源”或“控制行为”
    params = {
        "from": from_cur,# 起始货币
        "to": to_cur# 目标货币
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Error: {response.status_code}")
#Pandas来把数据读取
def to_dataframe(date):
    date1 = date["rates"]
    rows =[{"日期":a, "货币":b, "汇率":c}
           for a,bc in date1.items()
           for b,c in bc.items()]
    return pd.DataFrame(rows)

def print_summary(df,from_cur: str, to_cur: str):
    latest = df["汇率"].iloc[-1]
    highest = df["汇率"].max()
    lowest = df["汇率"].min()
    change = (latest - df["汇率"].iloc[0]) / df["汇率"].iloc[0] * 100

    print("\n===== 汇率统计 =====")
    print(f"货币对：{from_cur} → {to_cur}")                   
    print(f"最新汇率：{latest:.4f}")
    print(f"最高：{highest:.4f}")
    print(f"最低：{lowest:.4f}")
    print(f"区间涨跌幅：{change:.2f}%")
    print("\n最近 5 天数据：")
    print(df.tail())

def plot_rate(df: pd.DataFrame, from_cur: str, to_cur: str):
    plt.plot(df["日期"], df["汇率"])
    plt.title(f"{from_cur} 到 {to_cur} 的汇率")
    plt.xlabel("日期")
    plt.ylabel("汇率")
    plt.grid(True)
    # 自动旋转
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()

def main():
    # 你可以在这里修改货币对和天数
    from_cur = "USD"
    to_cur = "CNY"
    days = 30

    print(f"正在获取 {from_cur} → {to_cur} 最近 {days} 天汇率...")

    try:
        raw = get_exchange_rate(from_cur, to_cur, days)
    except requests.RequestException as e:
        print(f"请求失败：{e}")
        return

    df = to_dataframe(raw)

    print_summary(df, from_cur, to_cur)
    plot_rate(df, from_cur, to_cur)


if __name__ == "__main__":
    main()

