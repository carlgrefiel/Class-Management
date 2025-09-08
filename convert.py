import os
import shutil
import win32com.client

def convert_and_copy_recursive(source_root):
    converted_root = os.path.join(source_root, "convertedDoc")
    os.makedirs(converted_root, exist_ok=True)

    # Start Word
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False

    for dirpath, _, filenames in os.walk(source_root):
        # Skip the convertedDoc folder itself
        if "convertedDoc" in dirpath:
            continue

        for filename in filenames:
            # ❌ Skip temporary files that start with "~$"
            if filename.startswith("~$"):
                continue

            ext = filename.lower()
            if ext.endswith(".doc") and not ext.endswith(".docx") or ext.endswith(".docx"):
                source_path = os.path.join(dirpath, filename)

                # Create mirrored directory inside convertedDoc
                relative_path = os.path.relpath(dirpath, source_root)
                target_dir = os.path.join(converted_root, relative_path)
                os.makedirs(target_dir, exist_ok=True)

                if ext.endswith(".doc") and not ext.endswith(".docx"):
                    # Convert .doc to .docx
                    docx_name = os.path.splitext(filename)[0] + ".docx"
                    target_path = os.path.join(target_dir, docx_name)
                    try:
                        print(f"Converting: {source_path} -> {target_path}")
                        doc = word.Documents.Open(source_path)
                        doc.SaveAs(target_path, FileFormat=16)
                        doc.Close()
                    except Exception as e:
                        print(f"[ERROR] Failed to convert {source_path}: {e}")
                elif ext.endswith(".docx"):
                    # Copy .docx as-is
                    target_path = os.path.join(target_dir, filename)
                    try:
                        print(f"Copying: {source_path} -> {target_path}")
                        shutil.copy2(source_path, target_path)
                    except Exception as e:
                        print(f"[ERROR] Failed to copy {source_path}: {e}")

    word.Quit()
    print("✅ Done converting and copying all documents.")

# 🔁 Use UNC path or map to a drive
source_root = r"\\192.168.30.93\carl\Yna\Updateddocs"
convert_and_copy_recursive(source_root)
