#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ClawAF Result Formatter (中文版)
Convert evaluation results to multiple formats with Chinese labels
"""
import json
import sys
import io
from pathlib import Path
from typing import Dict

# Fix Windows encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


class ResultFormatterCN:
    """Format evaluation results to multiple formats (Chinese)"""

    # Dimension names in Chinese
    DIMENSION_NAMES = {
        "Identity Cognition": "身份认知度",
        "Memory Capability": "记忆能力",
        "Security Mechanism": "安全机制",
        "Automation Level": "自动化程度",
        "Skill Ecosystem": "技能体系",
        "Collaboration Rapport": "协作默契度",
        "Experience Accumulation": "经验积累",
        "Evolution Capability": "进化能力"
    }

    # Level names in Chinese
    LEVEL_NAMES = {
        "Bronze": "青铜",
        "Silver": "白银",
        "Gold": "黄金",
        "Platinum": "铂金",
        "Diamond": "钻石",
        "Legendary": "传奇"
    }

    def __init__(self, result: Dict):
        self.result = result

    def translate_dimension(self, name: str) -> str:
        """Translate dimension name to Chinese"""
        return self.DIMENSION_NAMES.get(name, name)

    def translate_level(self, name: str) -> str:
        """Translate level name to Chinese"""
        return self.LEVEL_NAMES.get(name, name)

    def to_markdown(self) -> str:
        """Convert to Markdown format (Chinese)"""
        lines = []

        # Title
        lines.append("# ClawAF 评估报告")
        lines.append("")
        lines.append(f"**日期：** {self.result.get('date', '未知')}")
        lines.append(f"**Claw 目录：** `{self.result.get('claw_directory', '未知')}`")
        lines.append(f"**等级：** **{self.translate_level(self.result.get('level', '未知'))}**")
        lines.append("")
        lines.append(f"## 总分")
        lines.append("")
        score = self.result.get('total_score', 0)
        lines.append(f"### {score}/800")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Dimensions
        lines.append("## 各维度评分")
        lines.append("")

        dimensions = self.result.get('dimensions', {})
        details = self.result.get('details', {})

        # Sort by score
        sorted_dims = sorted(dimensions.items(), key=lambda x: x[1], reverse=True)

        for dim_name, score in sorted_dims:
            # Create progress bar
            filled = "█" * (score // 10)
            empty = "░" * (10 - score // 10)
            bar = f"{filled}{empty}"

            lines.append(f"### {self.translate_dimension(dim_name)}")
            lines.append("")
            lines.append(f"**得分：** {score}/100")
            lines.append("")
            lines.append(f"进度：`{bar}`")
            lines.append("")

            # Details
            dim_details = details.get(dim_name, {})
            if dim_details:
                lines.append("**详情：**")
                lines.append("")
                for key, value in dim_details.items():
                    lines.append(f"- **{key}：** {value}")
                lines.append("")

        lines.append("---")
        lines.append("")

        # Footer
        lines.append("*由 ClawAF - Claw 评估框架生成*")
        lines.append("")

        return "\n".join(lines)

    def to_html(self) -> str:
        """Convert to HTML format (Chinese)"""
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ClawAF 评估报告</title>
    <style>
        body {{
            font-family: 'Microsoft YaHei', 'Segoe UI', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
        }}
        .total-score {{
            font-size: 48px;
            font-weight: bold;
            color: #3498db;
            text-align: center;
            margin: 20px 0;
        }}
        .level {{
            font-size: 24px;
            font-weight: bold;
            color: #2ecc71;
            text-align: center;
            margin-bottom: 20px;
        }}
        .dimension {{
            margin: 20px 0;
            padding: 15px;
            background: #ecf0f1;
            border-radius: 5px;
        }}
        .dimension h3 {{
            margin-top: 0;
            color: #2c3e50;
        }}
        .progress-bar {{
            height: 20px;
            background: #bdc3c7;
            border-radius: 10px;
            overflow: hidden;
            margin: 10px 0;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #3498db, #2ecc71);
            transition: width 0.3s ease;
        }}
        .details {{
            margin-top: 10px;
            font-size: 14px;
        }}
        .details ul {{
            margin: 5px 0;
            padding-left: 20px;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            color: #7f8c8d;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🐾 ClawAF 评估报告</h1>
        <p><strong>日期：</strong> {self.result.get('date', '未知')}</p>
        <p><strong>Claw 目录：</strong> <code>{self.result.get('claw_directory', '未知')}</code></p>

        <div class="total-score">{self.result.get('total_score', 0)}/800</div>
        <div class="level">等级：{self.translate_level(self.result.get('level', '未知'))}</div>

        <h2>各维度评分</h2>
"""

        dimensions = self.result.get('dimensions', {})
        details = self.result.get('details', {})

        # Sort by score
        sorted_dims = sorted(dimensions.items(), key=lambda x: x[1], reverse=True)

        for dim_name, score in sorted_dims:
            dim_details = details.get(dim_name, {})

            html += f"""
        <div class="dimension">
            <h3>{self.translate_dimension(dim_name)}</h3>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {score}%"></div>
            </div>
            <p><strong>得分：</strong> {score}/100</p>
"""

            if dim_details:
                html += f"""
            <div class="details">
                <ul>
"""
                for key, value in dim_details.items():
                    html += f"                    <li><strong>{key}：</strong> {value}</li>\n"
                html += """
                </ul>
            </div>
"""

            html += """
        </div>
"""

        html += """
        <div class="footer">
            <p>由 ClawAF - Claw 评估框架生成</p>
        </div>
    </div>
</body>
</html>
"""
        return html

    def save_all(self, output_dir: str = ".") -> None:
        """Save all formats"""
        output_path = Path(output_dir)

        # Save JSON
        json_path = output_path / "clawaf_result_cn.json"
        # Add Chinese labels to JSON
        result_cn = self.result.copy()
        if 'dimensions' in result_cn:
            result_cn['dimensions_cn'] = {
                self.translate_dimension(k): v
                for k, v in result_cn['dimensions'].items()
            }
        if 'level' in result_cn:
            result_cn['level_cn'] = self.translate_level(result_cn['level'])

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(result_cn, f, indent=2, ensure_ascii=False)
        print(f"✓ JSON (中文) 保存到: {json_path}")

        # Save Markdown
        md_path = output_path / "clawaf_result_cn.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(self.to_markdown())
        print(f"✓ Markdown (中文) 保存到: {md_path}")

        # Save HTML
        html_path = output_path / "clawaf_result_cn.html"
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(self.to_html())
        print(f"✓ HTML (中文) 保存到: {html_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("用法：python format_result_cn.py <result.json>")
        sys.exit(1)

    result_file = sys.argv[1]

    with open(result_file, 'r', encoding='utf-8') as f:
        result = json.load(f)

    formatter = ResultFormatterCN(result)
    formatter.save_all()

    print("\n所有格式已生成！")