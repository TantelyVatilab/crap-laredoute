
fix-dpkg:
	@echo "Correction des paquets dpkg interrompus..."
	sudo dpkg --configure -a
	@echo "Correction terminée. Vous pouvez continuer l'installation."


install-curl: fix-dpkg
	@command -v curl >/dev/null 2>&1 || (sudo apt update && sudo apt install -y curl)

install-pixi: install-curl
	curl -fsSL https://pixi.sh/install.sh | sh
	~/.pixi/bin/pixi upgrade

install-deps:
	~/.pixi/bin/pixi install
	~/.pixi/bin/pixi update

run:
	~/.pixi/bin/pixi run start

livrable:
	~/.pixi/bin/pixi run livrable

setup: install-pixi install-deps

.PHONY: fix-dpkg install-curl install-pixi install-deps run livrable setup