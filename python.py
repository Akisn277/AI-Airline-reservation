f = open("C:/Users/AKSHARA/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/Roaming/jupyter/runtime/test.txt", "w")
f.write("YOLO\n MILAN")
f.close()
f1=open("C:/Users/AKSHARA/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/Roaming/jupyter/runtime/test.txt","r")
for i in f1.readlines():
    print(i)  # This checks if the file is readable
f1.close()  # Always close the file after use
 