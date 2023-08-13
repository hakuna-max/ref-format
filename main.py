
# 该程序将webofscience上导出的ris文件，如：
# TY  - JOUR
# TI  - Assessing energy vulnerability and its impact on carbon emissions: A global case
# AU  - Liu, Yang
# AU  - Dong, Kangyin
# AU  - Jiang, Qingzhe
# T2  - Energy Economics
# AB  - Reducing the vulnerability of the energy system can help safeguard the normal functioning of the economy and society and promote the transition to a green, low-carbon system, which in turn has a potential impact on the global greenhouse effect. To explore the causal relationship between energy vulnerability and CO2 emissions, this study first constructs a composite energy vulnerability index (EVI) for empirical analysis based on a balanced panel dataset of 119 countries from 2000 to 2019. The study then examines the potential heterogeneity. Further, to investigate the impact mechanism, this study decomposes the total effect into scale effect, structural effect, and technology effect for detailed discussion. The main findings are: (1) decreased energy vulnerability can help curb CO2 emissions, leading to a “win-win” situation; (2) significant heterogeneity exists in the relationship between EVI and CO2 emissions; (3) decreased energy vulnerability can not only reduce CO2 emissions directly, but also indirectly by lowering the total primary energy supply, promoting renewable energy use, and enhancing energy efficiency. In light of these findings, we offer specific recommendations for reducing energy vulnerability and limiting the greenhouse effect.
# DA  - 2023/03/01/
# PY  - 2023
# DO  - 10.1016/j.eneco.2023.106557
# DP  - ScienceDirect
# VL  - 119
# SP  - 106557
# J2  - Energy Economics
# LA  - en
# SN  - 0140-9883
# ST  - Assessing energy vulnerability and its impact on carbon emissions
# UR  - https://www.sciencedirect.com/science/article/pii/S0140988323000555
# Y2  - 2023/06/09/03:35:07
# KW  - CO emissions
# KW  - Energy vulnerability
# KW  - Global case
# KW  - Heterogeneity
# KW  - Mediating effects
# ER  -
#
# 转换为如下的格式：
# [2] 标题：Intersecting near-optimal spaces: European power systems with more resilience to weather variability
# 作者：Grochowicz, Aleksander; van Greevenbroek, Koen; Benth, Fred Espen; Zeyringer, Marianne
# 期刊名称：ENERGY ECONOMICS
# 出版时间：Feb 2023；卷：118，页：106496
# JCR分区：
# 引用位置：
# 引用原句：


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


def format_entry(entry):
    title = entry.get("TI", [""])[0]
    authors = "; ".join(entry.get("AU", []))
    journal = entry.get("T2", [""])[0].upper()
    year = entry.get("PY", [""])[0]

    da_values = entry.get("DA", [""])[0].split("/")
    month = da_values[1] if len(da_values) > 1 else ""

    volume = entry.get("VL", [""])[0]
    pages = entry.get("SP", [""])[0]

    month_map = {
        "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
        "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
        "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
    }

    formatted_entry = f"标题：{title}\n"
    formatted_entry += f"作者：{authors}\n"
    formatted_entry += f"期刊名称：{journal}\n"
    formatted_entry += f"出版时间：{month_map.get(month, month)} {year}；卷：{volume}，页：{pages}\n"
    formatted_entry += "JCR分区：\n"
    formatted_entry += "引用位置：\n"
    formatted_entry += "引用原句：\n"

    return formatted_entry


def main():
    with open("sample.ris", "r", encoding="utf-8") as f:
        ris_text = f.read()

    parsed_entries = parse_ris(ris_text)
    sorted_entries = sorted(parsed_entries, key=lambda x: x.get("PY", ["0"])[0], reverse=True)

    formatted_entries = []
    for index, entry in enumerate(sorted_entries, 1):  # 开始索引从1开始
        formatted_entry = format_entry(entry)
        # 在标题前添加序号标记
        formatted_entry = formatted_entry.replace("标题：", f"[{index}] 标题：")
        formatted_entries.append(formatted_entry)

    formatted_text = "\n\n".join(formatted_entries)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(formatted_text)


if __name__ == "__main__":
    main()
