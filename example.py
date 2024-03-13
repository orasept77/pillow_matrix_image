from path import Path
from main import gen_qr_code


text = "link"
path_to_download = Path().joinpath("example", "Logo")  # Путь до фона qr кода
path_to_save = Path().joinpath("example", "example122.png")  # Куда сохранять результат и под каким именем (обязательно в png)

gen_qr_code(text, path_to_download, path_to_save)