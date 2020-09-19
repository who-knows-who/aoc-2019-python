from util import print_ascii, print_answer
from intcode import Program, make_program


def part1(program):

    user_input = None
    saved_states = dict()
    items = set()

    route = ["west",
             "take cake",
             "west",
             "south",
             "take monolith",
             "north",
             "west",
             "south",
             "east",
             "east",
             "east",
             "take mug",
             "west",
             "west",
             "west",
             "north",
             "east",
             "east",
             "east",
             "south",
             "take coin",
             "south",
             "west",
             "north",
             "north",
             "north"]

    # Run until program finishes
    while not program.finished:

        # Run program with the user input
        program.run_program(user_input)
        print_ascii(program.output_buffer)

        # Loop getting input until machine command given
        run_again = False
        while not run_again:

            u_input = input().strip()

            # Commands not for machine: save and load

            # Save state with given name
            if u_input[:4] == "save":
                if not u_input[5:]:
                    print("Please specify a save name")
                saved_states[u_input[5:]] = program.copy()
                print("Saved", u_input[5:])
                continue

            # Load given state
            if u_input[:4] == "load":
                # If no/invalid state name given
                if not u_input[5:] or u_input[5:] not in saved_states:
                    # List available states
                    print("Available load commands:")
                    for save in saved_states:
                        print("load", save)
                else:
                    # Load specified state
                    program = saved_states[u_input[5:]]
                    print("Loaded", u_input[5:])
                continue

            # Enhanced commands: Drop *, run route

            # Drop all items
            if u_input == "drop *":
                for item in items:
                    program.run_program([ord(c)
                                         for c in ("drop " + item + "\n")])
                    print_ascii(program.output_buffer)
                continue

            # Run route found
            if u_input == "run route":
                for instruction in route:
                    program.run_program([ord(c)
                                         for c in (instruction + "\n")])
                    print_ascii(program.output_buffer)
                continue

            # Commands for machine

            # Auto save state on move
            if u_input in ["north", "south", "east", "west"]:
                saved_states["auto"] = program.copy()

            # Add any taken item to list - can then be dropped in "drop *"
            if u_input[:4] == "take":
                items.add(u_input[5:])

            # Convert ascii text to numbers
            user_input = [ord(c) for c in (u_input + "\n")]

            # Run intcode on next loop
            run_again = True


def part2():
    return 0


if __name__ == "__main__":

    part1_correct = None
    part2_correct = None

    program = Program("25")

    print_answer(1, part1(program), part1_correct)
    print_answer(2, part2(), part2_correct)
