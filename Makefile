
install-curl:
	@command -v curl >/dev/null 2>&1 || sudo apt update && sudo apt install -y curl

install-pixi: install-curl
	curl -fsSL https://pixi.sh/install.sh | sh
	~/.pixi/bin/pixi upgrade

install-deps:
	~/.pixi/bin/pixi install
	~/.pixi/bin/pixi update

run:
	~/.pixi/bin/pixi run python src/main.py

setup: install-pixi install-deps

.PHONY: install-curl install-pixi install-deps run setup
