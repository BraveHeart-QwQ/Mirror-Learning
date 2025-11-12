# -*- coding: utf-8 -*-
import os
import re

CONTENT = r""""""

def ProcessAIOutput(content: str) -> str:
    # 按顺序删除特定内容
    removeWords = ("您的", "你的", "您", "你", "**")
    for word in removeWords:
        content = content.replace(word, "")

    # 替换
    replaceWords = [
        ("“", "\""),
        ("”", "\""),
        ("‘", "\""),
        ("’", "\""),
        ("*   ", "- "),
        ("````", "```"),
        ("```", "$$##@@"), # 临时替换
    ]
    for old, new in replaceWords:
        content = content.replace(old, new)

    # 删除 code
    content = content.replace("`", "")
    content = content.replace("$$##@@", "```")

    # TODO 数字替换

    # 将 Markdown 表格转为简化格式
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| ") and len(line) >= 9:
            line = line[2:-2]  # 删除开头的 '| ' 和结尾的 ' |'
            if line.endswith("。"):
                line = line[:-1]  # 删除结尾的 '。'
            lines[i] = line

    return "\n".join(lines)

if __name__ == "__main__":
    processedContent = ProcessAIOutput(CONTENT)
    # 保存到文件里
    with open("ProcessAIOutputResult.md", "w", encoding="utf-8") as f:
        f.write(processedContent)
    
