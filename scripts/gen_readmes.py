#!/usr/bin/env python3
"""Generate detailed README.md for each Verilog design file.

- Extract module name, ports (direction, width, name).
- Detect sub‑module instantiations.
- Produce a markdown file next to the .v source containing:
  * Header with module name
  * Placeholder for hand‑written description
  * Input table, Output table
  * Brief functionality section (auto‑generated placeholder)
  * Mermaid diagram showing hierarchy of instantiated sub‑modules.

The script is deliberately simple – it uses regular expressions so no external
dependency is required. It is meant to be run once after any design change.
"""

import os
import re
from pathlib import Path

MODULE_RE = re.compile(r"module\s+(?P<name>\w+)\s*#?\s*\((?P<portlist>.*?)\)\s*;", re.S)
PORT_RE = re.compile(r"(?P<dir>input|output|inout)\s+(?:\[\s*(?P<msb>\d+)\s*:\s*(?P<lsb>\d+)\s*\]\s+)?(?P<name>\w+)", re.S)
INST_RE = re.compile(r"(?P<type>\w+)\s+(?P<inst>\w+)\s*\(.*?\);", re.S)

def parse_file(vfile: Path):
    text = vfile.read_text()
    m = MODULE_RE.search(text)
    if not m:
        return None
    name = m.group('name')
    ports_raw = m.group('portlist')
    ports = []
    for pm in PORT_RE.finditer(ports_raw):
        direction = pm.group('dir')
        msb = pm.group('msb')
        lsb = pm.group('lsb')
        width = '1' if not msb else f"{int(msb)-int(lsb)+1}"
        ports.append({
            'direction': direction,
            'name': pm.group('name'),
            'width': width
        })
    # find instantiated sub‑modules (simple heuristic, may miss generate statements)
    submods = []
    for im in INST_RE.finditer(text):
        submods.append({
            'type': im.group('type'),
            'inst': im.group('inst')
        })
    return name, ports, submods

def write_readme(vfile: Path, module_info):
    name, ports, submods = module_info
    readme_path = vfile.parent / "README.md"
    with readme_path.open('w') as f:
        f.write(f"# {name}\n\n")
        f.write("## Description\n\n")
        f.write("*Please provide a detailed hand‑written description of the module’s purpose, functionality, and any noteworthy design decisions.*\n\n")
        # Inputs
        inputs = [p for p in ports if p['direction'] == 'input']
        outputs = [p for p in ports if p['direction'] == 'output']
        f.write("## Interface\n\n")
        if inputs:
            f.write("### Inputs\n\n| Name | Width | Description |\n|------|-------|-------------|\n")
            for p in inputs:
                f.write(f"| {p['name']} | {p['width']} | – |\n")
            f.write("\n")
        if outputs:
            f.write("### Outputs\n\n| Name | Width | Description |\n|------|-------|-------------|\n")
            for p in outputs:
                f.write(f"| {p['name']} | {p['width']} | – |\n")
            f.write("\n")
        f.write("## Functionality\n\n*")
        f.write(f"This block implements the {name} logic. Fill in a concise high‑level description here.*\n\n")
        f.write("## Block Diagram (Mermaid)\n\n```mermaid\ngraph LR\n    % Sub‑module instances\n")
        for sm in submods:
            f.write(f"    {sm['inst']}[\"{sm['type']} {sm['inst']}\"] --> {name}\n")
        f.write("```\n")

def main():
    repo_root = Path(os.getenv('DESIGN_REPO_ROOT', '.') ).resolve()
    for vfile in repo_root.rglob('*.v'):
        info = parse_file(vfile)
        if info:
            write_readme(vfile, info)
    print("README generation complete.")

if __name__ == "__main__":
    main()
