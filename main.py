import os
import subprocess
from pathlib import Path

def create_folders():
    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    print("The 'input' and 'output' folders have been created. Please put the files to be converted into the 'input' folder.")

def delete_temp_files(folder, extension):
    for filename in os.listdir(folder):
        if filename.endswith(extension):
            os.remove(os.path.join(folder, filename))
            print(f"Temporary files deleted: {filename}")

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
                print(f"{input_file} Conversion to {output_file} successful!")
            else:
                print(f"{input_file} Conversion to {output_file} failed!")
                print("error message:", result.stderr)

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
                "-f", "PVRTC1_4"  
            ]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{input_file} Conversion to {output_file} successful!")
            else:
                print(f"{input_file} Conversion to {output_file} failed!")
                print("错误信息:", result.stderr)

if __name__ == "__main__":
    
    current_dir = Path(__file__).parent

    pvrtxtool_path = current_dir / "CLI" / "PVRTexToolCLI"  

    create_folders()

    input("Please put the files to be converted into the 'input' folder and press Enter to continue...")

    convert_pvr_to_png(pvrtxtool_path)

    convert_png_to_pvr(pvrtxtool_path)

    delete_temp_files("input", ".pvr")
    delete_temp_files("output", ".pvr")

    print("All files are converted.")
