from backend.utils.utils import *

BENCH_MAX = get_max("bench_max")
SQUAT_MAX = get_max("squat_max")
DEAD_MAX = get_max("dead_max")
PRESS_MAX = get_max("press_max")

# Describes each phase and corresponding waves percentages, sets and rep schemes. Utilized by Phase class.
SCHEMES = {
    "10s": {
        "accumulate": [(60, "5 x 10")],
        "intensify":  [(55, "x 5"), (60, "x 5"), (55, "x 3 x 10")],
        "realize":    [(50, "x 5"), (60, "x 3"), (70, "x 1"), (75, "x AMRAP")],
        "deload":     [(40, "x 5"), (50, "x 5"), (60, "x 5")],
    },
    "8s": {
        "accumulate": [(65, "5 x 8")],
        "intensify":  [(60, "x 3"), (65, "x 3"), (70, "x 3 x 8")],
        "realize":    [(50, "x 5"), (60, "x 3"), (70, "x 2"), (75, "x 1"), (80, "x AMRAP")],
        "deload":     [(40, "x 5"), (50, "x 5"), (60, "x 5")],
    },
    "5s": {
        "accumulate": [(70, "6 x 5")],
        "intensify":  [(65, "x 2"), (70, "x 2"), (75, "x 4 x 5")],
        "realize":    [(50, "x 5"), (60, "x 3"), (70, "x 2"), (75, "x 1"), (80, "x 1"), (85, "x AMRAP")],
        "deload":     [(40, "x 5"), (50, "x 5"), (60, "x 5")],
    },
    "3s": {
        "accumulate": [(75, "7 x 3")],
        "intensify":  [(70, "x 1"), (75, "x 1"), (80, "x 5 x 3")],
        "realize":    [(50, "x 5"), (60, "x 3"), (70, "x 1"), (75, "x 1"), (80, "x 1"), (85, "x 1"), (90, "x AMRAP")],
        "deload":     [(40, "x 5"), (50, "x 5"), (60, "x 5")],
    },
}

class Phase:
    def __init__(self, phase_name: str):
        self.phase_name = phase_name
        self.scheme = SCHEMES[phase_name]
        pass

    def render_phase(self, lift_max: int, wave: str):
        sel_wav = self.scheme[wave]
        lines = [wave.capitalize()]
        for pct, rep_set in sel_wav:
            w = weight_calc(lift_max, pct)
            lines.append(f'{w}lbs: {rep_set}')
        return "\n".join(lines) + "\n"

    
    def accumulate(self, lift_max: int):
        return self.render_phase(lift_max, "accumulate")

    def intensify(self, lift_max: int):
        return self.render_phase(lift_max, "intensify")

    def realize(self, lift_max: int):
        return self.render_phase(lift_max, "realize")
    
    def deload(self, lift_max: int):
        return self.render_phase(lift_max, "deload")
    
    def run_all(self, lift_max: int):
        return (f'{self.phase_name} Wave\n' 
                + self.accumulate(lift_max) + "\n"
                + self.intensify(lift_max) + "\n"
                + self.realize(lift_max) + "\n"
                + self.deload(lift_max)) + "\n"


my_maxes = [BENCH_MAX, SQUAT_MAX, PRESS_MAX, DEAD_MAX]

phase_10 = Phase("10s")

for max in my_maxes:
    print(phase_10.accumulate(max))



# ✅ We want to take working max data and calculate working weights for sets and reps for each phase of each wave.
# ✅enter working maxes for major lifts (bench, squat, deadlift, press, pullup, dips)
# ✅populate sets and reps for each wave and phase
# Get exercise to print with each phase

# # allow to update max after each phase
# # populate weekly workout schedule


  

