"""A script to add a study_id as the first field of a file.

Usage:
    python add_study_id.py source.csv destination.csv study_id
"""

import sys


def main():
    infile = sys.argv[1]
    outfile = sys.argv[2]
    study_id = sys.argv[3]
    with open(infile) as f_in:
        header = f_in.readline()
        if "study_id" in header:
            raise RuntimeError(f"file contains study_id")
        with open(outfile, "w") as f_out:
            f_out.write("study_id," + header)
            for line in f_in:
                f_out.write(f"{study_id},{line}")

if __name__ == '__main__':
    main()

