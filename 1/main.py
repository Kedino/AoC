

def main():
    filepath = 'input.txt'
    input_moves = get_moves(filepath)
    formatted_moves = format_moves(input_moves)

    print("Number of moves:", len(formatted_moves))

    get_result_debug(formatted_moves)

    result = get_result(formatted_moves)
    return result

def get_moves(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

def get_result(moves):
    position = 50
    matches = 0

    for move in moves:
        if not move:
            continue

        value = int(move[1:])
        delta = -value if move[0] == "L" else value

        hits, position = step_hits(position, delta, 100)
        matches += hits

    return matches

def get_result_debug(moves):
    pos_sim = 50
    pos_math = 50
    hits_sim_total = 0
    hits_math_total = 0

    for i, move in enumerate(moves, start=1):
        if not move:
            continue

        value = int(move[1:])
        delta = -value if move[0] == "L" else value

        h_sim, pos_sim = step_hits(pos_sim, delta, 100)
        h_math, pos_math = count_hits_math(pos_math, delta, 100)

        hits_sim_total += h_sim
        hits_math_total += h_math

        if h_sim != h_math or pos_sim != pos_math:
            print("First mismatch at move", i, move)
            print("  sim:  hits =", h_sim,  "pos =", pos_sim)
            print("  math: hits =", h_math, "pos =", pos_math)
            print("  totals so far: sim =", hits_sim_total, "math =", hits_math_total)
            break

    print("Final totals: sim =", hits_sim_total, "math =", hits_math_total)

def step_hits(old_pos, delta, size=100):
    hits = 0
    pos = old_pos

    step = 1 if delta > 0 else -1
    for _ in range(abs(delta)):
        pos = (pos + step) % size
        if pos == 0:
            hits += 1

    return hits, pos

def count_hits_math(old_pos, delta, size=100):
    steps = abs(delta)
    full_laps = steps // size
    partial = steps % size

    hits = full_laps

    if delta > 0:
        if old_pos + partial >= size:
            hits += 1
    elif delta < 0:
        if old_pos - partial < 0:
            hits += 1

    new_pos = (old_pos + delta) % size
    return hits, new_pos

def count_hits(old_pos, delta, size=100):
    # total movement
    steps = abs(delta)
    full_laps = steps // size
    partial = steps % size

    hits = full_laps

    if delta > 0:
        # moving right
        if old_pos + partial >= size:
            hits += 1
    elif delta < 0:
        # moving left
        if old_pos - partial < 0:
            hits += 1

    new_pos = (old_pos + delta) % size
    return hits, new_pos

def get_result_debug(moves):
    pos_sim = 50
    pos_math = 50
    hits_sim_total = 0
    hits_math_total = 0

    for i, move in enumerate(moves, start=1):
        if not move:
            continue

        value = int(move[1:])
        delta = -value if move[0] == "L" else value

        h_sim, pos_sim = step_hits(pos_sim, delta, 100)
        h_math, pos_math = count_hits_math(pos_math, delta, 100)

        hits_sim_total += h_sim
        hits_math_total += h_math

        if h_sim != h_math or pos_sim != pos_math:
            print("First mismatch at move", i, move)
            print("  sim:  hits =", h_sim,  "pos =", pos_sim)
            print("  math: hits =", h_math, "pos =", pos_math)
            print("  totals so far: sim =", hits_sim_total, "math =", hits_math_total)
            break

    print("Final totals: sim =", hits_sim_total, "math =", hits_math_total)

def format_moves(input_moves):
    return [move.strip() for move in input_moves.split('\n') if move.strip()]

def test_single_r1000():
    position = 50
    delta = 1000
    hits, new_pos = count_hits(position, delta, 100)
    print("R1000 from 50 -> hits:", hits, "new_pos:", new_pos)

def test_example():
    moves = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    position = 50
    hits_total = 0

    for move in moves:
        value = int(move[1:])
        delta = -value if move[0] == "L" else value
        hits, position = count_hits(position, delta, 100)
        hits_total += hits
        print(move, "-> hits:", hits, "new_pos:", position)

    print("Total hits for example:", hits_total)



if __name__ == "__main__":
    print("Number of times position 0 is reached:", main())