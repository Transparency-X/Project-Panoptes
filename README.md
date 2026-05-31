# 👁️ Project Panoptes v2.0 – The Surveillance Cult Research Framework

**Project Panoptes** is an open‑source sociological research repository and educational framework dedicated to identifying, documenting, and analysing **Surveillance Cults** – modern high‑control groups that wield systemic monitoring, digital espionage, and algorithmic profiling to dominate their members.

> **v2.0 “The Framework Release”** transforms the original whitepaper into a structured, machine‑readable knowledge base that can power tools, fuel academic research, and educate the public.

---

## 📁 Full Repository Directory

```
panoptes/
├── .github/
│   └── workflows/
│       └── validate.yml                # CI to validate JSON data against schemas
├── .gitignore
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SAFETY_DISCLAIMER.md
├── LICENSE                             # CC BY 4.0 (docs/data) + MIT (code)
├── schema/
│   ├── group.schema.json               # JSON Schema for a surveillance cult record
│   ├── case-study.schema.json          # JSON Schema for long‑form case studies
│   └── source.schema.json              # Shared citation schema
├── data/
│   ├── bibliography.bib                # BibTeX references
│   ├── groups/                         # Validated group JSON files
│   │   ├── nxivm.json
│   │   ├── twin_flames_universe.json
│   │   ├── shincheonji.json
│   │   ├── scientology.json
│   │   ├── peoples_temple.json
│   │   ├── jehovahs_witnesses.json
│   │   ├── aum_shinrikyo.json
│   │   ├── rajneeshpuram.json
│   │   └── teal_swan.json
│   └── case-studies/                   # Optional long‑form narratives
├── docs/                               # Human‑readable documentation
│   ├── introduction.md
│   ├── four-pillars.md
│   ├── methodology.md
│   ├── case-studies.md
│   ├── psychology-of-escape.md
│   ├── glossary.md
│   ├── roadmap.md
│   └── index.md                        # Auto‑generated group index
├── scripts/
│   ├── validate_data.py                # Validate JSON against schemas
│   └── generate_docs.py                # Rebuild docs/index.md from data
├── tools/                              # Future software (AI analyser, etc.)
│   └── README.md
├── templates/                          # Future survivor & policy templates
│   └── README.md
└── assets/                             # Diagrams, images
    └── pillars_diagram.svg
```

---

## ✨ What’s New in v2.0

- **Structured data**: every group is stored as a validated JSON object, making analysis, comparison, and tool‑building trivial.
- **Extensible schema**: add a new group by submitting a single JSON file – no Markdown editing required.
- **Auto‑generated documentation**: the group index is built directly from the data, keeping everything in sync.
- **Ethical by design**: safety disclaimer, methodology, and contributor guidelines baked in from day one.
- **Roadmap refined**: clear separation between the knowledge base (now), survivor tools (v2.1), and AI analysis (v3.0).

---

## 📖 Overview

While traditional cults rely on physical isolation, modern high‑control groups increasingly leverage complex webs of systemic monitoring, digital espionage, coercive control, and algorithmic profiling. Project Panoptes centralises data on how these groups operate, providing researchers, psychologists, journalists, and the public with a comprehensive understanding of panoptic control mechanisms, recruitment strategies, and pathways to exit.

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/your-org/panoptes.git
cd panoptes

# Validate all group data against schemas
python scripts/validate_data.py

# Regenerate the group index (also runs automatically via CI)
python scripts/generate_docs.py
```

Browse the auto‑generated [Group Index](./docs/index.md) immediately after cloning.

---

## 🗺️ Roadmap

- [x] **v2.0 – The Structured Framework** (you are here)  
  Machine‑readable dataset, auto‑validation, contributor scaffolding.
- [ ] **v2.1 – Survivor Data Sanitisation Guide**  
  Step‑by‑step technical manual for removing spyware and reclaiming digital privacy.
- [ ] **v3.0 – AI Recruitment Analyser**  
  Open‑source NLP tool to detect cult grooming linguistics in text.
- [ ] **v4.0 – Policy & Advocacy Module**  
  Legislative templates and briefing papers for lawmakers.

---

## 🤝 Contributing

We welcome contributions from sociologists, cybersecurity experts, cult‑recovery advocates, developers, and survivors. Please read:

- [`CONTRIBUTING.md`](./CONTRIBUTING.md) – how to add a group, submit a fix, or propose a new feature.
- [`SAFETY_DISCLAIMER.md`](./SAFETY_DISCLAIMER.md) – important warnings before you start.
- [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md) – community standards.

---

## ⚠️ Safety & Ethics

Researching active high‑control groups carries real risks of retaliation, doxxing, and psychological harm.  
**Read the full disclaimer** before contributing: [`SAFETY_DISCLAIMER.md`](./SAFETY_DISCLAIMER.md).

---

## 📜 License

- **Data & Documentation**: [Creative Commons Attribution 4.0 International](./LICENSE) (CC BY 4.0)
- **Software**: [MIT License](./LICENSE)

---

<p align="center">
  <sub>Named after the all‑seeing giant in Greek mythology – because knowledge is the first step to freedom.</sub>
</p>
