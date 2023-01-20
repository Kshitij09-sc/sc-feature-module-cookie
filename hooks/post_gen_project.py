from pathlib import Path
import os
import shutil

MAIN_SOURCE_SET = Path("src/main/java")
ANDROID_TEST_SOURCE_SET = Path("src/androidTest/java")
TEST_SOURCE_SET = Path("src/test/java")
PACKAGE_NAME = '{{ cookiecutter.package_name }}'
MODULE_NAME = '{{ cookiecutter.module_name }}'

def expand_package(root: Path):
    src_path = root/PACKAGE_NAME
    dest_path = root/PACKAGE_NAME.replace('.','/')
    shutil.copytree(src_path, dest_path)
    shutil.rmtree(src_path)

def expand_module():
    old_root = Path(os.path.realpath(os.path.curdir))
    new_root = MODULE_NAME[1:] if MODULE_NAME.startswith(":") else MODULE_NAME
    new_root = old_root.parent/new_root.replace(":","/")
    new_root.mkdir(parents=True, exist_ok=True)
    for file in os.listdir(old_root):
        src_path = old_root/file
        dst_path = new_root/file
        shutil.move(src_path, dst_path)
    old_root.rmdir()
    

def make_settings_entry():
    settings_gradle_path = Path("../settings.gradle.kts")
    if settings_gradle_path.exists():
        with open(settings_gradle_path, "a") as settings_file:
            settings_file.writelines(f"includeIfEnabled(\"{MODULE_NAME}\")\n")

if __name__ == "__main__":
    make_settings_entry()
    expand_package(MAIN_SOURCE_SET)
    expand_package(ANDROID_TEST_SOURCE_SET)
    expand_package(TEST_SOURCE_SET)
    expand_module()