"""
   Перейдти по ссылке, 
   найдти файлообменник zipfiles, 
   перейдти по ссылке,
   почередно переход по ссылкам от 1 до n,
   найти ссылку на файл, и скачать его.
"""

from pathlib import Path
import wget


def check_path(path: str) -> None:
    """
    Check directory exsists,
    if not raise FileNotFoundError
    """
    cwd = Path().cwd()
    exist = Path(cwd, path).exists()
    if not exist:
        raise FileNotFoundError


def create_dir(path: str) -> None:
    """
    Create directory
    param: path directory path
    """
    cwd = Path().cwd()
    Path(cwd, path).mkdir()


def download_file(url: str, save_path: str) -> None:
    """
    Функция обертка wget.dowload
    param: url Ссылка на файл ur
    param: save_path путь для загруженного файа
    """
    wget.download(url, save_path)


def main() -> None:
    url: str = "http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg"
    file_name: str = url.split("/")[-1]
    dowload_dir: str = "./downloads"
    save_path: str = "/".join([dowload_dir, file_name])

    try:
        print("... Check directory exsists")
        check_path(dowload_dir)
        print(f"[✓] Directory is exsists {dowload_dir}")
    except FileNotFoundError:
        print("[X] Directory not exsists ...")
        create_dir(dowload_dir)
        print(f"... Create directory {dowload_dir}")
        check_path(dowload_dir)
        print(f"[✓] Directory is exsists {dowload_dir}")

    print(f"... Download from url: {url}")
    print(f"... Save to: {save_path}")

    download_file(url, save_path)
    print()
    print("[✓] Complete download")


if __name__ == "__main__":
    main()
