
def score(frames):
    score = sum((sum(frame) for frame in frames))
    return score
