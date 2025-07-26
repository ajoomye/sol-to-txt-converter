import os
import shutil
import zipfile

def convert_sol_to_txt_in_new_folder(src_root, dst_root):
    for foldername, subfolders, filenames in os.walk(src_root):
        # Create mirrored directory in destination
        rel_path = os.path.relpath(foldername, src_root)
        dst_folder = os.path.join(dst_root, rel_path)
        os.makedirs(dst_folder, exist_ok=True)

        for filename in filenames:
            if filename.endswith('.sol'):
                src_path = os.path.join(foldername, filename)
                dst_filename = os.path.splitext(filename)[0] + '.txt'
                dst_path = os.path.join(dst_folder, dst_filename)
                with open(src_path, 'r', encoding='utf-8') as sol_file:
                    content = sol_file.read()
                with open(dst_path, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(content)
                print(f"Converted: {src_path} -> {dst_path}")

def zip_folder(src_folder, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for foldername, subfolders, filenames in os.walk(src_folder):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, src_folder)
                zf.write(file_path, arcname)
        print(f"Zipped folder {src_folder} -> {zip_path}")

if __name__ == "__main__":
    foldernames = ["src","test"]
    for foldername in foldernames:
        #The protocol name here is flexible vaults, but feel free to change it to anything
        main_folder = f"./{foldername}"  
        output_folder = f"./{foldername}_txt"  
        zip_file_path = f"{foldername}_txt_flexible_vaults.zip"   

        # Convert .sol to .txt in new folder with mirrored structure
        convert_sol_to_txt_in_new_folder(main_folder, output_folder)

        # Zip the original main folder
        zip_folder(output_folder, zip_file_path)

        destination_folder = f"/mnt/c/Users/clibe/Documents/{zip_file_path}"
        shutil.copy(zip_file_path, destination_folder)
        print(f"Copied zip to {destination_folder}")
