import os
def install(lib):
    os.system(f'pip install {lib}')

libs=['threaded','requests','selenium']
for i in libs:
    install(i)