# ClawAF - Claw Assessment Framework

> A standardized framework for evaluating the intelligence capabilities of Claw-based AI Agent systems

---

## Overview

**ClawAF (Claw Assessment Framework)** is a standardized evaluation framework designed to assess the intelligence capabilities of Claw-based AI Agent systems, including OpenClaw, CoPaw, qclaw, winClaw, zeroclaw, and other variants.

### Goal

Provide a universal standard for measuring AI Agent capabilities, enabling:
- Self-assessment
- Team benchmarking
- Evolution planning
- Industry comparison

---

## Quick Start

### Installation

```bash
git clone https://github.com/lcq225/claw-assessment-framework.git
cd claw-assessment-framework
pip install -r requirements.txt
```

### Automatic Evaluation (Recommended)

The script will automatically scan your Claw workspace directory and evaluate based on actual files and configurations:

```bash
python assess_auto.py
```

Or specify your Claw workspace directory:

```bash
# CoPaw example
python assess_auto.py --dir "D:\CoPaw\.copaw\workspaces\default"

# OpenClaw example
python assess_auto.py --dir "/path/to/openclaw/.copaw/workspaces/default"

# Linux/Mac example
python assess_auto.py --dir "~/copaw/.copaw/workspaces/default"
```

**Important:** The `--dir` parameter should point to the **workspace directory** (the folder containing `AGENTS.md`, `SOUL.md`, `PROFILE.md`, and `skills/`), not the project root directory.

**Claw Directory Structure:**

```
project-root/
├── .copaw/
│   ├── workspaces/
│   │   ├── default/           <-- EVALUATE THIS (workspace directory)
│   │   │   ├── AGENTS.md
│   │   │   ├── SOUL.md
│   │   │   ├── PROFILE.md
│   │   │   └── skills/
│   │   └── other-workspace/
│   └── skills/               <-- Global skills (optional)
└── ... (project files)
```

### Directory Diagnostic Tool

Not sure which directory to evaluate? Use the diagnostic tool:

```bash
python diagnose.py --dir "D:\CoPaw"
```

The diagnostic tool will:
1. Check if the current directory is a workspace
2. Search for all available workspace directories
3. Provide the correct evaluation command

Example output:
```
Found workspace directories:

1. D:\CoPaw\.copaw\workspaces\default
   Command: python assess_auto.py --dir "D:\CoPaw\.copaw\workspaces\default"
   Files: AGENTS.md SOUL.md PROFILE.md

Recommended: Use the first workspace directory
```

**How it works:**

1. **Auto-detection** - Automatically find your Claw directory
2. **File scanning** - Scan for key files (AGENTS.md, memory.db, skills, etc.)
3. **Database query** - Query memory database for record counts
4. **Objective scoring** - Score based on actual data, not manual input
5. **Detailed results** - Show inspection points for each dimension

Output:
```
============================================================
ClawAF - Automatic Evaluation
============================================================

Identity Cognition................................ 80/100
Memory Capability................................. 50/100
Security Mechanism................................ 70/100
Automation Level.................................. 70/100
Skill Ecosystem................................... 100/100
Collaboration Rapport............................. 0/100
Experience Accumulation........................... 40/100
Evolution Capability.............................. 70/100

============================================================
Total Score: 480/800
Level: Platinum
============================================================

Results saved to: clawaf_result.json
```

### Convert Results to Other Formats

After generating the JSON result, convert to human-readable formats:

```bash
# English versions
python format_result.py clawaf_result.json

# Chinese versions
python format_result_cn.py clawaf_result.json
```

This generates:
- `clawaf_result.json` - Machine-readable (program processing, comparison, history)
- `clawaf_result.md` - Human-readable (viewing, sharing, archiving)
- `clawaf_result.html` - Visual report (browser viewing, presentation)
- `clawaf_result_cn.*` - Chinese versions

**Format Comparison:**

| Format | Best For | Use Case |
|--------|----------|----------|
| **JSON** | Machine | Program processing, comparison, history tracking |
| **Markdown** | Human | Quick reading, documentation, version control |
| **HTML** | Visual | Presentation, sharing, printing |

### Manual Assessment

For manual evaluation, run the interactive script:

```bash
python assess.py
```

### Team Comparison

```bash
python compare.py --users user1,user2,user3
```

---

## 8 Evaluation Dimensions

### 1. Identity Cognition

Does the AI Agent have a clear, complete self-cognitive framework?

| Score | Description |
|-------|-------------|
| 0-20 | No identity cognition, basic template only |
| 21-40 | Basic identity (name, role) |
| 41-60 | Complete identity document (AGENTS.md) |
| 61-80 | Detailed identity with rules and preferences |
| 81-100 | Complete identity, continuous evolution (AGENTS.md/SOUL.md/PROFILE.md) |

**Indicators:**
- Identity document completeness
- Rule clarity
- Preference definition
- Continuous update frequency

---

### 2. Memory Capability

Does the AI Agent have persistent memory and intelligent retrieval capabilities?

| Score | Description |
|-------|-------------|
| 0-20 | No memory system, fresh conversation each time |
| 21-40 | Simple memory (manual recording) |
| 41-60 | Memory system (basic retrieval) |
| 61-80 | Intelligent memory (semantic search) |
| 81-100 | Powerful memory (layered memory + Reranker + auto-learning) |

**Indicators:**
- Memory persistence
- Retrieval accuracy
- Semantic understanding
- Auto-learning capability

---

### 3. Security Mechanism

Does the AI Agent have comprehensive security protection mechanisms?

| Score | Description |
|-------|-------------|
| 0-20 | No security mechanism |
| 21-40 | Basic permission control |
| 41-60 | Sensitive information check |
| 61-80 | Multi-layer protection (rules + triggers + hooks) |
| 81-100 | Complete protection (3-layer + auto-block + continuous audit) |

**Indicators:**
- Sensitive information protection
- Permission verification
- Sanitization mechanism
- Audit tracking

---

### 4. Automation Level

Can the AI Agent automatically handle common scenarios?

| Score | Description |
|-------|-------------|
| 0-20 | Fully manual operation |
| 21-40 | Some scripts available |
| 41-60 | Partial automation scenarios |
| 61-80 | Scenario auto-trigger mechanism |
| 81-100 | Deep automation (pre-op check + smart trigger + auto-recovery) |

**Indicators:**
- Scenario coverage
- Auto-trigger capability
- Error auto-recovery
- Workflow standardization

---

### 5. Skill Ecosystem

Does the AI Agent have a comprehensive skill system?

| Score | Description |
|-------|-------------|
| 0-20 | No skill system |
| 21-40 | Few skills available |
| 41-60 | Skill classification and documentation |
| 61-80 | Skill discovery and recommendation |
| 81-100 | Complete skill ecosystem (classification + documentation + recommendation + deduplication + audit) |

**Indicators:**
- Skill quantity
- Classification clarity
- Documentation completeness
- Extension mechanism

---

### 6. Collaboration Rapport

How well does the user collaborate with the AI Agent?

| Score | Description |
|-------|-------------|
| 0-20 | Unfamiliar, no rapport |
| 21-40 | Basic collaboration, simple communication |
| 41-60 | Some rapport, can understand intent |
| 61-80 | Good rapport, efficient communication |
| 81-100 | Excellent rapport, partnership-like collaboration |

**Indicators:**
- Communication efficiency
- Intent understanding
- Feedback loop
| Trust relationship

---

### 7. Experience Accumulation

Does the AI Agent continuously accumulate experience and lessons?

| Score | Description |
|-------|-------------|
| 0-20 | No experience accumulation |
| 21-40 | Few records |
| 41-60 | Experience documentation |
| 61-80 | Intelligent experience retrieval |
| 81-100 | Complete experience system (classification + retrieval + application + evolution) |

**Indicators:**
- Experience quantity
- Classification quality
- Retrieval efficiency
| Application effectiveness

---

### 8. Evolution Capability

Does the AI Agent have self-evolution and adaptation capabilities?

| Score | Description |
|-------|-------------|
| 0-20 | No evolution capability |
| 21-40 | Basic updates |
| 41-60 | Active improvement |
| 61-80 | Self-evolution engine |
| 81-100 | Complete evolution system (review + learning + solidification + evolution) |

**Indicators:**
- Self-review
| Experience learning
| Task solidification
| Closed-loop evolution

---

## Scoring Levels

| Level | Score Range | Definition |
|-------|------------|------------|
| **Bronze** | 0-159 | Entry level, basic usage |
| **Silver** | 160-279 | Intermediate, with workflows |
| **Gold** | 280-399 | Expert level, deep customization |
| **Platinum** | 400-519 | Top level, co-evolution |
| **Diamond** | 520-599 | Excellent level, industry benchmark |
| **Legendary** | 600-800 | Industry leader, pioneering new era |

---

## Use Cases

### Case Study: CoPaw

**Version:** 2026-04-05

| Dimension | Score | Description |
|-----------|-------|-------------|
| Identity Cognition | 90 | Complete AGENTS.md/SOUL.md/PROFILE.md |
| Memory Capability | 90 | MemoryCoreClaw v2.4.0 (plugins + Reranker + security) |
| Security Mechanism | 90 | 3-layer desensitization protection, permission verification |
| Automation Level | 80 | Pre-operation check, scenario auto-trigger |
| Skill Ecosystem | 85 | 40+ skills, clear classification, complete documentation |
| Collaboration Rapport | 90 | BLUF communication, good trust relationship |
| Experience Accumulation | 85 | 87 lessons, intelligent retrieval |
| Evolution Capability | 90 | Self-evolution engine, closed-loop evolution |
| **Total** | **700** | **Legendary Level** |

**Key Features:**
- Layered memory system with semantic search
- 3-layer security protection (rules + triggers + pre-commit hooks)
- Plugin architecture for extensibility
- Reranker service for improved search relevance
- Comprehensive skill ecosystem with documentation

---

## Background & Purpose

### Background

AI Agent systems are rapidly evolving, but there is no standardized way to evaluate their capabilities. Different implementations (OpenClaw, CoPaw, etc.) have different strengths and weaknesses, making it difficult to:

1. Compare different systems objectively
2. Measure progress over time
3. Identify areas for improvement
4. Share best practices across teams

### Purpose

ClawAF aims to:

1. **Standardize Evaluation** - Provide a universal framework for assessing AI Agent capabilities
2. **Enable Comparison** - Allow objective comparison between different systems and teams
3. **Guide Evolution** - Identify improvement areas and provide actionable recommendations
4. **Share Knowledge** - Establish a community for sharing best practices and experiences

### Principles

1. **Practicality First** - Standards derived from real-world collaboration experience
2. **Measurable** - All dimensions have clear, quantifiable metrics
3. **Extensible** - Framework can be adapted to different scenarios
4. **Community-Driven** - Open source, community contribution encouraged

---

## Evaluation Methods

### Self-Assessment

Run the assessment script and answer questions:

```bash
python assess.py
```

Output:
```
============================================================
ClawAF - Claw Assessment Framework
============================================================

[Identity Cognition]
  1. Do you have complete identity documents? (0/1/2): 2
  ...
  Score: 90/100

...

============================================================
Assessment Results
============================================================
Total Score: 700/800
Level: Legendary

Results saved to: clawaf_result.json
```

### Team Comparison

Compare multiple team members:

```bash
python compare.py --users user1,user2,user3
```

Output:
```
============================================================
ClawAF - Team Comparison
============================================================

Overall Scores:

  user2: 650/800 - Legendary
  user1: 580/800 - Diamond
  user3: 420/800 - Platinum

...

Comparison report saved to: clawaf_compare_report.json
```

---

## Result Application

### 1. Self-Improvement

Based on assessment results:

- **Below-average dimensions** → Prioritize improvement
- **Near-next-level dimensions** → Continuous optimization
- **Perfect scores** → Share experiences

### 2. Team Benchmarking

- Identify team strengths and weaknesses
- Establish internal benchmarks
- Share best practices across members

### 3. Evolution Planning

Generate improvement roadmap based on assessment gaps.

---

## Documentation

| Language | Document |
|----------|----------|
| English | [README.md](README.md) (this file) |
| Chinese | [README_zh.md](README_zh.md) |

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

---

## Project Structure

```
claw-assessment-framework/
├── README.md                    # English documentation
├── README_zh.md                 # Chinese documentation
├── CHANGELOG.md                 # Version history
├── LICENSE                      # MIT License
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── assess_auto.py               # Automatic evaluation script (recommended)
├── assess.py                    # Manual self-assessment script
├── compare.py                   # Comparison script for two results
├── diagnose.py                  # Directory diagnostic tool
├── format_result.py             # Result formatter (English)
├── format_result_cn.py          # Result formatter (Chinese)
├── cases/                       # Case studies
│   └── copaw/                   # CoPaw case study
│       └── README.md            # Detailed documentation
```

---

## Files Description

### Core Scripts

- **assess_auto.py** - Automatic evaluation script (recommended)
  - Automatically scans Claw directory
  - Detects files, directories, and database records
  - Provides objective scoring based on actual data
  - No manual input required

- **assess.py** - Manual self-assessment script
  - Interactive questionnaire
  - Suitable for teams without complete file structure

- **compare.py** - Comparison script
  - Compare two evaluation results
  - Show score changes and dimension differences
  - Detailed insight into improvements

- **format_result.py** - Result formatter (English)
  - Convert JSON to Markdown and HTML
  - Generate human-readable reports
  - Support for progress bars and visual elements

- **format_result_cn.py** - Result formatter (Chinese)
  - Convert JSON to Chinese Markdown and HTML
  - Translate dimension names and levels
  - Support for Chinese users

### Documentation

- **README.md** - English documentation
- **README_zh.md** - Chinese documentation
- **LICENSE** - MIT License
- **requirements.txt** - No external dependencies (Python stdlib only)

### Case Studies

- **cases/copaw/README.md** - Detailed CoPaw case study
  - Directory structure
  - Evaluation results breakdown
  - Strengths and areas for improvement
  - Key features and insights

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| v1.0.2 | 2026-04-06 | Add multi-format output support (JSON/MD/HTML) with English and Chinese versions |
| v1.0.1 | 2026-04-05 | Fix recursive file detection, add comparison script |
| v1.0.0 | 2026-04-05 | Initial version, 8 dimensions defined |

---

## License

MIT License

---

## Authors

- Mr Lee
- 老K (LaoK)

---

## Feedback & Contributing

- **Issues**: https://github.com/lcq225/claw-assessment-framework/issues
- **Contributions**: Pull requests welcome

---

**ClawAF - Making AI Agent Intelligence Measurable, Comparable, Evolvable**