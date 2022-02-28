import os

def main():
    i = 0
    folderPath = input("Enter the path to the folder (for ex: C:/Users/Name/Pictures/Vacation/):")
    Name = input("Enter the name")
    if (os.path.exists(folderPath)):
        for filename in os.listdir(folderPath):
            newName = Name+ " " + str(i) + ".jpg"
            filePath = folderPath + filename
            newName = folderPath + newName
            os.rename(filePath, newName)
            i += 1
        print("Success")
    else:
        print("Folder does not exist")
    #path = "C:/Users/Elisha/Pictures/Test/"
    
if __name__ == '__main__':
    main()