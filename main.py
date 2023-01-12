from kernel.kernel import Core, Color
from kernel.columner import Columner
from importlib import reload
import os

columner = Columner()

def files_from_curdir(type: str, startwith: str) -> list[str]:
    if type == "var":
        path = os.path.curdir
    else:
        path = os.path.curdir + f"\\var{type.split('[')[1]}"
    variables = []
    for file in os.listdir():
        if file.startswith(startwith):
            variables.append(file)
    return variables

def GetVarList() -> None:
    variables = files_from_curdir("var", "var")
    print(f"{Color.FGCyan}  [~] Variables:")
    for elem in variables:
        print(f"  {elem}")
    print(f"  [~] End variables message{Color.Reset}")

def GenerateVar(i) -> None:
    print(f"{Color.FGCyan}  [~] Generating...")
    variables = files_from_curdir("var", "var")  
    if f"var{i}" in variables:
        print(f"{Color.FGRed}  [~] Variable exist!{Color.Reset}")
        return
    res = os.system(f"mkdir var{i}")
    
    if res != 0:
        print(Color.Reset)
        return
    
    for j in range(1, 28):
        with open(f"./var{i}/task{j}.py", "w", encoding="utf-8") as file:
            file.write("##################################\n")
            file.write("#               #                #\n")
            file.write(f"#  Variable {i}   #     Task {j}     #\n")
            file.write("#               #                #\n")
            file.write("##################################\n")
            file.flush()
    print("  [~] Variable generated!", Color.Reset)
    

def GetTaskList(var: int) -> None:
    variables = files_from_curdir(f"[{var}", "task")
    print(f"{Color.FGCyan}  [~] Tasks from variable - {var}:")
    for elem in variables:
        print(f"  {elem}")
    print(f"  [~] End tasks message{Color.Reset}")

def launch(var: int, task: int) -> None:
    module = __import__(f"var{var}.task{task}", fromlist=[f"var{var}"])
    reload(module)

if __name__ == "__main__":
    core = Core()
    
    core.add_command("var:list", "Get list with variables", GetVarList)
    core.add_command("var:gen", "Generate new variable", GenerateVar)
    core.add_command("task:list", "Get list with task from variable", GetTaskList)
    core.add_command("launch", "Launch task from variable", launch)
    
    core()