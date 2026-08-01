class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        

        def playerScore(turn, player1, player2, left, right, nums):

            if left > right:

                if player1 >= player2:
                    return 1
                else:
                    return -1
            
            output = 0
            if turn:
                next_turn = not turn
                output = max(playerScore(next_turn, player1+nums[left], player2, left+1, right, nums), playerScore(next_turn, player1+nums[right], player2, left, right-1, nums))


            else:
                next_turn = not turn
                output = min(playerScore(next_turn, player1, player2+nums[left], left+1, right, nums),playerScore(next_turn, player1, player2+nums[right], left, right-1, nums))

            return output

        ans = playerScore(True, 0, 0, 0, len(nums)-1, nums)
        
        return ans >= 0
