"""Copy a file from a folder

Synopsis: <trigger> [duration [break duration [long break duration [count]]]]"""

import albert
import json
import os

__title__ = "Sticker Searcher"
__version__ = "0.1.1"
__triggers__ = "ss "
__authors__ = "Edwin Kofler"


def getCfg() -> str:
    file = os.path.join("albert-sticker-searcher", "config.json")
    if os.getenv("XDG_CONFIG_HOME"):
        return os.path.join(os.getenv("XDG_CONFIG_HOME"), file)
    return os.path.join(os.getenv("HOME"), ".config", file)

def readCfg() -> object:
    with open(getCfg()) as f:
        return json.load(f)

def doCopy(file: str) -> None:
    os.system('xclip -selection clipboard -t image/png -i {}'.format(file))

cfg = readCfg()
stickersDir = os.path.expandvars(os.path.expanduser(cfg.stickerDir))
def handleQuery(query) -> object:
    if not query.isTriggered:
        return

    results = []

    for stickerDir in os.listdir(stickersDir):
        albert.info(os.path.join(stickersDir, stickerDir))
        if not os.path.isdir(os.path.join(stickersDir, stickerDir)):
            continue

        for img in os.listdir(os.path.join(stickersDir, stickerDir)):
            def fn():
                icon=os.path.join(stickersDir, stickerDir, img)
                albert.info(icon)
                item = albert.Item(
                    id=__title__,
                    text=stickerDir + ': ' + img,
                    subtext=stickerDir,
                    icon=icon,
                    actions=[
                        albert.FuncAction(text="Copy Image", callable=lambda: doCopy(icon))
                    ]
                )

                results.append(item)
            fn()

    return results
