import re

# 读取readme.md文件
with open('readme.md', 'r', encoding='utf-8') as file:
    content = file.read()

# 定义替换函数
def replace_images(match):
    img_src = match.group(1)
    return f'<div style="text-align: center;">\n    <img src="{img_src}" alt="alt text" style="width:50%; height:auto;"></div>'

# 使用正则表达式替换图像格式
new_content = re.sub(r'!\[alt text\]\((.*?)\)', replace_images, content)

# 将修改后的内容写回文件
with open('readme.md', 'w', encoding='utf-8') as file:
    file.write(new_content)

print("替换完成！")
