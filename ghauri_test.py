import os

def process_file(filename):
    with open(filename, 'r') as file:
        urls = file.readlines()
    
    for url in urls:
        url = url.strip()
        command = f'ghauri --url "{url}" --dbs --level=3 --threads=3 --confirm --banner --batch'
        os.system(command)

def main():
    filename = input("Enter the filename containing URLs: ")
    if not os.path.isfile(filename):
        print("File not found.")
        return
    
    process_file(filename)

if __name__ == "__main__":
    main()

