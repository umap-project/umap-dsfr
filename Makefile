.DEFAULT_GOAL := help

.PHONY: vendors
vendors: ## Install the DSFR source files
	npm install
	npm run vendors


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
