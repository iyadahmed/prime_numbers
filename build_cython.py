import subprocess as sp

if __name__ == "__main__":
    sp.run(["cythonbuilder", "build", "--include-numpy", "-y"])
