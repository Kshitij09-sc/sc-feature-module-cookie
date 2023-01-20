from pathlib import Path
import os
import shutil

MAIN_SOURCE_SET = "src/main/java"
ANDROID_TEST_SOURCE_SET = "src/androidTest/java"
TEST_SOURCE_SET = "src/test/java"
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
    shutil.move(old_root, new_root)
    os.chdir(old_root.parent)
    return new_root

def make_settings_entry():
    settings_gradle_path = Path(f"{os.getcwd()}/settings.gradle.kts")
    if settings_gradle_path.exists():
        with open(settings_gradle_path, "a") as settings_file:
            settings_file.writelines(f"includeIfEnabled(\"{MODULE_NAME}\")\n")

if __name__ == "__main__":
    new_root = expand_module()
    expand_package(new_root/MAIN_SOURCE_SET)
    expand_package(new_root/ANDROID_TEST_SOURCE_SET)
    expand_package(new_root/TEST_SOURCE_SET)
    make_settings_entry()
    