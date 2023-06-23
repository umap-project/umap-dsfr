.DEFAULT_GOAL := help

.PHONY: install
install: ## Install the dependencies
	python3 -m pip install --upgrade pip
	python3 -m pip install -e .

.PHONY: jsinstall
jsinstall: ## Install the JS dependencies
	npm install
	npm run vendors

.PHONY: develop
develop: ## Install the test and dev dependencies
	python3 -m pip install -e .[dev]

.PHONY: pretty-templates
pretty-templates: ## Prettify template files
	djlint umap_dsfr/templates --reformat

.PHONY: lint-templates
lint-templates: ## Lint template files
	djlint umap_dsfr/templates --lint

.PHONY: dsfr-lite
dsfr-lite: ## Copy DSFR pertinent files and purge the huge CSS
	mkdir -p umap_dsfr/static/umap/dsfr-lite
	cp -R node_modules/@gouvfr/dsfr/dist/fonts umap_dsfr/static/umap/dsfr-lite
	cp -R node_modules/@gouvfr/dsfr/dist/icons umap_dsfr/static/umap/dsfr-lite
	cp -R node_modules/@gouvfr/dsfr/dist/favicon umap_dsfr/static/umap/dsfr-lite
	cp -R node_modules/@gouvfr/dsfr/dist/artwork/pictograms umap_dsfr/static/umap/dsfr-lite
	./node_modules/purgecss/bin/purgecss.js --config purgecss.config.js
	# Maybe not Linux-compatible? https://stackoverflow.com/a/22122819
	sed -i '' 's/..\/..\///g' umap_dsfr/static/umap/dsfr-lite/icons.min.css
	sed -i '' 's/#E1000F/#009081/g' umap_dsfr/static/umap/dsfr-lite/pictograms/map/map.svg
	sed -i '' 's/#E1000F/#009081/g' umap_dsfr/static/umap/dsfr-lite/pictograms/map/location-france.svg
	sed -i '' 's/#E1000F/#009081/g' umap_dsfr/static/umap/dsfr-lite/pictograms/digital/avatar.svg
	# See https://github.com/GouvernementFR/dsfr/issues/617
	sed -i '' 's/  \/\*! media sm \*\///g' umap_dsfr/static/umap/dsfr-lite/dsfr.min.css
	sed -i '' 's/  \/\*! media md \*\///g' umap_dsfr/static/umap/dsfr-lite/dsfr.min.css
	sed -i '' 's/  \/\*! media lg \*\///g' umap_dsfr/static/umap/dsfr-lite/dsfr.min.css
	sed -i '' 's/  \/\*! media xl \*\///g' umap_dsfr/static/umap/dsfr-lite/dsfr.min.css
	sed -i '' 's/  \/\*! media sm \*\///g' umap_dsfr/static/umap/dsfr-lite/icons.min.css
	sed -i '' 's/  \/\*! media md \*\///g' umap_dsfr/static/umap/dsfr-lite/icons.min.css
	sed -i '' 's/  \/\*! media lg \*\///g' umap_dsfr/static/umap/dsfr-lite/icons.min.css
	sed -i '' 's/  \/\*! media xl \*\///g' umap_dsfr/static/umap/dsfr-lite/icons.min.css


.PHONY: help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

# See https://daniel.feldroy.com/posts/autodocumenting-makefiles
define PRINT_HELP_PYSCRIPT # start of Python section
import re, sys

output = []
# Loop through the lines in this file
for line in sys.stdin:
    # if the line has a command and a comment start with
    #   two pound signs, add it to the output
    match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
    if match:
        target, help = match.groups()
        output.append("\033[36m%-20s\033[0m %s" % (target, help))
# Sort the output in alphanumeric order
output.sort()
# Print the help result
print('\n'.join(output))
endef
export PRINT_HELP_PYSCRIPT # End of python section
