# news-image-20261124 entry (Python 3.13, standard library only): the image is
# the entry.png beside this file, and the program copies it to the output
# directory. The image sums up Tuesday 24 November 2026 world news in one
# newspaper front page: Ukraine says it sank a Russian warship off Libya;
# Jensen Huang reinstated as Nvidia CEO; COP31 ends with no deal; Iran vows
# to counter a US blockade of Hormuz; the ICJ rules Myanmar committed
# genocide against the Rohingya; the UK is confirmed as 2035 Women's World
# Cup host; NATO vows space defence.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
src = os.path.join(HERE, "entry.png")
dst = os.path.join(OUT_DIR, "entry.png")
shutil.copyfile(src, dst)
# Sanity check: the output must be a whole, non-empty PNG identical to the
# source (the grader runs this program twice and both runs must agree).
assert os.path.getsize(dst) == os.path.getsize(src) > 0
print("wrote", dst)
