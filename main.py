# 標準ライブラリ
from pathlib import Path
import importlib.util
import inspect
import pygame as pg

# 独自モジュール
from modules.charactor import Charactor
from unit.species import Species

# 関数
def extract_subclasses_from_folder(folder_path, base_class):
    """
    指定フォルダ内のファイルからbase_classクラスを継承したクラスを抽出する
    """
    subclasses = []
    folder = Path(folder_path)

    import sys
    sys.path += [str(folder.resolve())]

    # 指定フォルダ内のpyファイルを走査
    for file_path in folder.glob("*.py"):
        # ファイルパスから拡張子を排除(ex:"hoge.py">"hoge")
        module_name = file_path.stem

        # モジュールを動的にロード
        try:
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)
        except Exception as e:
            print(f"ファイルのロードに失敗しました ({file_path.name}): {e}")
            continue

        # モジュール内のクラスや関数などすべての属性を確認
        for name, obj in inspect.getmembers(module, inspect.isclass):
            # base_classを継承し、かつbase_class自体ではないクラスを選別
            if issubclass(obj, base_class) and obj is not base_class:
                # そのモジュール内で定義されたクラスであることも確認する
                if obj.__module__ == module_name:
                    subclasses += [obj]

    return subclasses

classes = extract_subclasses_from_folder(".", Species)

# ゲームループ
# game = True
# while(game):
#     break
print("HOGE")