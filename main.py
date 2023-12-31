#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: hakuna-max
@date: 2023/8/13
"""
import openpyxl


def parse_ris(ris_text):
    entries = ris_text.split("ER  -")
    parsed_entries = []

    for entry in entries:
        lines = entry.strip().split("\n")
        parsed_entry = {}
        for line in lines:
            if "  - " not in line:
                continue
            key, value = line.split("  - ", 1)
            if key in parsed_entry:
                parsed_entry[key].append(value)
            else:
                parsed_entry[key] = [value]

        parsed_entries.append(parsed_entry)

    return parsed_entries


def load_jcr_data(filename):
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook.active

    jcr_data = {}
    for row in sheet.iter_rows(min_row=2, values_only=True):  # 跳过标题行
        journal_name = row[0].upper().strip()  # 将期刊名称转换为大写并去除空格
        jcr_values = row[5:11]
        jcr_data[journal_name] = jcr_values

    print("Loaded JCR data:", jcr_data)
    return jcr_data


def get_jcr_ranking(jcr_values):
    rankings = {
        "SCIE(Q1)": "SCI一区",
        "SCIE(Q2)": "SCI二区",
        "SCIE(Q3)": "SCI三区",
        "SCIE(Q4)": "SCI四区",
        "SSCI(Q1)": "SSCI一区",
        "SSCI(Q2)": "SSCI二区",
        "SSCI(Q3)": "SSCI三区",
        "SSCI(Q4)": "SSCI四区"
    }

    scie_ranks = []
    ssci_ranks = []

    for value in jcr_values:
        if value is None:
            continue
        if value.startswith("SCIE"):
            scie_ranks.append(rankings.get(value, value))
        elif value.startswith("SSCI"):
            ssci_ranks.append(rankings.get(value, value))

    # 选择最高的分区
    scie_rank = sorted(scie_ranks)[0] if scie_ranks else None
    ssci_rank = sorted(ssci_ranks)[0] if ssci_ranks else None

    final_ranks = [rank for rank in [scie_rank, ssci_rank] if rank]

    return ", ".join(final_ranks)


def format_entry(entry):
    title = entry.get("TI", [""])[0]
    authors = "; ".join(entry.get("AU", []))
    journal = entry.get("T2", [""])[0].upper()
    year = entry.get("PY", [""])[0]

    da_values = entry.get("DA", [""])[0].split("/")
    month = da_values[1] if len(da_values) > 1 else ""

    volume = entry.get("VL", [""])[0]
    s_pages = entry.get("SP", [""])[0]
    e_pages = entry.get("EP", [""])[0]

    month_map = {
        "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
        "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
        "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
    }

    formatted_entry = f"标题：{title}\n"
    formatted_entry += f"作者：{authors}\n"
    formatted_entry += f"期刊名称：{journal}\n"

    if e_pages:
        formatted_entry += f"出版时间：{month_map.get(month, month)} {year}；卷：{volume}，页：{s_pages}-{e_pages}\n"
    elif s_pages:
        formatted_entry += f"出版时间：{month_map.get(month, month)} {year}；卷：{volume}，文献号：{s_pages}\n"
    else:
        formatted_entry += f"出版时间：{month_map.get(month, month)} {year}；卷：{volume}，文献号(页)：\n"

    formatted_entry += "JCR分区：\n"
    formatted_entry += "引用位置：\n"
    formatted_entry += "引用原句：\n"

    return formatted_entry


def main():
    with open("sample.ris", "r", encoding="utf-8") as f:  # change the path of file
        ris_text = f.read()

    jcr_data = load_jcr_data("jcr_2021.xlsx")

    parsed_entries = parse_ris(ris_text)
    sorted_entries = sorted(parsed_entries, key=lambda x: x.get("PY", ["0"])[0], reverse=True)

    formatted_entries = []
    for index, entry in enumerate(sorted_entries, 1):  # 开始索引从1开始
        formatted_entry = format_entry(entry)
        # 在标题前添加序号标记
        formatted_entry = formatted_entry.replace("标题：", f"[{index}] 标题：")
        journal_name = entry.get("T2", [""])[0].upper().strip()
        print("Processing journal:", journal_name)
        if journal_name in jcr_data:
            jcr_ranking = get_jcr_ranking(jcr_data[journal_name])
            print("JCR ranking is: ", jcr_ranking)
            print("Found JCR ranking:", jcr_ranking)
            formatted_entry = formatted_entry.replace("JCR分区：", f"JCR分区：{jcr_ranking}")
        formatted_entries.append(formatted_entry)

    formatted_text = "\n\n".join(formatted_entries)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(formatted_text)


if __name__ == "__main__":
    main()
