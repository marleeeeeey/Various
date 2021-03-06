import argparse
import os
import sys

import gpxlib
import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", type=str, default="./output/")
    parser.add_argument('gpx_files', nargs='*')
    args = parser.parse_args()

    gpx_files = []
    if not args.gpx_files:
        for line in sys.stdin:
            line = line.strip('\n')
            gpx_files.append(line)
    else:
        gpx_files = args.gpx_files
    print('file count:', len(gpx_files))

    if len(gpx_files) < 1:
        return

    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for gpx in gpx_files:
        gpxlib.split_gpx(gpx, output_dir)


main()
