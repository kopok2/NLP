# coding=utf-8
"""Convert movie lines file."""

if __name__ == '__main__':
    with open('out.txt', 'w') as outfile:
        for line in open('movie_lines.txt'):
            outfile.write(line.split("+++$+++ ")[-1])
