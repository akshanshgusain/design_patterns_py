from structural.adapter.RoundHole import RoundHole
from structural.adapter.RoundPeg import RoundPeg
from structural.adapter.SquarePeg import SquarePeg
from structural.adapter.squarepegadapter import SquarePegAdapter

if __name__ == "__main__":
    # Round fits round, no surprise.
    round_hole: RoundHole = RoundHole(9)
    round_peg: RoundPeg = RoundPeg(9)
    if round_hole.fits(round_peg):
        print(f"Round peg r9 fits round hole r9")

    small_square_peg: SquarePeg = SquarePeg(2)
    large_square_peg: SquarePeg = SquarePeg(20)

    # round_hole.fits(small_square_peg)
    # Expected type 'RoundPeg', got 'SquarePeg' instead
    # Adapter Solves this problem =>
    small_square_peg_adapter: SquarePegAdapter = SquarePegAdapter(small_square_peg)
    large_square_peg_adapter: SquarePegAdapter = SquarePegAdapter(large_square_peg)

    if round_hole.fits(small_square_peg_adapter):
        print("Square peg w2 fits round hole r5")
    if not round_hole.fits(large_square_peg_adapter):
        print("Square peg w20 does not fit into round hole r5.")