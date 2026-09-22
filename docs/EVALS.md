# Skill Evals

Skills are routing and behavioral contracts, not just prompt text. High-value skills therefore carry repository-native eval fixtures.

## Layout

~~~text
.agents/skills/<skill>/
├── SKILL.md
└── evals/
    └── eval.json
~~~

The canonical ".agents/skills" tree is mirrored to ".claude/skills".

## Fixture schema

~~~json
{
  "skill": "example-skill",
  "version": 1,
  "positive_cases": [
    {
      "id": "should-trigger",
      "prompt": "A representative request.",
      "must_trigger": true
    }
  ],
  "negative_cases": [
    {
      "id": "should-not-trigger",
      "prompt": "A nearby but different request.",
      "must_trigger": false
    }
  ],
  "required_behaviors": [
    "behavior the skill must cause"
  ],
  "forbidden_behaviors": [
    "behavior the skill must prevent"
  ]
}
~~~

## What these evals prove

The committed fixtures are deterministic specifications for model/assistant evals. The repository validator checks their structure and parity. A future eval runner may execute prompts against supported assistants, but structural validation does not pretend to measure model quality by itself.

Static validation proves the contract is well formed. Model execution tests whether an assistant actually follows the contract.

## Principles

A good eval contains:
- at least one obvious positive trigger;
- at least one close negative trigger;
- behaviors observable in output or tool usage;
- prohibited shortcuts/failure modes;
- stable IDs for regression tracking.

Do not write evals whose only assertion is "the answer looks good."
