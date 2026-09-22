.PHONY: validate sync-skills validate-evals asset-index

sync-skills:
	python3 scripts/sync_skills.py

validate-evals:
	python3 scripts/validate_evals.py

validate: sync-skills
	python3 scripts/validate_repo.py
	python3 scripts/validate_evals.py

asset-index:
	python3 scripts/build_asset_index.py --output .agents/asset-index.json
