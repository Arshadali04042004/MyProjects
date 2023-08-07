fileToCopy = input("Enter the File Path to copy :")
fileToPaste = input("Enter the File Path to Paste :")

filepathCopy =  open(fileToCopy,'r')
filepathPaste = open(fileToPaste,'w')

copyFile = filepathCopy.readlines()
pasteFile = filepathPaste.writelines(copyFile)

filepathPaste.close()
