
install:
	@pip install -e . --config-settings editable_mode=compat


run_api:
	uvicorn doc_gpt.api.fast:app --reload
