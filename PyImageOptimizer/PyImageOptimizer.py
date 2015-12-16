# -*- coding: utf-8 -*-
#!/usr/bin/env python

from __future__ import print_function
import os
import requests
import concurrent.futures


def optimize_jpg(file_path,backup=False):
    if type(file_path)!=str :
        raise Exception("Image file path must be string")
    if type(backup)!=bool:
        raise Exception("Backup must be of type Boolean")
    
    if not os.path.isfile(os.path.abspath(file_path)) and not os.path.isdir(os.path.abspath(file_path)):
        raise Exception("file path must be a valid directory or a file path "+os.path.abspath(file_path) )
        
    if os.path.isfile(file_path) and os.path.getsize(file_path)>>20 < 5:
        if backup:
            shutil.copyfile(file_path,file_path.rstrip(".jpg")+".backup.jpg")
        files={'input':open(file_path,'rb')}            
        r=requests.post("http://jpgoptimiser.com/optimise",files=files,stream=True)
        if r.status_code == 200:
                 with open(file_path, 'wb') as f:
                    for chunk in r.iter_content(1024):
                            f.write(chunk)
                
        elif os.path.isdir(file_path):
            for root,dirs,files in os.walk("."):
            for file in files:
                if file.endswith(".jpg"):
                     optimize_jpg(os.path.abspath(os.path.join(root,file)),backup)

def optimize_png(file_path,backup=False):
    if type(file_path)!=str :
        raise Exception("Image file path must be string")
    if type(backup)!=bool:
        raise Exception("Backup must be of type Boolean")
    
    if not os.path.isfile(os.path.abspath(file_path)) and not os.path.isdir(os.path.abspath(file_path)):
        raise Exception("file path must be a valid directory or a file path "+os.path.abspath(file_path) )
        
    if os.path.isfile(file_path) and os.path.getsize(file_path)>>20 < 5:
        if backup:
            shutil.copyfile(file_path,file_path.rstrip(".png")+".backup.png")
        files={'input':open(file_path,'rb')}            
        r=requests.post("http://pngcrush.com/optimise",files=files,stream=True)
        if r.status_code == 200:
                 with open(file_path, 'wb') as f:
                    for chunk in r.iter_content(1024):
                            f.write(chunk)
                
        elif os.path.isdir(file_path):
            for root,dirs,files in os.walk("."):
            for file in files:
                if file.endswith(".png"):
                     optimize_png(os.path.abspath(os.path.join(root,file)),backup)



def optimize(file_path,backup=False):
    if os.path.isfile(file_path):
        print ("Compressing file: " + file_path)
        if file_path.endswith(".jpg"):
            optimize_jpg(file_path,backup)
        elif file_path.endswith(".png"):
            optimize_png(file_path,backup)
    if os.path.isdir(file_path):
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            for root,dirs,files in os.walk(file_path):
                for file in files:
                    print ("Compressing file: " + file_path)
                    if file.endswith(".jpg"):
                        executor.submit(optimize_jpg,file_path,backup)
                    elif file.endswith(".png"):
                        executor.submit(optimize_png,file_path,backup)