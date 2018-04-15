class Dfl:
    '''
    dlfile返回download目录下的文件全名列表;
    dlname返回download目录下的文件名列表（不包含扩展名）
    '''
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DOWNLOAD_DIR = BASE_DIR.replace("\\","/")+"/download/"
    flist,nlist=[],[]
    for f in os.listdir(DOWNLOAD_DIR):
        flist.append(f)
        (fname,flx)=f.split(".")
        nlist.append(fname)
    def dlname(self):
        return nlist
    def dlfile(self):
        return flist