
install:
	@pip install -e . --config-settings editable_mode=compat


run_api:
	@uvicorn doc_gpt.api.fast:app --reload



pylint:
	@find . -iname "*.py" -not -path "./tests/*" | xargs -n1 -I {}  pylint --output-format=colorized {}; true

pytest:
	@PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes


default: pylint pytest
