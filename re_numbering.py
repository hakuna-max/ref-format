def main():
    # 读取原始txt文件的数据
    with open("files/13.txt", "r", encoding="utf-8") as file:
        data = file.read()

    # 根据空行拆分数据
    entries = data.split("\n\n")

    # 为每个标题加上序号
    new_data = ""
    counter = 1
    for entry in entries:
        new_data += entry.replace("标题：", f"[{counter}] 标题：") + "\n\n"
        counter += 1

    # 保存处理后的数据到新的txt文件
    with open("output/processed_data_13.txt", "w", encoding="utf-8") as file:
        file.write(new_data.strip())

    print("处理后的数据已保存到 output/processed_data_13.txt")


if __name__ == "__main__":
    main()