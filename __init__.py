# -*- coding: utf-8 -*-

"""Copy a file from a folder

Synopsis: <trigger> [duration [break duration [long break duration [count]]]]"""

import albert
import os

__title__ = "Sticker Copier"
__version__ = "0.1.0"
__triggers__ = "st "
__authors__ = "Edwin Kofler"

stickersDir = os.path.join(os.environ['HOME'], 'Pics/telegram-stickers')

def doCopy(file: str):
    os.system('xclip -selection clipboard -t image/png -i {}'.format(file))

def handleQuery(query):
    if not query.isTriggered:
        return

    results = []

    for stickerDir in os.listdir(stickersDir):
        albert.info(os.path.join(stickersDir, stickerDir))
        if not os.path.isdir(os.path.join(stickersDir, stickerDir)):
            continue

        for img in os.listdir(os.path.join(stickersDir, stickerDir)):
            def d():
                icon=os.path.join(stickersDir, stickerDir, img)
                albert.info(icon)
                item = albert.Item(
                    id=__title__,6A4F-868A
                    text=stickerDir + ': ' + img,
                    subtext=stickerDir,
                    icon=icon,
                    actions=[
                        albert.FuncAction(text="Copy Image", callable=lambda: doCopy(icon))
                    ]
                )

                results.append(item)
            d()

    return results
