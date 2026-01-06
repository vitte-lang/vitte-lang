# Vitte — vitte-lang (WIP)


<!-- Badges rapides -->
## 📈 Stats publiques GitHub

<p align="left">
  <img height="165"
    src="https://github-readme-stats-sigma-five.vercel.app/api?username=roussov&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&theme=transparent&cache_seconds=21600"
    alt="stats"
  />
  <img height="165"
    src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=roussov&layout=compact&langs_count=8&hide_border=true&theme=transparent&cache_seconds=21600"
    alt="top langs"
  />
</p>
<!-- Language badges -->
![Vitte](https://img.shields.io/badge/Vitte-language-6E56CF?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEwIDEyaDEwbDEyIDMwIDEyLTMwaDEwTDM2IDUySDI4eiIvPjwvc3ZnPg%3D%3D&logoColor=white)
![Muffin](https://img.shields.io/badge/Muffin-buildfile-FFB703?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTIwIDIyYzAtNyA2LTEyIDEyLTEyczEyIDUgMTIgMTJjMCA0LTIgNy01IDlsLTEgMnYxN0gyNlYzM2wtMS0yYy0zLTItNS01LTUtOXoiLz48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMjIgMzZoMjBsLTIgMThIMjR6Ii8%2BPC9zdmc%2B&logoColor=white)


Vitte est un langage de programmation en cours de construction, conçu comme un projet **toolchain-first** : l’objectif n’est pas seulement la syntaxe, mais un ensemble cohérent comprenant compilateur, bibliothèque standard, packaging, tests, et une trajectoire vers le **self-hosting**.

Le projet est en phase active de structuration. Les interfaces et la grammaire peuvent évoluer rapidement.

---

## Objectifs

- Construire un langage généraliste avec une chaîne de compilation maîtrisée.
- Mettre en place un pipeline de build reproductible (manifest, dépendances, profils).
- Fournir une stdlib modulaire et stable à terme.
- Supporter une architecture multi-stage pour atteindre un compilateur écrit en Vitte.
- Encadrer proprement l’ABI / calling convention pour viser plusieurs cibles (OS/arch).

---

## État actuel

Le dépôt progresse par briques “compilateur” et “infrastructure” :

- **Front-end** : lexer/parser (noyau + surface), diagnostics, structure AST.
- **Désucrage** : une couche surface pensée pour produire un core canonique de façon déterministe.
- **ABI / calling conventions** : classification (registres, modes de passage, signature ABI) + routage canonique selon la target.
- **Packaging** : manifests et conventions de build via Muffin.
- **Tests** : scénarios smoke et unités pour verrouiller les invariants au fil de l’évolution.

Les “stats” (nombre de modules, couverture, etc.) ne sont pas figées : la priorité est la stabilisation des primitives (grammaire, APIs std, build, ABI).

---

## Choix de conception

- **Lisibilité et déterminisme** : conventions de blocs et structure de code pensées pour limiter l’ambiguïté côté parsing et faciliter l’outillage.
- **Séparation core / surface** : le core sert d’IR syntaxique stable ; la surface améliore l’ergonomie et se désucre vers le core.
- **Modularité** : stdlib et composants compilateur organisés en modules explicites.
- **Portabilité** : l’ABI/callconv est traitée comme une couche à part entière, routée par target, pour permettre l’ajout progressif de backends.

---

## Projet en privé

Le dépôt est maintenu en privé tant que ces éléments ne sont pas suffisamment stabilisés :

- grammaire (référence parser + référence EBNF),
- conventions de modules/stdlib,
- pipeline de build et packaging,
- conventions ABI/callconv par target.

L’objectif est d’éviter de figer trop tôt des interfaces publiques.

---

## Roadmap (haute-niveau)

- Stabilisation de la grammaire et des conventions de surface
- Renforcement des diagnostics et des tests
- Consolidation ABI/callconv (impls par arch/OS)
- Progression vers le self-hosting (stage1 → stage2)
- Durcissement packaging (versioning, dépendances, reproductibilité)

---

## Publication

Une ouverture progressive (documentation, guidelines, contribution) est prévue une fois la base suffisamment stable.
