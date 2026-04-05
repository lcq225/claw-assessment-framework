# Changelog

All notable changes to ClawAF (Claw Assessment Framework) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.3] - 2026-04-06

### Fixed
- Collaboration Rapport score: Added bilingual (English/Chinese) keyword detection
- Identity Cognition score: Added bilingual (English/Chinese) keyword detection
- Chinese documents now scored correctly (previously scored 0/100 for Collaboration Rapport)
- Added Chinese keywords for user, preference, collaboration, communication detection
- Added Chinese keywords for role, rules, personality detection
- **Score improvements for CoPaw:**
  - Identity Cognition: 80/100 → 100/100 (+20)
  - Collaboration Rapport: 0/100 → 100/100 (+100)
  - Total Score: 480/800 → 600/800 (+120)
  - Level: Platinum → Legendary

## [1.0.2] - 2026-04-06

### Added
- Multi-format output support (JSON, Markdown, HTML)
- English and Chinese result formatters
- Format comparison table in documentation
- Progress bar visualization in Markdown output
- HTML report with responsive design

### Fixed
- Windows encoding issues (UTF-8 output for console)
- Recursive file detection for better accuracy
- Collaboration Rapport scoring

### Changed
- Updated README with format usage instructions
- Updated README_zh with Chinese format support
- Updated CoPaw case study with new format examples

## [1.0.1] - 2026-04-05

### Added
- Comparison script (compare.py) for comparing two results
- Recursive file detection for better accuracy
- _find_most_relevant_file() for prioritizing files

### Fixed
- Identity Cognition - now searches recursively for AGENTS.md/SOUL.md/PROFILE.md
- Skill Ecosystem - now searches recursively for skills/active_skills directories
- Collaboration Rapport - now searches recursively for identity files
- Missing _get_memory_details() method

## [1.0.0] - 2026-04-05

### Added
- Initial release of ClawAF (Claw Assessment Framework)
- 8 evaluation dimensions:
  - Identity Cognition
  - Memory Capability
  - Security Mechanism
  - Automation Level
  - Skill Ecosystem
  - Collaboration Rapport
  - Experience Accumulation
  - Evolution Capability
- Automatic evaluation script (assess_auto.py)
- Manual self-assessment script (assess.py)
- Scoring levels: Bronze, Silver, Gold, Platinum, Diamond, Legendary
- English and Chinese documentation
- CoPaw case study
- MIT License