# Vitte — vitte-lang (WIP)


<!-- Badges rapides -->
## 📈 Stats publiques GitHub

<p align="left">
  <img
    height="165"
    src="https://github-readme-stats-sigma-five.vercel.app/api?username=vitte-lang&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&theme=transparent&cache_seconds=21600"
    alt="stats"
  />
  <img
    height="165"
    src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=vitte-lang&layout=compact&langs_count=8&hide_border=true&theme=transparent&cache_seconds=21600"
    alt="top langs"
  />
</p>



![Profile views](https://komarev.com/ghpvc/?username=vitte-lang&style=for-the-badge)

![CI](https://img.shields.io/github/actions/workflow/status/vitte-lang/vitte/ci.yml?branch=main&style=for-the-badge)
![Stars](https://img.shields.io/github/stars/vitte-lang/vitte?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/vitte-lang/vitte?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/vitte-lang/vitte?style=for-the-badge)
![PRs](https://img.shields.io/github/issues-pr/vitte-lang/vitte?style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/vitte-lang/vitte?style=for-the-badge)
![Commit activity](https://img.shields.io/github/commit-activity/m/vitte-lang/vitte?style=for-the-badge)
![Last commit](https://img.shields.io/github/last-commit/vitte-lang/vitte/main?style=for-the-badge)
![Org totals](https://img.shields.io/endpoint?style=for-the-badge&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvitte-lang%2Fvitte-lang%2Fmain%2Fbadges%2Forg_totals.json)

<!-- Repo language mix (generated endpoints) -->
![Languages](https://img.shields.io/endpoint?style=for-the-badge&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvitte-lang%2Fvitte%2Fmain%2Fbadges%2Flanguages_summary.json)
![Vitte %](https://img.shields.io/endpoint?style=for-the-badge&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvitte-lang%2Fvitte%2Fmain%2Fbadges%2Flang_vitte.json)
![Muffin %](https://img.shields.io/endpoint?style=for-the-badge&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvitte-lang%2Fvitte%2Fmain%2Fbadges%2Flang_muffin.json)


<!-- Language badges -->
![Vitte](https://img.shields.io/badge/Vitte-language-6E56CF?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEwIDEyaDEwbDEyIDMwIDEyLTMwaDEwTDM2IDUySDI4eiIvPjwvc3ZnPg%3D%3D&logoColor=white)
![Muffin](https://img.shields.io/badge/Muffin-buildfile-FFB703?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTIwIDIyYzAtNyA2LTEyIDEyLTEyczEyIDUgMTIgMTJjMCA0LTIgNy01IDlsLTEgMnYxN0gyNlYzM2wtMS0yYy0zLTItNS01LTUtOXoiLz48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMjIgMzZoMjBsLTIgMThIMjR6Ii8%2BPC9zdmc%2B&logoColor=white)


Vitte est un langage de programmation **en construction**.

### En 10 secondes
- Tu écris du code en Vitte.
- Le compilateur le transforme en **IR/bytecode**.
- Tu build/test avec **Muffin**.

### À quoi ça sert
- Construire des **outils** (CLI), des petits programmes, et une base solide pour aller plus loin.
- Avoir un projet “langage” qui ne fait pas que de la syntaxe : **build + stdlib + tests**.

### Commandes (le minimum)

```bash
# build tout
muffin build -all

# build debug / release
muffin build -debug
muffin build -release

# valider le projet
muffin validate
```

---

## Objectifs

- Avoir un **compilateur qui marche** (lexer + parser + diagnostics).
- Avoir une **stdlib utile** (modules testés).
- Avoir un **build/packaging** simple et reproductible via Muffin.

---

## État actuel

Le dépôt progresse par briques “compilateur” et “infrastructure” :

- **Compiler** : tokens → AST → transformations.
- **IR/Bytecode** : format interne pour exécuter/brancher un backend.
- **Muffin + tests** : builds reproductibles + garde-fous.

Les détails changent souvent : l’idée est d’avancer vite, sans casser ce qui marche.

---

## Choix de conception

- **Reproductible** : mêmes inputs → mêmes outputs.
- **Core interne** : plus simple à tester et à faire évoluer.
- **Modules clairs** : compiler/stdlib/build séparés.

---

## ✨ Exemples

### Exemple Vitte (hello)

```vit
# examples/hello/hello.vit

mod examples.hello

fn main() -> i32
  say "hello from Vitte"
  ret 0
.end
```

### Exemple Vitte (style vitte_amber)

```vit
# examples/token_dump/token_dump.vit

use vitte_amber.types::{TokenKind, token_kind_name}

mod examples.token_dump

fn main() -> i32
  let k = TokenKind::KwFn
  say token_kind_name(k)
  ret 0
.end
```

### Exemple Muffin (build.muf)

```muf
# build.muf — Muffin Bakefile v2 (exemple)

muf 2

workspace "vitte-lang"
  root "."
  out  "out/"
.end

package "vitte_amber"
  version "0.1.0"
  description "Lexer + Token stream + Bytecode IR for Vitte (example module)."
  license "MIT"
.end

profile "debug"
  opt 0
  debug true
.end

profile "release"
  opt 3
  debug false
  lto true
.end

target "vitte_amber"
  kind "lib"
  lang "vit"
  src  "src/"
  entry "src/lib.vit"
  out   "out/vitte_amber"
  profile use "debug"
.end
```

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
