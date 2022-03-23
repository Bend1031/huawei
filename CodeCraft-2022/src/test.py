import os
base_path=os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
with open(base_path+"/output/test.txt","a") as f:
    print("test",end="",file=f)