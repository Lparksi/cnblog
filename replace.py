import os
import re
import argparse
from pathlib import Path

def replace_image_urls_in_file(file_path: Path, old_domain: str, new_domain: str) -> None:
    """替换单个Markdown文件中的图片链接域名"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 使用正则表达式查找并替换图片链接
        pattern = re.compile(rf'!\[.*?\]\((.*?{re.escape(old_domain)}.*?)\)')
        new_content = pattern.sub(lambda m: f'![{m.group(0).split("]")[0][2:]}]({m.group(1).replace(old_domain, new_domain)})', content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"已更新: {file_path}")
        else:
            print(f"未修改: {file_path} (未找到匹配的域名)")
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")

def main():
    parser = argparse.ArgumentParser(description='替换Markdown文件中的图片链接域名')
    parser.add_argument('--directory', '-d', required=True, help='要处理的目录路径')
    parser.add_argument('--old-domain', '-o', default='img0.parksi.top', help='要替换的旧域名')
    parser.add_argument('--new-domain', '-n', default='img1.parksi.cn', help='替换后的新域名')
    parser.add_argument('--recursive', '-r', action='store_true', default=True, help='递归处理子目录')
    
    args = parser.parse_args()
    
    target_dir = Path(args.directory)
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"错误: 指定的目录 '{args.directory}' 不存在或不是一个目录")
        return
    
    # 获取所有.md文件
    if args.recursive:
        md_files = list(target_dir.rglob('*.md'))
    else:
        md_files = list(target_dir.glob('*.md'))
    
    if not md_files:
        print(f"在目录 '{args.directory}' 中未找到Markdown文件")
        return
    
    print(f"找到 {len(md_files)} 个Markdown文件，开始处理...")
    
    for file in md_files:
        replace_image_urls_in_file(file, args.old_domain, args.new_domain)
    
    print("处理完成!")

if __name__ == "__main__":
    main()    
