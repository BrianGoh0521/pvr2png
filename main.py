import os
import subprocess
from pathlib import Path

def create_folders():
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    print("已创建 'input' 和 'output' 文件夹。请将需要转换的文件放入 'input' 文件夹中。")

def delete_temp_files(folder, extension):
    for filename in os.listdir(folder):
        if filename.endswith(extension):
            os.remove(os.path.join(folder, filename))
            print(f"已删除临时文件: {filename}")

def convert_pvr_to_png(pvrtxtool_path):
    input_folder = "input"
    output_folder = "output"

    for filename in os.listdir(input_folder):
        if filename.endswith(".pvr"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace(".pvr", ".png"))
            command = [
                str(pvrtxtool_path),
                "-i", input_file,
                "-d", output_file
            ]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{input_file} 转换为 {output_file} 成功!")
            else:
                print(f"{input_file} 转换为 {output_file} 失败!")
                print("错误信息:", result.stderr)

def convert_png_to_pvr(pvrtxtool_path):
    input_folder = "input"
    output_folder = "output"

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace(".png", ".pvr"))
            command = [
                str(pvrtxtool_path),
                "-i", input_file,
                "-o", output_file,
                "-f", "PVRTC1_4"  # 指定PVR格式
            ]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{input_file} 转换为 {output_file} 成功!")
            else:
                print(f"{input_file} 转换为 {output_file} 失败!")
                print("错误信息:", result.stderr)

if __name__ == "__main__":
    # 获取当前脚本所在的目录
    current_dir = Path(__file__).parent

    # 定义PVRTexToolCLI的路径
    pvrtxtool_path = current_dir / "CLI" / "PVRTexToolCLI"  # 更新为实际路径

    # 创建 input 和 output 文件夹
    create_folders()

    # 提示用户将文件放入 input 文件夹
    input("请将需要转换的文件放入 'input' 文件夹后按回车键继续...")

    # 执行PVR转PNG
    convert_pvr_to_png(pvrtxtool_path)

    # 执行PNG转PVR
    convert_png_to_pvr(pvrtxtool_path)

    # 删除临时的 .pvr 文件
    delete_temp_files("input", ".pvr")
    delete_temp_files("output", ".pvr")

    print("所有文件转换完成。")
