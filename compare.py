#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ClawAF Team Comparison Script
Compare ClawAF scores of multiple users
"""
import argparse
import json
from pathlib import Path

LEVELS = {
    "Bronze": (0, 159),
    "Silver": (160, 279),
    "Gold": (280, 399),
    "Platinum": (400, 519),
    "Diamond": (520, 599),
    "Legendary": (600, 999),
}

# Dimension questions
QUESTIONS = {
    "identity_cognition": "Identity Cognition",
    "memory_capability": "Memory Capability",
    "security_mechanism": "Security Mechanism",
    "automation_level": "Automation Level",
    "skill_ecosystem": "Skill Ecosystem",
    "collaboration_rapport": "Collaboration Rapport",
    "experience_accumulation": "Experience Accumulation",
    "evolution_capability": "Evolution Capability",
}

def get_level(score):
    """Get level based on score"""
    for level, (min_score, max_score) in LEVELS.items():
        if min_score <= score <= max_score:
            return level
    return "Bronze"

def compare_users(users):
    """Compare users"""
    print("=" * 70)
    print("ClawAF - Team Comparison")
    print("=" * 70)

    results = {}

    for user in users:
        result_file = Path(f"clawaf_result_{user}.json")
        if result_file.exists():
            with open(result_file, 'r', encoding='utf-8') as f:
                results[user] = json.load(f)
        else:
            print(f"Warning: {user} result file not found, skipping")

    if not results:
        print("Error: No assessment results found")
        return

    # Print comparison results
    print("\nOverall Score Comparison:\n")
    for user, data in sorted(results.items(), key=lambda x: x[1]['total_score'], reverse=True):
        level = get_level(data['total_score'])
        print(f"  {user}: {data['total_score']}/800 - {level}")

    # Dimension comparison
    print("\nDimension Score Comparison:\n")

    dimensions = list(results.values())[0]['dimensions'].keys()

    for dim in dimensions:
        print(f"\n【{QUESTIONS.get(dim, dim)}】")
        for user, data in sorted(results.items(), key=lambda x: x[1]['dimensions'].get(dim, 0), reverse=True):
            score = data['dimensions'].get(dim, 0)
            print(f"  {user}: {score}/100")

    # Generate comparison report
    report = {
        "date": "2026-04-05",
        "users": users,
        "results": results
    }

    report_file = Path("clawaf_compare_report.json")
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\nComparison report saved to: {report_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ClawAF Team Comparison')
    parser.add_argument('--users', type=str, required=True, help='User list, comma-separated')

    args = parser.parse_args()
    users = [u.strip() for u in args.users.split(',')]

    compare_users(users)