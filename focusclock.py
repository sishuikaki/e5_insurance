import time

def pomodoro_timer(total_time, focus_time, break_time):
    cycles = total_time // (focus_time + break_time)
    remaining_time = total_time % (focus_time + break_time)

    print("专注时间开始！")
    for i in range(cycles):
        print(f"第 {i+1} 个工作周期")
        time.sleep(focus_time * 60)  # 将专注时间转换为分钟
        print("休息时间开始！")
        time.sleep(break_time * 60)  # 将休息时间转换为分钟

    if remaining_time > 0:
        print(f"第 {cycles+1} 个工作周期")
        time.sleep(remaining_time * 60)  # 将剩余时间转换为分钟

    print("专注时间结束！")

# 使用示例
total_time = 90  # 总时间（单位：分钟）
focus_time = 25  # 专注时间（单位：分钟）
break_time = 5   # 休息时间（单位：分钟）

pomodoro_timer(total_time, focus_time, break_time)
