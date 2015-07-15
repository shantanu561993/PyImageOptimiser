========
Usage
========

To use PyImageOptimizer in a project::

    import PyImageOptimizer
    
To Just optimize the JPG images::

    PyImageOptizer.optimise_jpg(file_path,backup=False)

To Just optimize PNG images::

    PyImageOptizer.optimise_png(file_path,backup=False)
    
To optimise both jpg and png images (regardless of type)::

    PyImageOptimzer.optimize(file_path, backup=False)
    
file_path can be both a single file path and a path of a directory 

changing backup to True will make a backup of your old file

Note::
    PyImageOptimzer.optimize method uses ThreadPool , So if you have a large number of images try to use this method
    
    
