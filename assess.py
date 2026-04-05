#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ClawAF Self-Assessment Script
Claw Assessment Framework
"""
import json
from pathlib import Path

# Assessment questions
QUESTIONS = {
    "identity_cognition": {
        "name": "身份认知度",
        "questions": [
            "你有完整的身份文档（AGENTS.md/SOUL.md/PROFILE.md）吗？",
            "身份文档包含清晰的规则、偏好吗？",
            "身份文档持续更新吗？",
            "AI 能准确回答关于自己的问题吗？",
        ]
    },
    "memory_capability": {
        "name": "记忆能力",
        "questions": [
            "你有持久化记忆系统吗？",
            "记忆系统能语义检索吗？",
            "记忆会自动学习吗？",
            "检索准确度高吗？",
        ]
    },
    "security_mechanism": {
        "name": "安全机制",
        "questions": [
            "有敏感信息防护机制吗？",
            "有权限验证吗？",
            "有多层防护吗？",
            "有审计追踪吗？",
        ]
    },
    "automation_level": {
        "name": "自动化程度",
        "questions": [
            "常见场景能自动化处理吗？",
            "有场景自动触发机制吗？",
            "错误能自动恢复吗？",
            "工作流标准化了吗？",
        ]
    },
    "skill_ecosystem": {
        "name": "技能体系",
        "questions": [
            "有技能分类系统吗？",
            "技能文档完整吗？",
            "有技能发现机制吗？",
            "技能容易扩展吗？",
        ]
    },
    "collaboration_rapport": {
        "name": "协作默契度",
        "questions": [
            "沟通效率高吗？",
            "AI 能准确理解你的意图吗？",
            "反馈循环顺畅吗？",
            "有信任关系吗？",
        ]
    },
    "experience_accumulation": {
        "name": "经验积累",
        "questions": [
            "有经验记录系统吗？",
            "经验分类清晰吗？",
            "能智能检索经验吗？",
            "经验能有效应用吗？",
        ]
    },
    "evolution_capability": {
        "name": "进化能力",
        "questions": [
            "有自我审视机制吗？",
            "能从经验中学习吗？",
            "有任务固化机制吗？",
            "能闭环进化吗？",
        ]
    },
}

def get_level(score):
    """根据分数获取等级"""
    if score >= 600:
        return "传奇"
    elif score >= 520:
        return "钻石"
    elif score >= 400:
        return "铂金"
    elif score >= 280:
        return "黄金"
    elif score >= 160:
        return "白银"
    else:
        return "青铜"

def assess():
    """Self-assessment"""
    print("=" * 70)
    print("ClawAF - Claw Assessment Framework")
    print("=" * 70)
    print("\nPlease answer the following questions (0=No, 1=Partially, 2=Yes):\n")

    scores = {}

    for key, info in QUESTIONS.items():
        print(f"\n【{info['name']}】")
        dimension_score = 0

        for i, question in enumerate(info['questions'], 1):
            while True:
                try:
                    answer = input(f"  {i}. {question} (0/1/2): ").strip()
                    if answer in ['0', '1', '2']:
                        dimension_score += int(answer) * 6.25  # 4 questions, 25 points each
                        break
                    else:
                        print("    Please enter 0, 1, or 2")
                except KeyboardInterrupt:
                    print("\n\nAssessment cancelled")
                    return

        scores[key] = int(dimension_score)
        print(f"  得分: {scores[key]}/100")

    total_score = sum(scores.values())
    level = get_level(total_score)

    print("\n" + "=" * 70)
    print("Assessment Results")
    print("=" * 70)

    for key, info in QUESTIONS.items():
        print(f"{info['name']}: {scores[key]}/100")

    print(f"\nTotal Score: {total_score}/800")
    print(f"Level: {level}")

    # Save results
    result = {
        "date": "2026-04-05",
        "total_score": total_score,
        "level": level,
        "dimensions": scores
    }

    result_file = Path("clawaf_result.json")
    with open(result_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\nResults saved to: {result_file}")

if __name__ == '__main__':
    assess()