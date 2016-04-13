
def score(balls):
    score = sum((sum(ball) for ball in balls))
    return score
