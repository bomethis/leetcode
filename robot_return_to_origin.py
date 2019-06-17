class Solution:
    def judgeCircle(moves):
        horiz = 0
        virt = 0

        # Assign horizontal and virtical location value
        for i in range(len(moves)):
            if 'L' in moves[i]:
                horiz -= 1
            if 'R' in moves[i]:
                horiz += 1
            if 'U' in moves[i]:
                virt -= 1
            if 'D' in moves[i]:
                virt += 1

        # if both virtical and horizontal locations are 0, return True
        if horiz == 0 and virt == 0:
            return True

        else:
            return False


moves = "LRUDRL"
print(Solution.judgeCircle(moves))
