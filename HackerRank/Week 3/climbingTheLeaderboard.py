def climbingLeaderboard(ranked, player):
    unique_scores = sorted(set(ranked), reverse=True)
    result = []
    index = len(unique_scores) - 1  

    for score in player:
        
        while index >= 0 and score >= unique_scores[index]:
            index -= 1
        
        result.append(index + 2)
    
    return result
