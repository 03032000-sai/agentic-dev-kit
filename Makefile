.PHONY: validate sync-skills

sync-skills:
	python3 scripts/sync_skills.py

validate: sync-skills
	python3 scripts/validate_repo.py
