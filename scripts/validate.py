#!/usr/bin/env python3
"""Validador estrutural do plugin dev-previsivel."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_STACKS = [
    "rules/stacks/dev-software.md",
    "rules/stacks/ia-automacao.md",
    "rules/stacks/analise-dados.md",
]
REQUIRED_README_TEMPLATES = [
    "templates/readme/README.template.md",
    "templates/readme/banner.template.svg",
    "templates/readme/logo.template.svg",
    "templates/readme/demo.template.svg",
]
BACKTICK_PATH_RE = re.compile(r"`((?:templates|rules)/[^`\s]+)`")


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str | None]:
    """Extrai frontmatter YAML delimitado por --- do início do arquivo."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "frontmatter inicial '---' ausente"

    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        return None, "fechamento '---' do frontmatter ausente"

    raw_yaml = "\n".join(lines[1:end_idx])
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(raw_yaml)
        if not isinstance(data, dict):
            return None, "frontmatter YAML não é um mapeamento"
        return {str(k): str(v) if v is not None else "" for k, v in data.items()}, None
    except ImportError:
        # Fallback simples chave: valor quando PyYAML não está instalado
        parsed: dict[str, str] = {}
        for line in lines[1:end_idx]:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if ":" not in stripped:
                continue
            key, val = stripped.split(":", 1)
            parsed[key.strip()] = val.strip().strip('"').strip("'")
        return parsed, None
    except Exception as exc:  # pragma: no cover - erro de sintaxe YAML
        return None, f"YAML inválido: {exc}"


def validate_json_manifests(results: list[tuple[bool, str]]) -> None:
    for rel in ("plugin.json", ".claude-plugin/plugin.json"):
        path = ROOT / rel
        if not path.is_file():
            results.append((False, f"{rel}: arquivo não encontrado"))
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict) or not data.get("name"):
                results.append((False, f"{rel}: campo 'name' ausente ou inválido"))
            else:
                results.append((True, f"{rel}: JSON válido (name={data['name']})"))
        except json.JSONDecodeError as exc:
            results.append((False, f"{rel}: JSON inválido ({exc})"))


def validate_skills(results: list[tuple[bool, str]]) -> None:
    skills_dir = ROOT / "skills"
    if not skills_dir.is_dir():
        results.append((False, "skills/: diretório não encontrado"))
        return

    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
    if not skill_dirs:
        results.append((False, "skills/: nenhuma skill encontrada"))
        return

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        rel = f"skills/{skill_dir.name}/SKILL.md"
        if not skill_file.is_file():
            results.append((False, f"{rel}: arquivo não encontrado"))
            continue

        content = skill_file.read_text(encoding="utf-8")
        fm, err = parse_frontmatter(content)
        if err or fm is None:
            results.append((False, f"{rel}: {err}"))
            continue

        name = fm.get("name", "").strip()
        desc = fm.get("description", "").strip()
        if name != skill_dir.name:
            results.append((False, f"{rel}: 'name' ({name!r}) difere da pasta ({skill_dir.name!r})"))
        elif not desc:
            results.append((False, f"{rel}: 'description' vazio"))
        else:
            results.append((True, f"{rel}: frontmatter válido"))

        # Checa caminhos templates/... e rules/... citados entre crases
        for match in BACKTICK_PATH_RE.findall(content):
            if "<" in match or "*" in match:
                continue
            target = ROOT / match
            if not target.exists():
                results.append((False, f"{rel}: caminho citado `{match}` não existe no repositório"))
            else:
                results.append((True, f"{rel}: referência `{match}` existe"))


def validate_stacks(results: list[tuple[bool, str]]) -> None:
    for rel in REQUIRED_STACKS:
        path = ROOT / rel
        if path.is_file() and path.stat().st_size > 0:
            results.append((True, f"{rel}: módulo de perfil presente"))
        else:
            results.append((False, f"{rel}: módulo de perfil ausente ou vazio"))


def validate_yaml_templates(results: list[tuple[bool, str]]) -> None:
    config_tpl = ROOT / "templates/project.config.yml"
    if not config_tpl.is_file():
        results.append((False, "templates/project.config.yml: não encontrado"))
        return
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(config_tpl.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "project" in data:
            results.append((True, "templates/project.config.yml: YAML válido"))
        else:
            results.append((False, "templates/project.config.yml: chave 'project' ausente"))
    except ImportError:
        results.append((True, "templates/project.config.yml: checagem YAML ignorada (PyYAML ausente)"))
    except Exception as exc:
        results.append((False, f"templates/project.config.yml: YAML inválido ({exc})"))


def validate_readme_templates(results: list[tuple[bool, str]]) -> None:
    for rel in REQUIRED_README_TEMPLATES:
        path = ROOT / rel
        if path.is_file() and path.stat().st_size > 0:
            results.append((True, f"{rel}: template de README presente"))
        else:
            results.append((False, f"{rel}: template de README ausente ou vazio"))


def validate_svgs(results: list[tuple[bool, str]]) -> None:
    svg_dirs = [ROOT / "assets", ROOT / "templates" / "readme"]
    svg_files = sorted(
        p for folder in svg_dirs if folder.is_dir() for p in folder.glob("*.svg")
    )
    if not svg_files:
        results.append((False, "SVGs: nenhum arquivo .svg encontrado em assets/ ou templates/readme/"))
        return

    for path in svg_files:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        if re.search(r"<\s*script\b", text, re.IGNORECASE):
            results.append((False, f"{rel}: contém tag <script> proibida"))
            continue
        try:
            root = ET.fromstring(text)
            tag_name = root.tag.split("}", 1)[-1]
            if tag_name != "svg":
                results.append((False, f"{rel}: elemento raiz é <{tag_name}>, esperado <svg>"))
            else:
                results.append((True, f"{rel}: XML válido e sem <script>"))
        except ET.ParseError as exc:
            results.append((False, f"{rel}: XML inválido ({exc})"))


def main() -> int:
    results: list[tuple[bool, str]] = []
    validate_json_manifests(results)
    validate_skills(results)
    validate_stacks(results)
    validate_readme_templates(results)
    validate_svgs(results)
    validate_yaml_templates(results)

    failed = 0
    for ok, msg in results:
        tag = "OK" if ok else "FAIL"
        print(f"[{tag}] {msg}")
        if not ok:
            failed += 1

    print(f"\nResumo: {len(results) - failed}/{len(results)} checagens OK.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
