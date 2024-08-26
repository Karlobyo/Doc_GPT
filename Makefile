
install:
	@pip install -e . --config-settings editable_mode=compat


run_api:
	uvicorn taxifare.api.fast:app --reload
