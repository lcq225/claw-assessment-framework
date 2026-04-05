#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ClawAF Auto-Assessment Script
Automatically evaluates Claw-based AI Agent systems

Features:
- Auto-detect Claw directory
- Evaluate 8 dimensions based on actual files and configurations
- Objective scoring instead of manual input
- Multiple output formats (JSON, Markdown, HTML)
- English and Chinese versions
"""
import json
import argparse
from pathlib import Path
import subprocess
import re
from typing import Dict, List, Tuple, Optional
from datetime import datetime

# Claw directory detection
CLAW_DIRECTORIES = [
    "openclaw",
    "copaw",
    "qclaw",
    "winclaw",
    "zeroclaw",
    "workspace",
    "workspaces",
    ".copaw",
]

# Key files and directories to detect
KEY_FILES = {
    "identity": [
        "AGENTS.md",
        "SOUL.md",
        "PROFILE.md",
    ],
    "memory": [
        "memory.db",
        ".agent-memory/memory.db",
        "memory/memory.db",
    ],
    "security": [
        "sanitize_check.py",
        "pre-commit",
        ".copaw/hooks/pre-commit",
    ],
    "automation": [
        "pre_operation_check.py",
        "auto_trigger.py",
    ],
    "skills": [
        "skills/",
        "active_skills/",
    ],
}

class ClawAFEvaluator:
    """Automatic ClawAF Evaluator"""

    def __init__(self, claw_dir: str = None):
        """Initialize evaluator"""
        if claw_dir:
            self.claw_dir = Path(claw_dir)
        else:
            self.claw_dir = self._find_claw_directory()

        if not self.claw_dir or not self.claw_dir.exists():
            raise Exception("Claw directory not found")

        print(f"Claw directory: {self.claw_dir}")

    def _find_claw_directory(self) -> Path:
        """Find Claw directory"""
        # Check current directory
        current = Path.cwd()

        # Check if current directory contains Claw indicators
        if self._is_claw_directory(current):
            return current

        # Check parent directories
        for parent in [current] + list(current.parents):
            if self._is_claw_directory(parent):
                return parent

        # Check common Claw directory names
        for name in CLAW_DIRECTORIES:
            path = current / name
            if path.exists() and self._is_claw_directory(path):
                return path

        return None

    def _is_claw_directory(self, path: Path) -> bool:
        """Check if directory is a Claw directory"""
        # Check for key indicators
        if (path / "AGENTS.md").exists():
            return True
        if (path / "skills").exists():
            return True
        if (path / ".copaw").exists():
            return True
        return False

    def evaluate_identity_cognition(self) -> int:
        """Evaluate Identity Cognition (0-100)"""
        score = 0

        # Check AGENTS.md - search recursively
        agents_files = list(self.claw_dir.rglob("AGENTS.md"))
        if agents_files:
            # Pick the most relevant one (prefer workspaces/default)
            agents_file = self._find_most_relevant_file(agents_files, ["workspaces", "default"])
            if agents_file and agents_file.exists():
                content = agents_file.read_text(encoding='utf-8', errors='ignore')
                if len(content) > 1000:
                    score += 30
                if "role" in content.lower():
                    score += 10
                if "rules" in content.lower() or "red line" in content.lower():
                    score += 10

        # Check SOUL.md - search recursively
        soul_files = list(self.claw_dir.rglob("SOUL.md"))
        if soul_files:
            soul_file = self._find_most_relevant_file(soul_files, ["workspaces", "default"])
            if soul_file and soul_file.exists():
                content = soul_file.read_text(encoding='utf-8', errors='ignore')
                if len(content) > 500:
                    score += 25
                if "personality" in content.lower() or "style" in content.lower():
                    score += 10

        # Check PROFILE.md - search recursively
        profile_files = list(self.claw_dir.rglob("PROFILE.md"))
        if profile_files:
            profile_file = self._find_most_relevant_file(profile_files, ["workspaces", "default"])
            if profile_file and profile_file.exists():
                content = profile_file.read_text(encoding='utf-8', errors='ignore')
                if len(content) > 200:
                    score += 15

        return min(score, 100)

    def _find_most_relevant_file(self, files: List[Path], preferred_keywords: List[str]) -> Path:
        """Find the most relevant file from a list of files"""
        # Prefer files that contain preferred keywords in their path
        for file in files:
            path_str = str(file).lower()
            for keyword in preferred_keywords:
                if keyword.lower() in path_str:
                    return file

        # Return the first file if no preferred match
        return files[0] if files else None

    def evaluate_memory_capability(self) -> int:
        """Evaluate Memory Capability (0-100)"""
        score = 0

        # Find memory database
        memory_files = list(self.claw_dir.rglob("memory.db"))
        if memory_files:
            score += 30

            # Check memory size
            for mem_file in memory_files:
                if mem_file.stat().st_size > 10240:  # > 10KB
                    score += 20

        # Check for vector search (semantic retrieval)
        py_files = list(self.claw_dir.rglob("*.py"))
        for py_file in py_files:
            content = py_file.read_text(encoding='utf-8', errors='ignore')
            if "vector" in content.lower() or "embedding" in content.lower():
                score += 20
                break

        # Check for memory-related skills
        skill_dirs = [
            self.claw_dir / "skills",
            self.claw_dir / "active_skills",
        ]
        for skill_dir in skill_dirs:
            if skill_dir.exists():
                if (skill_dir / "memorycoreclaw").exists():
                    score += 30
                    break

        return min(score, 100)

    def evaluate_security_mechanism(self) -> int:
        """Evaluate Security Mechanism (0-100)"""
        score = 0

        # Check for sanitize_check.py
        sanitize_files = list(self.claw_dir.rglob("sanitize_check.py"))
        if sanitize_files:
            score += 30

        # Check for pre-commit hooks
        precommit_files = list(self.claw_dir.rglob("pre-commit"))
        if precommit_files:
            for file in precommit_files:
                content = file.read_text(encoding='utf-8', errors='ignore')
                if "sanitize" in content.lower():
                    score += 30
                    break

        # Check for permission checks
        permission_files = list(self.claw_dir.rglob("permission_check.py"))
        if permission_files:
            score += 20

        # Check for credential validation
        credential_files = list(self.claw_dir.rglob("credential_validator.py"))
        if credential_files:
            score += 20

        return min(score, 100)

    def evaluate_automation_level(self) -> int:
        """Evaluate Automation Level (0-100)"""
        score = 0

        # Check for auto-trigger scripts
        auto_files = list(self.claw_dir.rglob("auto_trigger.py"))
        if auto_files:
            score += 30

        # Check for pre-operation checks
        preop_files = list(self.claw_dir.rglob("pre_operation_check.py"))
        if preop_files:
            score += 30

        # Check for cron/scheduled tasks
        cron_files = list(self.claw_dir.rglob("cron"))
        if cron_files:
            score += 20

        # Check for automation-related skills
        skill_dirs = [
            self.claw_dir / "skills",
            self.claw_dir / "active_skills",
        ]
        for skill_dir in skill_dirs:
            if skill_dir.exists():
                # Count automation-related skills
                automation_count = 0
                for skill in skill_dir.iterdir():
                    if skill.is_dir():
                        skill_file = skill / "SKILL.md"
                        if skill_file.exists():
                            content = skill_file.read_text(encoding='utf-8', errors='ignore')
                            if "auto" in content.lower() or "trigger" in content.lower():
                                automation_count += 1
                if automation_count >= 3:
                    score += 20
                    break

        return min(score, 100)

    def evaluate_skill_ecosystem(self) -> int:
        """Evaluate Skill Ecosystem (0-100)"""
        score = 0

        # Find skill directories recursively
        skill_dirs = list(self.claw_dir.rglob("skills")) + list(self.claw_dir.rglob("active_skills"))

        total_skills = 0
        documented_skills = 0

        for skill_dir in skill_dirs:
            if skill_dir.is_dir():
                for skill in skill_dir.iterdir():
                    if skill.is_dir() and not skill.name.startswith('.'):
                        total_skills += 1

                        # Check for SKILL.md
                        skill_file = skill / "SKILL.md"
                        if skill_file.exists():
                            documented_skills += 1

        # Score based on skill count
        if total_skills >= 10:
            score += 30
        elif total_skills >= 5:
            score += 20
        elif total_skills >= 1:
            score += 10

        # Score based on documentation
        if total_skills > 0:
            doc_ratio = documented_skills / total_skills
            if doc_ratio >= 0.8:
                score += 40
            elif doc_ratio >= 0.5:
                score += 30
            elif doc_ratio >= 0.3:
                score += 20

        # Check for skill classification
        if total_skills >= 5:
            score += 30

        return min(score, 100)

    def evaluate_collaboration_rapport(self) -> int:
        """Evaluate Collaboration Rapport (0-100)"""
        score = 0

        # Check PROFILE.md for user information - search recursively
        profile_files = list(self.claw_dir.rglob("PROFILE.md"))
        if profile_files:
            profile_file = self._find_most_relevant_file(profile_files, ["workspaces", "default"])
            if profile_file and profile_file.exists():
                content = profile_file.read_text(encoding='utf-8', errors='ignore')
                if "user" in content.lower() or "profile" in content.lower():
                    score += 30
                if "preference" in content.lower() or "style" in content.lower():
                    score += 20

        # Check SOUL.md for collaboration guidelines - search recursively
        soul_files = list(self.claw_dir.rglob("SOUL.md"))
        if soul_files:
            soul_file = self._find_most_relevant_file(soul_files, ["workspaces", "default"])
            if soul_file and soul_file.exists():
                content = soul_file.read_text(encoding='utf-8', errors='ignore')
                if "collaborate" in content.lower() or "partner" in content.lower():
                    score += 30

        # Check AGENTS.md for communication style - search recursively
        agents_files = list(self.claw_dir.rglob("AGENTS.md"))
        if agents_files:
            agents_file = self._find_most_relevant_file(agents_files, ["workspaces", "default"])
            if agents_file and agents_file.exists():
                content = agents_file.read_text(encoding='utf-8', errors='ignore')
                if "bluf" in content.lower() or "communication" in content.lower():
                    score += 20

        return min(score, 100)

    def evaluate_experience_accumulation(self) -> int:
        """Evaluate Experience Accumulation (0-100)"""
        score = 0

        # Check for experience records
        memory_files = list(self.claw_dir.rglob("memory.db"))
        if memory_files:
            # Try to query experience count
            for mem_file in memory_files:
                try:
                    import sqlite3
                    conn = sqlite3.connect(mem_file)
                    cursor = conn.cursor()

                    # Check for experiences table
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='experiences'")
                    if cursor.fetchone():
                        cursor.execute("SELECT COUNT(*) FROM experiences")
                        count = cursor.fetchone()[0]
                        if count >= 50:
                            score += 40
                        elif count >= 20:
                            score += 30
                        elif count >= 10:
                            score += 20
                        elif count >= 5:
                            score += 10

                    conn.close()
                except:
                    pass

        # Check for memory documentation
        memory_docs = list(self.claw_dir.rglob("memory.md"))
        if memory_docs:
            score += 20

        # Check for lesson learned records
        lesson_files = list(self.claw_dir.rglob("*lesson*.md"))
        if lesson_files:
            score += 20

        # Check for experience retrieval
        py_files = list(self.claw_dir.rglob("*.py"))
        for py_file in py_files:
            content = py_file.read_text(encoding='utf-8', errors='ignore')
            if "recall" in content.lower() and "experience" in content.lower():
                score += 20
                break

        return min(score, 100)

    def evaluate_evolution_capability(self) -> int:
        """Evaluate Evolution Capability (0-100)"""
        score = 0

        # Check for self-evolution engine
        evo_files = list(self.claw_dir.rglob("self_evolution"))
        if evo_files:
            score += 30

        # Check for evolution-related scripts
        evo_scripts = [
            "self_review.py",
            "learn.py",
            "improve.py",
        ]
        for script in evo_scripts:
            files = list(self.claw_dir.rglob(script))
            if files:
                score += 10

        # Check for experience learning
        py_files = list(self.claw_dir.rglob("*.py"))
        for py_file in py_files:
            content = py_file.read_text(encoding='utf-8', errors='ignore')
            if "learn" in content.lower() and "experience" in content.lower():
                score += 20
                break

        # Check for closed-loop evolution
        for py_file in py_files:
            content = py_file.read_text(encoding='utf-8', errors='ignore')
            if "evolution" in content.lower() and "loop" in content.lower():
                score += 20
                break

        return min(score, 100)

    def get_level(self, score: int) -> str:
        """Get level based on score"""
        if score >= 600:
            return "Legendary"
        elif score >= 520:
            return "Diamond"
        elif score >= 400:
            return "Platinum"
        elif score >= 280:
            return "Gold"
        elif score >= 160:
            return "Silver"
        else:
            return "Bronze"

    def evaluate(self) -> Dict:
        """Run full evaluation"""
        print("\n" + "=" * 70)
        print("ClawAF - Automatic Evaluation")
        print("=" * 70)
        print()

        dimensions = {
            "Identity Cognition": self.evaluate_identity_cognition(),
            "Memory Capability": self.evaluate_memory_capability(),
            "Security Mechanism": self.evaluate_security_mechanism(),
            "Automation Level": self.evaluate_automation_level(),
            "Skill Ecosystem": self.evaluate_skill_ecosystem(),
            "Collaboration Rapport": self.evaluate_collaboration_rapport(),
            "Experience Accumulation": self.evaluate_experience_accumulation(),
            "Evolution Capability": self.evaluate_evolution_capability(),
        }

        # Print results
        for dim, score in dimensions.items():
            print(f"{dim:.<50} {score}/100")

        total_score = sum(dimensions.values())
        level = self.get_level(total_score)

        print()
        print("=" * 70)
        print(f"Total Score: {total_score}/800")
        print(f"Level: {level}")
        print("=" * 70)

        # Prepare result
        result = {
            "claw_directory": str(self.claw_dir),
            "date": "2026-04-05",
            "total_score": total_score,
            "level": level,
            "dimensions": dimensions,
            "details": {
                "Identity Cognition": self._get_identity_details(),
                "Memory Capability": self._get_memory_details(),
                "Security Mechanism": self._get_security_details(),
                "Automation Level": self._get_automation_details(),
                "Skill Ecosystem": self._get_skill_details(),
                "Collaboration Rapport": self._get_collaboration_details(),
                "Experience Accumulation": self._get_experience_details(),
                "Evolution Capability": self._get_evolution_details(),
            }
        }

        return result

    def _get_identity_details(self) -> Dict:
        """Get identity details"""
        details = {}

        # Search recursively
        agents_files = list(self.claw_dir.rglob("AGENTS.md"))
        if agents_files:
            details["AGENTS.md"] = f"{len(agents_files)} found"
        else:
            details["AGENTS.md"] = "Not Found"

        soul_files = list(self.claw_dir.rglob("SOUL.md"))
        if soul_files:
            details["SOUL.md"] = f"{len(soul_files)} found"
        else:
            details["SOUL.md"] = "Not Found"

        profile_files = list(self.claw_dir.rglob("PROFILE.md"))
        if profile_files:
            details["PROFILE.md"] = f"{len(profile_files)} found"
        else:
            details["PROFILE.md"] = "Not Found"

        return details

    def _get_memory_details(self) -> Dict:
        """Get memory details"""
        details = {}
        memory_files = list(self.claw_dir.rglob("memory.db"))
        details["Memory Database"] = f"{len(memory_files)} found" if memory_files else "Not Found"

        # Get record count
        if memory_files:
            try:
                import sqlite3
                conn = sqlite3.connect(memory_files[0])
                cursor = conn.cursor()

                # Check tables
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                tables = [row[0] for row in cursor.fetchall()]
                details["Tables"] = ", ".join(tables)

                # Get record counts
                counts = {}
                for table in tables:
                    try:
                        cursor.execute(f"SELECT COUNT(*) FROM {table}")
                        counts[table] = cursor.fetchone()[0]
                    except:
                        pass
                details["Record Counts"] = counts

                conn.close()
            except Exception as e:
                details["Error"] = str(e)

        return details

    def _get_security_details(self) -> Dict:
        """Get security details"""
        details = {}
        sanitize_files = list(self.claw_dir.rglob("sanitize_check.py"))
        details["Sanitize Check"] = f"{len(sanitize_files)} found" if sanitize_files else "Not Found"

        precommit_files = list(self.claw_dir.rglob("pre-commit"))
        details["Pre-commit Hooks"] = f"{len(precommit_files)} found" if precommit_files else "Not Found"

        permission_files = list(self.claw_dir.rglob("permission_check.py"))
        details["Permission Check"] = f"{len(permission_files)} found" if permission_files else "Not Found"

        return details

    def _get_automation_details(self) -> Dict:
        """Get automation details"""
        details = {}
        auto_files = list(self.claw_dir.rglob("auto_trigger.py"))
        details["Auto Trigger"] = f"{len(auto_files)} found" if auto_files else "Not Found"

        preop_files = list(self.claw_dir.rglob("pre_operation_check.py"))
        details["Pre-operation Check"] = f"{len(preop_files)} found" if preop_files else "Not Found"

        return details

    def _get_skill_details(self) -> Dict:
        """Get skill details"""
        details = {}

        # Find skill directories recursively
        skill_dirs = list(self.claw_dir.rglob("skills")) + list(self.claw_dir.rglob("active_skills"))

        total_skills = 0
        documented_skills = 0

        for skill_dir in skill_dirs:
            if skill_dir.is_dir():
                for skill in skill_dir.iterdir():
                    if skill.is_dir() and not skill.name.startswith('.'):
                        total_skills += 1

                        skill_file = skill / "SKILL.md"
                        if skill_file.exists():
                            documented_skills += 1

        details["Total Skills"] = total_skills
        details["Documented Skills"] = documented_skills
        details["Documentation Rate"] = f"{(documented_skills/total_skills*100):.1f}%" if total_skills > 0 else "N/A"
        details["Skill Directories Found"] = len(skill_dirs)

        return details

    def _get_collaboration_details(self) -> Dict:
        """Get collaboration details"""
        details = {}

        # Search recursively
        profile_files = list(self.claw_dir.rglob("PROFILE.md"))
        if profile_files:
            details["PROFILE.md"] = f"{len(profile_files)} found"
        else:
            details["PROFILE.md"] = "Not Found"

        soul_files = list(self.claw_dir.rglob("SOUL.md"))
        if soul_files:
            details["SOUL.md"] = f"{len(soul_files)} found"
        else:
            details["SOUL.md"] = "Not Found"

        return details

    def _get_experience_details(self) -> Dict:
        """Get experience details"""
        details = {}

        # Get experience count from memory.db
        memory_files = list(self.claw_dir.rglob("memory.db"))
        if memory_files:
            try:
                import sqlite3
                conn = sqlite3.connect(memory_files[0])
                cursor = conn.cursor()

                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='experiences'")
                if cursor.fetchone():
                    cursor.execute("SELECT COUNT(*) FROM experiences")
                    details["Experience Count"] = cursor.fetchone()[0]

                    cursor.execute("SELECT COUNT(*) FROM facts")
                    details["Fact Count"] = cursor.fetchone()[0]

                conn.close()
            except Exception as e:
                details["Error"] = str(e)

        return details

    def _get_evolution_details(self) -> Dict:
        """Get evolution details"""
        details = {}
        evo_files = list(self.claw_dir.rglob("self_evolution"))
        details["Self Evolution"] = f"{len(evo_files)} found" if evo_files else "Not Found"

        return details

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='ClawAF Automatic Evaluation',
        epilog="""
Examples:

  # Auto-detect Claw workspace directory
  python assess_auto.py

  # Specify workspace directory (CoPaw example)
  python assess_auto.py --dir "D:\\CoPaw\\.copaw\\workspaces\\default"

  # Specify workspace directory (OpenClaw example)
  python assess_auto.py --dir "/path/to/openclaw/.copaw/workspaces/default"

  # Specify workspace directory (Linux/Mac)
  python assess_auto.py --dir "~/copaw/.copaw/workspaces/default"

Note:
  - The --dir parameter should point to the WORKSPACE directory
  - Workspace directory contains: AGENTS.md, SOUL.md, PROFILE.md, skills/
  - If not specified, auto-detection will search in current and parent directories

Claw Directory Structure:
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
        """
    )
    parser.add_argument('--dir', '--workspace',
                       type=str,
                       help='Claw workspace directory (contains AGENTS.md/SOUL.md/PROFILE.md/skills/). Auto-detect if not specified.')
    parser.add_argument('--output', type=str, default='clawaf_result.json', help='Output JSON file')

    args = parser.parse_args()

    try:
        evaluator = ClawAFEvaluator(args.dir)
        result = evaluator.evaluate()

        # Save result
        output_file = Path(args.output)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"\nResults saved to: {output_file}")
        print(f"\nTo convert to other formats:")
        print(f"  python format_result.py {output_file}")
        print(f"  python format_result_cn.py {output_file}")

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()