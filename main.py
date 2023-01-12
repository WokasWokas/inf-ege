from kernel.kernel import Core, Color
from kernel.columner import Columner
from importlib import reload
import os

columner = Columner()

def GetVarList() -> None:
    variables = []
    for file in os.listdir(os.path.curdir):
        if file.startswith("var"):
            variables.append(file)
    print(f"{Color.FGCyan}  [~] Variables:")
    for i in range(variables.__len__()):
        print(f"  [{i}] {variables[i]}")
    print(f"  [~] End variables message{Color.Reset}")

def GetTaskList(var: int) -> None:
    variables = []
    for file in os.listdir(os.path.curdir + f"\\var-{var}"):
        if file.startswith("task"):
            variables.append(file)
    print(f"{Color.FGCyan}  [~] Tasks from var-{var}:")
    for i in range(variables.__len__()):
        print(f"  [{i}] {variables[i]}")
    print(f"  [~] End tasks message{Color.Reset}")

def launch(var: int, task: int) -> None:
    module = __import__(f"var{var}.task{task}", fromlist=[f"var{var}"])
    reload(module)

if __name__ == "__main__":
    core = Core()
    
    core.add_command("var:list", "Get list with variables", GetVarList)
    core.add_command("task:list", "Get list with task from variable", GetTaskList)
    core.add_command("task:launch", "Launch task", launch)
    
    core()