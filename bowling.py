
def score(frames):
    score = 0
    double_next_throw = False
    for frame in frames:
        if double_next_throw:
            score += frame[0]
            double_next_throw = False
        if sum(frame) == 10:
            double_next_throw = True
        score += sum(frame)
    return score
