import tarfile
import os


def handle_file(path):
    tar_path(path)
    split_file(path + '.tar', path + '.tar', 2097152)


def tar_path(path):
    tar = tarfile.open('./buffer/' + path + '.tar', 'w:gz')
    for root, dir, files in os.walk(path):
        for file in files:
            fullpath = os.path.join(root, file)
            tar.add(fullpath)
    tar.close()


def extract_tar(path):
    tar = tarfile.open(path)
    tar.extractall()
    tar.close()


def split_file(file, prefix, max_size, buffer=1024):
    """
    file: the input file
    prefix: prefix of the output files that will be created
    max_size: maximum size of each created file in bytes
    buffer: buffer size in bytes

    Returns the number of parts created.
    """
    with open(file, 'r+b') as src:
        suffix = 0
        while True:
            with open('./buffer/' + prefix + '.%s' % suffix, 'w+b') as tgt:
                written = 0
                while written < max_size:
                    data = src.read(buffer)
                    if data:
                        tgt.write(data)
                        written += buffer
                    else:
                        return suffix
                suffix += 1


def cat_files(infiles, outfile, buffer=1024):
    """
    infiles: a list of files
    outfile: the file that will be created
    buffer: buffer size in bytes
    """
    with open('./output/'+outfile, 'w+b') as tgt:
        for infile in sorted(infiles):
            with open(infile, 'r+b') as src:
                while True:
                    data = src.read(buffer)
                    if data:
                        tgt.write(data)
                    else:
                        break


def main():
    tar_path('u.jpg')
    # split_file('screen.png', 'screen.png', 1048576)
    # cat_files(['screen.png.0', 'screen.png.1', 'screen.png.2', 'screen.png.3', 'screen.png.4', 'screen.png.5'], 'screen.png')


if __name__ == '__main__':
    main()
