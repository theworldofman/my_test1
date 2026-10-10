# -*- coding: utf-8 -*-
"""
项目：命令行天气查询系统 v1.0
数据源：Open-Meteo（免费，无需 API Key）
依赖：pip install requests
"""
# 学到的知识汇总
# resp.raise_for_status()用来API访问后抛出异常
# resp.json()这个函数可以将JSON格式的字符串转换成Python字典,是request库函数
# 字典.get(键名,默认值),更加安全的获取字典中的值，如果键不存在，返回默认值
# datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
# strftime 是 datetime 对象的一个方法，它的作用：把 datetime 对象变成你指定格式的字符串。
# 它需要一个参数：格式字符串，告诉它“我要什么样子”。




import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
import requests

# ---------- 常量配置 ----------
GEO_API = "https://geocoding-api.open-meteo.com/v1/search"   # 城市 -> 经纬度
WEATHER_API = "https://api.open-meteo.com/v1/forecast"       # 经纬度 -> 天气
HISTORY_FILE = "weather_history.json"                        # 本地历史记录文件

# WMO 天气代码对照表
WMO_CODE = {
    0: "晴", 1: "基本晴朗", 2: "局部多云", 3: "阴",
    45: "雾", 48: "冻雾",
    51: "小毛毛雨", 53: "毛毛雨", 55: "大毛毛雨",
    56: "冻毛毛雨", 57: "强冻毛毛雨",
    61: "小雨", 63: "中雨", 65: "大雨",
    66: "冻雨", 67: "强冻雨",
    71: "小雪", 73: "中雪", 75: "大雪", 77: "雪粒",
    80: "小阵雨", 81: "阵雨", 82: "强阵雨",
    85: "小阵雪", 86: "大阵雪",
    95: "雷阵雨", 96: "雷阵雨伴小冰雹", 99: "雷阵雨伴大冰雹",
}


class WeatherSystem:
    """天气查询系统主类"""

    def __init__(self):
        self.history = self._load_history()

    # ---------- 历史记录的读写 ----------
    def _load_history(self):
        """从本地文件读取历史记录，出错时返回空列表"""
        if not os.path.exists(HISTORY_FILE):
            return []
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []

    def _save_history(self):
        """把历史记录写入本地文件"""
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    # ---------- 网络请求 ----------
    @staticmethod
    def geocode(city):
        """城市名 -> 经纬度信息，找不到返回 None"""
        params = {"name": city, "count": 1, "language": "zh", "format": "json"}
        resp = requests.get(GEO_API, params=params, timeout=10)
        resp.raise_for_status()
        results = resp.json().get("results")
        if not results:
            return None
        r = results[0]
        return {
            "name": r.get("name", city),
            "admin": r.get("admin1", ""),
            "country": r.get("country", ""),
            "lat": r["latitude"],
            "lon": r["longitude"],
        }

    @staticmethod
    def fetch_weather(lat, lon):
        """根据经纬度获取实时天气 + 未来 3 天预报"""
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": ("temperature_2m,relative_humidity_2m,"
                        "apparent_temperature,weather_code,wind_speed_10m"),
            "daily": "weather_code,temperature_2m_max,temperature_2m_min",
            "timezone": "auto",
            "forecast_days": 3,
        }
        resp = requests.get(WEATHER_API, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()

    # ---------- 核心业务 ----------
    def query(self, city):
        """查询并打印某个城市的天气"""
        try:
            loc = self.geocode(city)
            if loc is None:
                print(f"❌ 未找到城市「{city}」，请检查拼写后重试。")
                return
            data = self.fetch_weather(loc["lat"], loc["lon"])
        except requests.RequestException as e:
            print(f"❌ 网络请求失败：{e}")
            return

        cur = data["current"]
        desc = WMO_CODE.get(cur["weather_code"], "未知")

        print("=" * 48)
        print(f"📍 {loc['admin']} {loc['name']}  ({loc['country']})")
        print(f"🕒 观测时间：{cur['time'].replace('T', ' ')}")
        print("-" * 48)
        print(f"🌡  温度：{cur['temperature_2m']} ℃（体感 {cur['apparent_temperature']} ℃）")
        print(f"☁  天气：{desc}")
        print(f"💧 湿度：{cur['relative_humidity_2m']} %")
        print(f"🌬  风速：{cur['wind_speed_10m']} km/h")
        print("-" * 48)
        print("未来三天预报：")
        daily = data["daily"]
        plt.plot(daily["time"], daily["temperature_2m_min"], label="Min Temp")
        plt.plot(daily["time"], daily["temperature_2m_max"], label="Max Temp")
        plt.xlabel("Date")
        plt.ylabel("Temperature (℃)")
        plt.title(f"Temperature Forecast for {loc['name']}")
        plt.legend()
        plt.show()
        for i, date in enumerate(daily["time"]):
            d = WMO_CODE.get(daily["weather_code"][i], "未知")
            lo = daily["temperature_2m_min"][i]
            hi = daily["temperature_2m_max"][i]
            print(f"  {date}  {d:<12} {lo:>5}℃ ~ {hi:>5}℃")
        print("=" * 48)

        # 记录到历史（最多保留 20 条）
        self.history.append({
            "city": loc["name"],
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "temp": cur["temperature_2m"],
        })
        self.history = self.history[-20:]
        self._save_history()

    def show_history(self):
        """展示历史查询记录"""
        if not self.history:
            print("📭 暂无查询历史。")
            return
        print("------ 最近查询记录 ------")
        for i, h in enumerate(reversed(self.history), 1):
            print(f"{i:>2}. {h['time']}   {h['city']}   {h['temp']}℃")
        print("-" * 26)

    def clear_history(self):
        """清空历史记录"""
        self.history = []
        self._save_history()
        print("✅ 历史记录已清空。")

    # ---------- 主循环 ----------
    def run(self):
        menu = """
╔══════════════════════════════╗
║       天气查询系统 v1.0      ║
╠══════════════════════════════╣
║  1. 查询城市天气             ║
║  2. 查看查询历史             ║
║  3. 清空历史记录             ║
║  0. 退出系统                 ║
╚══════════════════════════════╝"""
        while True:
            print(menu)
            choice = input("请输入选项：").strip()

            if choice == "1":
                city = input("请输入城市名（如 北京 / Shanghai / Tokyo）：").strip()
                if city:
                    self.query(city)
                else:
                    print("⚠️ 城市名不能为空。")
            elif choice == "2":
                self.show_history()
            elif choice == "3":
                self.clear_history()
            elif choice == "0":
                print("👋 感谢使用，再见！")
                break
            else:
                print("⚠️ 无效选项，请重新输入。")


if __name__ == "__main__":
    WeatherSystem().run()