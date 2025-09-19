class Spreadsheet:
    def __init__(self, rows: int):
        self.spreadsheet = [[0]*26 for _ in range(rows+1)]

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[int(cell[1:])][ord(cell[0]) - ord('A')] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        num1, num2 = formula[1:].split("+")
        if num1.isdigit():
            num1 = int(num1)
        else:
            num1 = self.spreadsheet[int(num1[1:])][ord(num1[0]) - ord('A')]

        if num2.isdigit():
            num2 = int(num2)
        else:
            num2 = self.spreadsheet[int(num2[1:])][ord(num2[0]) - ord('A')]
        return num1 + num2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)