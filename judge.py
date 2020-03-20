#!/usr/bin/env python3

from pathlib import Path
from subprocess import run
from typing import IO, Any, List, Tuple


def run_provided_file(
    filepath: Path, stdin: IO[Any]
) -> Tuple[int, List[str], List[str]]:
    """Run the user provided problem file
    
    :param filepath: The relative path to the script file
    :param stdin: The official inputs for the current problem
    :return: The return code, the stdout, and the stderr (the last two as lists of strings)
    """
    result = run(["python", str(filepath)], stdin=stdin, capture_output=True)
    return (
        result.returncode,
        result.stdout.decode("utf-8").splitlines(),
        result.stderr.decode("utf-8").splitlines(),
    )


def main(argv: List[str]):
    if len(argv) < 3 or len(argv) > 4:
        print("Missing arguments!")
        return 1

    problem_num, provided_file = sys.argv[1:3]
    verbose = False

    if len(argv) == 4 and argv[3] == "-v":
        verbose = True

    script_directory = Path(__file__).resolve().parent  # Where this script is
    io_filename = f"Prob{problem_num:0>2}.txt"  # Official input/output filenames

    # Run solution script and report errors if any
    with open(script_directory / "2019_io" / "inputs" / io_filename) as input_file:
        returncode, captured_outputs, stderr = run_provided_file(
            Path.cwd() / provided_file, input_file
        )
        if returncode != 0:
            print("Your program exited with an error! Exiting...")
            if verbose:
                print("Captured stderr:")
                print("\n".join(stderr))
            return 1

    with open(script_directory / "2019_io" / "outputs" / io_filename) as input_file:
        expected_outputs = input_file.read().splitlines()

    # Compare output lengths
    if len(expected_outputs) != len(captured_outputs):
        print(
            "The expected output and the output from your script don't match in length!"
        )
        if verbose:
            print(
                f"Expected length = {len(expected_outputs)} Captured length = {len(captured_outputs)}"
            )
        return 1

    # Compare output line by line
    failed = []
    for i, (expected, captured) in enumerate(zip(expected_outputs, captured_outputs)):
        if expected != captured:
            if verbose:
                failed.append((i + 1, expected, captured))
            else:
                print(f"FAILED! Line {i + 1} doesn't match in the output")
                return 1

    if len(failed) != 0:
        print("FAILED\n")
        print(f"Line # | Expected{' ': <41}| Captured")
        print("-" * 80)
        for i, expected, captured in failed:
            print(f"{i: <7}| {expected: <49}| {captured}")
        return 1

    print("SUCCESS")
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
