import os
import shutil


# 解析txt文件的函数
def parse_txt_file(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    data_entries = []
    for i in range(0, len(lines), 7):
        title = lines[i].split("标题：")[1]
        authors = lines[i + 1].split("作者：")[1].split(";")
        journal = lines[i + 2].split("期刊名称：")[1]
        year = lines[i + 3].split("出版时间：")[1].split("；")[0].split()[-1]
        data_entries.append(
            {"title": title, "authors": authors, "journal": journal, "year": year}
        )
    return data_entries


# 根据解析到的数据构建期望的PDF文件名
# def generate_expected_pdf_name(entry):
#     if len(entry["authors"]) == 1:
#         author_str = entry["authors"][0].split(",")[0]
#     elif len(entry["authors"]) == 2:
#         author_str = (
#             entry["authors"][0].split(",")[0] + "_" + entry["authors"][1].split(",")[0]
#         )
#     else:
#         author_str = entry["authors"][0].split(",")[0] + " et al"
#     return f"{entry['year']}_{author_str}_{entry['journal']}.pdf"

# 根据解析到的数据构建期望的PDF文件名
def generate_expected_pdf_name(entry):
    if len(entry['authors']) == 1:
        author_str = entry['authors'][0].split(",")[0].strip()
    elif len(entry['authors']) == 2:
        author_str = entry['authors'][0].split(",")[0].strip() + "_" + entry['authors'][1].split(",")[0].strip()
    else:
        author_str = entry['authors'][0].split(",")[0].strip() + " et al"
    return f"{entry['year']}_{author_str}_{entry['journal']}.pdf"


# 主函数
def main():
    txt_path = "files/numbering_15.txt"  # 指定txt文件的路径
    source_folder = "sciAward"  # 指定PDF文件所在的文件夹路径
    target_folder = "output/rep_paper_15"  # 指定新的文件夹路径

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    data_entries = parse_txt_file(txt_path)
    for idx, entry in enumerate(data_entries, 1):
        expected_pdf_name = generate_expected_pdf_name(entry)
        source_pdf_path = os.path.join(source_folder, expected_pdf_name)
        if os.path.exists(source_pdf_path):
            target_pdf_path = os.path.join(target_folder, f"{idx}_{expected_pdf_name}")
            shutil.copy(source_pdf_path, target_pdf_path)
        else:
            print(f"PDF not found for: {expected_pdf_name}")


if __name__ == "__main__":
    main()
