class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen_col = [0] * 9
        # for line in board:
        for row_cell in board:
            get_only_num = [num for num in row_cell if num != "."]
            if len(get_only_num) >len(set(get_only_num)): # check rows
                return False
        for i in range(0,len(row_cell)):
            get_only_colm = [board[j][i] for j in range (0, len(row_cell))]
            get_only_num = [num for num in get_only_colm if num != "."]
            if len(get_only_num) >len(set(get_only_num)): # check columns
                return False
        mat = []
    
        
        # ✅ Check all 9 boxes (3×3)
        for box_row in range(3):        # 0, 1, 2 → top, middle, bottom
            for box_col in range(3):    # 0, 1, 2 → left, center, right
                nums = []
                for i in range(3):      # rows within box
                    for j in range(3):  # cols within box
                        val = board[box_row*3 + i][box_col*3 + j]
                        if val != ".":
                            nums.append(val)
                if len(nums) > len(set(nums)):
                    return False
        
        return True


    


            
                                



        