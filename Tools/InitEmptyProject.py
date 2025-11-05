# -*- coding: utf-8 -*-
import os

def createAssetsSubDir():
    SUB_DIR_LIST = (
        "Editor",
        "Editor/Resources",
        "Editor Default Resources",
        "Gizmos",
        "Plugins",
        "Resources",
        "Standard Assets",
        "StreamingAssets",
        "AssetBundles",
        "Art",
        "Audio",
        "Content",
        "Data",
        "Documentation",
        "Prefabs",
        "Samples",
        "Settings",
        "Scenes",
        "Scripts",
        "Shaders",
    )
    assetsPath = os.path.join(os.getcwd(), "Assets")
    for subDir in SUB_DIR_LIST:
        dirPath = os.path.join(assetsPath, subDir)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
            print(f"Created directory: {dirPath}")
        else:
            print(f"Directory already exists: {dirPath}")

if __name__ == "__main__":
    createAssetsSubDir()
