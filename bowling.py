
def score(frames):
    score = 0
    next_throws_to_double = 0
    for frame in frames:
        if next_throws_to_double:
            score += sum(frame[:next_throws_to_double])
            next_throws_to_double -= throws_in_frame(frame)
        if is_strike(frame):
            next_throws_to_double += 2
        elif is_spare(frame):
            next_throws_to_double += 1
        score += sum(frame)
    return score

def is_spare(frame):
    return sum(frame) == 10

def is_strike(frame):
    return frame[0] == 10

def throws_in_frame(frame):
    return 1 if is_strike(frame) else 2
