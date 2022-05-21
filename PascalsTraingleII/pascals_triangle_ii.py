class Solution :
    def getRow(self, rowIndex: int) -> list[int] :
        if rowIndex == 0 :
            return [1]
        elif rowIndex == 1 :
            return [1, 1]
        else :
            row = self.getRow(rowIndex - 1)
            new_row = []
            new_row.append(1)
            for i in range(1, rowIndex) :
                new_row.append(row[i-1] + row[i])
            new_row.append(1)
            return new_row