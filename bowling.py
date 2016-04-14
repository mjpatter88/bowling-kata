
def score(frames):
    score = 0
    for index, frame in enumerate(frames[:10]):
        score += sum(frame)
        if is_spare(frame):
            score += frames[index + 1][0]
        if is_strike(frame):
            next_frame = frames[index + 1]
            if index == 9:
                score += sum(next_frame)
            else:
                if is_strike(next_frame):
                    score = score + next_frame[0] + frames[index + 2][0]
                else:
                    score += sum(next_frame)
    return score

def is_spare(frame):
    return sum(frame) == 10 and not is_strike(frame)

def is_strike(frame):
    return frame[0] == 10

