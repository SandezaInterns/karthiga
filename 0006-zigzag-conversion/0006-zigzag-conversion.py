class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        # Create empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Place each character in the correct row
        for char in s:
            rows[current_row] += char

            # Reverse direction if at top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move up or down
            current_row += 1 if going_down else -1

        # Join all rows into one string
        return ''.join(rows)