# Vitte — vitte-lang (WIP)


<!-- Badges rapides -->
![Profile views](https://komarev.com/ghpvc/?username=vitte-lang&style=for-the-badge&color=00E5FF&label=views)
![Org total](https://img.shields.io/endpoint?style=for-the-badge&label=org%20total&color=00E5FF&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvitte-lang%2Fvitte-lang%2Fmain%2Fbadges%2Forg_totals.json)
![Repo total](https://img.shields.io/endpoint?style=for-the-badge&label=repo%20total&color=7CFF6B&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvitte-lang%2Fvitte-lang%2Fmain%2Fbadges%2Frepo_totals.json)
![Vitte repo](https://img.shields.io/endpoint?style=for-the-badge&label=vitte%20repo&color=FFD166&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvitte-lang%2Fvitte-lang%2Fmain%2Fbadges%2Fvitte_repo_totals.json)

### Langages (tous les projets)

<!-- Org language mix (generated endpoints) -->
![Org languages](https://img.shields.io/endpoint?style=for-the-badge&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvitte-lang%2Fvitte-lang%2Fmain%2Fbadges%2Forg_languages_summary.json)

### Langages (ce dépôt)


<!-- Repo language mix (generated endpoints) -->
![Languages](https://img.shields.io/endpoint?style=for-the-badge&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvitte-lang%2Fvitte-lang%2Fmain%2Fbadges%2Flanguages_summary.json)
![Vitte %](https://img.shields.io/endpoint?style=for-the-badge&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvitte-lang%2Fvitte-lang%2Fmain%2Fbadges%2Flang_vitte.json)
![Muffin %](https://img.shields.io/endpoint?style=for-the-badge&url=https%3A%2F%2Fraw.githubusercontent.com%2Fvitte-lang%2Fvitte-lang%2Fmain%2Fbadges%2Flang_muffin.json)


<!-- Language badges -->
![Vitte](https://img.shields.io/badge/Vitte-language-6E56CF?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEwIDEyaDEwbDEyIDMwIDEyLTMwaDEwTDM2IDUySDI4eiIvPjwvc3ZnPg%3D%3D&logoColor=white)
![Muffin](https://img.shields.io/badge/Muffin-buildfile-FFB703?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTIwIDIyYzAtNyA2LTEyIDEyLTEyczEyIDUgMTIgMTJjMCA0LTIgNy01IDlsLTEgMnYxN0gyNlYzM2wtMS0yYy0zLTItNS01LTUtOXoiLz48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMjIgMzZoMjBsLTIgMThIMjR6Ii8%2BPC9zdmc%2B&logoColor=white)

### Projets publics

<!-- PROJECT_BADGES_START -->
- [vitte-lang](https://github.com/vitte-lang/vitte-lang)
- [VitteLangVsCode](https://github.com/vitte-lang/VitteLangVsCode)
- [homebrew-vitte](https://github.com/vitte-lang/homebrew-vitte)
- [VitteServerPluginsBackEnd-org](https://github.com/vitte-lang/VitteServerPluginsBackEnd-org)
- [PlatonEditor](https://github.com/vitte-lang/PlatonEditor)
- [linguist](https://github.com/vitte-lang/linguist)
- [muffin](https://github.com/vitte-lang/muffin)
- [muffin-org](https://github.com/vitte-lang/muffin-org)
- [steel.org](https://github.com/vitte-lang/steel.org)
- [OldSteel](https://github.com/vitte-lang/OldSteel)
<!-- PROJECT_BADGES_END -->

## Vitte — un langage complet pour construire vite et proprement

Vitte est un nouveau langage de programmation en construction, pensé pour livrer
des outils et des petits programmes sans bricolage.
Il combine un compilateur, une IR/bytecode et un outil de build (Muffin) pour
garder un flux simple, fiable et reproductible.

### En clair
- Écrire du code en Vitte.
- Compiler vers un format interne prêt à exécuter ou à brancher un backend.
- Builder/tester avec Muffin.

### Ce que Vitte vise
- Une chaîne complète, pas juste une syntaxe.
- Une base claire et évolutive pour éviter les hacks.
- Une expérience de build et de tests cohérente.

### Le repo Vitte
Le dépôt principal du langage (compilateur, IR/bytecode, stdlib, tests) est privé.

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
