import zipfile

def extract_files(archieve_path, dest_dir):
    with zipfile.ZipFile(archieve_path, 'r') as archieve:
        archieve.extractall(dest_dir)

if __name__ == "__main__":
    extract_files("..\dest\compressed.zip", "../dest")