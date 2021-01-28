# albert-sticker-copier

For easily copying stickers from a directory

## Installation

```sh
git clone https://github.com/eankeen/albert-sticker-searcher
cd albert-sticker-searcher
ln -s . "${XDG_DATA_HOME:-$HOME/.local/share}/albert/org.albert.extension.python/modules"
```

## Configuration

```json
// ${XDG_CONFIG_HOME:-$HOME/.config}/albert-sticker-searcher/config.json
// impl detail: stickersDir = os.path.expandvars(os.path.expanduser(cfg.stickerDir))
{
	"stickerDir", "~/Pics/telegram-stickers"
}
```
