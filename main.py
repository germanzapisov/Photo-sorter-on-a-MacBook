from pathlib import Path
from datetime import datetime

class MainHandler:

    def __init__(self, folder):
        self.__folder = folder

    @property
    def folder(self):
        return self.__folder


    def timer(self):
        return datetime.now().strftime('%H.%M.%S')

    def txt_sorter(self):
        for file in self.folder.glob(f"*.{file_signature[txt_asc]}"):
            if file.exists():
                file.rename(create_folder_file / file.name)
        print(f'{self.timer()} | successfully ')

    def img_sorter(self):
        for img in self.folder.glob("*"):
            if img.is_file():
                with open(img, "rb") as f:
                    reader = f.read(20)
                    if reader.startswith(img_signature[img_asc]):
                        img.rename(create_folder_img / img.name)
        print(f'{self.timer()} | successfully ')


if __name__ == "__main__":
    folder = Path.home() / "Downloads"
    filehandler = MainHandler(folder)

    file_signature = {
        0x1: "docx",
        0x2: "pdf",
        0x3: "txt",
        0x4: "py",
    }

    img_signature = {
        0x1: b"\xff\xd8\xff",
        0x2: b"\x89PNG",
        0x3: b"typavif",
    }

    while True:
        try:
            signature_asc = int(
                input(
                    """
               Enter the desired action
               1 >> Sort text files
               2 >> Sort images
               3 >> exit
               """
                )
            )

            if signature_asc == 0b1:
                txt_asc = int(
                    input(
                        """
                1 - docx
                2 - pdf
                3 - txt
                """
                    )
                )
                create_folder_file = Path.home() / "Desktop" / file_signature[txt_asc]
                create_folder_file.mkdir(exist_ok=True)
                filehandler.txt_sorter()

            elif signature_asc == 0b10:
                img_asc = int(
                    input(
                        """
                       1 - jpg
                       2 - png
                       3 - avif
                       """
                    )
                )
                create_folder_img = Path.home() / "Desktop" / "image"
                create_folder_img.mkdir(exist_ok=True)
                filehandler.img_sorter()

            elif signature_asc == 0b11:
                print("bye!")
                break
            else:
                print("wrong number")
        except ValueError:
            print("error")
