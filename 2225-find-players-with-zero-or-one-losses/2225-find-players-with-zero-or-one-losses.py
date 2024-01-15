class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = set({})
        losses = {}
        for match in matches:
            
            if match[1] not in losses:
                losses[match[1]] = 0
            
            wins.add(match[0])
            losses[match[1]] += 1
        
        win_list = []
        loss_list = []
        
        for player in wins:
            if player not in losses:
                win_list.append(player)
        
        for player, loss_count in losses.items():
            if loss_count == 1:
                loss_list.append(player)
        
        return [sorted(win_list),sorted(loss_list)]