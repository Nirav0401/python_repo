import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}") 

if __name__ == "__main__":
    
    try:    
        files = os.listdir()
        files.remove("clear_clutter.py")

        createIfNotExist('Images')
        createIfNotExist('Docs')
        createIfNotExist("ExcelFiles")
        createIfNotExist('Ones')
        createIfNotExist('Media')
        createIfNotExist("Programfiles")
        createIfNotExist('Others')

        imgExts = [".png", ".jpg", ".jpeg", ".jfif", ".gif", ".tiff", ".psd", ".eps", ".ai", ".indd", ".raw"]
        images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

        docExts = [".txt", ".docx", "doc", ".odt", ".ods", ".log", ".pptx", ".odg"]
        docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

        ExcelExts = [".xls", ".xlsx", "xlsm", ".pdf", ".xltx", ".xlsb", ".csv"]
        excels = [file for file in files if os.path.splitext(file)[1].lower() in ExcelExts]

        oneExts = [".zip", ".7z", ".Apk", ".exe", ".out"]
        ones = [file for file in files if os.path.splitext(file)[1].lower() in oneExts]

        mediaExts = [".mp4", ".mp3", ".flv"]
        medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

        cExts = [".bin", ".hex", ".c", ".py", "File", "File folder", ".h", ".json"]
        cs = [file for file in files if os.path.splitext(file)[1].lower() in cExts]

        others = []
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
                others.append(file)

        move("Images", images)
        move("Docs", docs)
        move("ExcelFiles", excels)
        move("Ones", ones)
        move("Media", medias)
        move("Programfiles", cs)
        move("Others", others)
    
    except OSError as error:
        print(error)

    finally:
        print("Congratulations! You have cleared the clutter in your system!!!")        





