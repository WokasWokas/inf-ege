class Columner:
    def __init__(self) -> None:
        pass
    
    def __call__(self, headers: list[str], data: list[list[str | int]]) -> str:
        columns = {}
        for header in headers:
            columns[header] = self.__get_row__(data, headers.index(header))
        lengths = [self.__getmaxlen__(header, columns[header]) for header in headers]
        
        result = "\n  "
        for i in range(headers.__len__()):
            result += f"{headers[i].upper()}{' ' * (lengths[i] - headers[i].__len__())}  "
        result += '\n\n  '
        
        for elem in data:
            for i in range(headers.__len__()):
                result += f"{elem[i]}{' ' * (lengths[i] - str(elem[i]).__len__())}  "
            result += '\n  '
        return result
            
    def __get_row__(self, data: list[any], krow: int) -> list[any]:
        return [elem[krow] for elem in data]
    
    def __getmaxlen__(self, header: str, data: list[str | int]) -> int:
        return max(header.__len__(), max([str(elem).__len__() for elem in data]))