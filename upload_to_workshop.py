#!/usr/bin/env python
from pathlib import Path
import package
import subprocess

# import shutil


steam_uploader_executable_name = "SteamUploader"
steam_uploader_executable_path = Path.cwd() / steam_uploader_executable_name

app_id = 1158310
workshop_id = 2243652060


def steam_uploader(app_id: int, workshop_id: int, upload_directory_path: Path) -> None:
    # if not shutil.which(steam_uploader_executable_name):
    #     raise ValueError("SteamUploader executable does not exist in path.")
    if (
        not steam_uploader_executable_path.exists()
        or not steam_uploader_executable_path.is_file()
    ):
        raise Exception(
            f"SteamUploader executable does not exist or is not a file: {steam_uploader_executable_path}"
        )
    if not upload_directory_path.exists() or not upload_directory_path.is_dir():
        raise Exception(
            f"Upload directory either doesn't exist or is not a dir: {upload_directory_path}"
        )
    steam_uploader_command_list = [
        steam_uploader_executable_path,
        "-a",
        str(app_id),
        "-w",
        str(workshop_id),
        "-c",
        upload_directory_path,
    ]
    subprocess.run(steam_uploader_command_list, check=True)


def main() -> None:
    package.main()
    steam_uploader(app_id, workshop_id, package.package_directory_path)
    package.clear_directory(package.package_directory_path)


if __name__ == "__main__":
    main()
