# Define all the functions you want to execute asynchronously(Parallely) in django views in qcluster worker

def softgo_greet():
    print("Django Q cluster Running, Parrallel Asynchronous Worker active.")
    return 1