import argparse
import numpy as np
from pathlib import Path
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from coco_combinator import COCO_Combinator

parser = argparse.ArgumentParser()
parser.add_argument('GTfile')
parser.add_argument('DTfile')
args = parser.parse_args()


GTpath = Path(args.GTfile)
DTpath = Path(args.DTfile)
# assert GTpath.is_file()
assert DTpath.is_file()
GTpath = GTpath if GTpath.is_file() else COCO_Combinator(args.GTfile, 'gtMerge.json').merge()

cocoGt=COCO(str(GTpath))
cocoDt=cocoGt.loadRes(str(DTpath))
cocoEval = COCOeval(cocoGt,cocoDt,'bbox')
cocoEval.evaluate()
# cocoEval.accumulate()
cocoEval.accumulateText()
cocoEval.summarize()
