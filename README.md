# Vitte — vitte-lang
🟦 Le langage Vitte — https://github.com/vitte-lang/vitte
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
![Steel](https://img.shields.io/badge/Vitte-command-file-FFB703?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTIwIDIyYzAtNyA2LTEyIDEyLTEyczEyIDUgMTIgMTJjMCA0LTIgNy01IDlsLTEgMnYxN0gyNlYzM2wtMS0yYy0zLTItNS01LTUtOXoiLz48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMjIgMzZoMjBsLTIgMThIMjR6Ii8%2BPC9zdmc%2B&logoColor=white)

<!-- PROJECT_BADGES_END -->

## Vitte — un langage complet pour construire vite et proprement

Vitte est un nouveau langage de programmation en construction, pensé pour livrer
des outils et des petits programmes sans bricolage.
Il combine un compilateur, une IR/bytecode et un outil de build (Steel) pour
garder un flux simple, fiable et reproductible.

### En clair
- Écrire du code en Vitte.
- Compiler vers un format interne prêt à exécuter ou à brancher un backend.
- Builder/tester avec Steel.

### Ce que Vitte vise
- Une chaîne complète, pas juste une syntaxe.
- Une base claire et évolutive pour éviter les hacks.
- Une expérience de build et de tests cohérente.


---
```vit
space demo;

use std.io.{
    print,
    println
};

use std.math.{
    abs,
    max,
    min
};

const VERSION: string = "1.0.0";
const MAX_USERS: int = 1024;

pick Role
{
    Guest,
    User,
    Moderator,
    Administrator
}

pick Result<T, E>
{
    Ok(T),
    Err(E)
}

form Address
{
    city: string;
    country: string;
}

form User
{
    id: u64;
    name: string;
    age: int;
    active: bool;
    role: Role;
    address: Address;
}

proc make_user(
    id: u64,
    name: string,
    age: int,
    city: string,
    country: string
) -> User
{
    give User{
        id: id,
        name: name,
        age: age,
        active: true,
        role: Role::User,
        address: Address{
            city: city,
            country: country
        }
    };
}

proc birthday(user: User) -> User
{
    give User{
        id: user.id,
        name: user.name,
        age: user.age + 1,
        active: user.active,
        role: user.role,
        address: user.address
    };
}

proc sum(values: [int]) -> int
{
    let total: int = 0;
    let i: int = 0;

    while i < len(values)
    {
        set total = total + values[i];
        set i = i + 1;
    }

    give total;
}

proc average(values: [int]) -> f64
{
    if len(values) == 0
    {
        give 0.0;
    }

    give sum(values) / len(values);
}

proc factorial(value: int) -> int
{
    if value <= 1
    {
        give 1;
    }

    give value * factorial(value - 1);
}

proc fibonacci(value: int) -> int
{
    if value <= 1
    {
        give value;
    }

    give fibonacci(value - 1) + fibonacci(value - 2);
}

proc clamp(value: int, low: int, high: int) -> int
{
    if value < low
    {
        give low;
    }

    if value > high
    {
        give high;
    }

    give value;
}

proc identity<T>(value: T) -> T
{
    give value;
}

proc swap<T>(a: T, b: T) -> (T, T)
{
    give (b, a);
}

proc is_even(value: int) -> bool
{
    give value % 2 == 0;
}

proc divide(a: int, b: int) -> Result<int, string>
{
    if b == 0
    {
        give Result::Err("division by zero");
    }

    give Result::Ok(a / b);
}

proc print_role(role: Role)
{
    match role
    {
        Role::Guest =>
        {
            println("guest");
        }

        Role::User =>
        {
            println("user");
        }

        Role::Moderator =>
        {
            println("moderator");
        }

        Role::Administrator =>
        {
            println("administrator");
        }
    }
}

proc demo_conditions(value: int)
{
    if value < 0
    {
        println("negative");
    }
    else if value == 0
    {
        println("zero");
    }
    else
    {
        println("positive");
    }
}

proc demo_loop()
{
    let i: int = 0;

    while i < 10
    {
        print(i);
        set i = i + 1;
    }
}

proc demo_array()
{
    let values: [int] = [
        5,
        10,
        15,
        20
    ];

    println(len(values));
    println(sum(values));
    println(average(values));
}

proc demo_users()
{
    let users: [User] = [];

    let alice = make_user(
        1,
        "Alice",
        25,
        "Paris",
        "France"
    );

    let bob = make_user(
        2,
        "Bob",
        31,
        "London",
        "United Kingdom"
    );

    set users = users + [alice];
    set users = users + [bob];

    let i: int = 0;

    while i < len(users)
    {
        println(users[i].name);
        println(users[i].age);

        set i = i + 1;
    }
}

proc main() -> int
{
    println("Vitte");
    println(VERSION);

    let numbers: [int] = [
        1,
        2,
        3,
        4,
        5
    ];

    println(sum(numbers));
    println(average(numbers));

    println(factorial(6));
    println(fibonacci(12));

    println(clamp(120, 0, 100));

    let value = identity(42);
    println(value);

    let first = 10;
    let second = 20;

    let (a, b) = swap(first, second);

    println(a);
    println(b);

    println(is_even(18));

    let result = divide(10, 2);

    match result
    {
        Result::Ok(value) =>
        {
            println(value);
        }

        Result::Err(message) =>
        {
            println(message);
        }
    }

    let user = make_user(
        1,
        "Vincent",
        29,
        "Paris",
        "France"
    );

    let updated = birthday(user);

    println(updated.name);
    println(updated.age);

    print_role(updated.role);

    demo_conditions(-5);
    demo_conditions(0);
    demo_conditions(8);

    demo_loop();
    demo_array();
    demo_users();

    println(abs(-50));
    println(max(100, 200));
    println(min(100, 200));

    give 0;
}

### Exemple Syntaxe !muf4 pour Steel (steelconf)

```steelconf
!muf 4
;; Exemple complet: bakes build_debug/build_release et sorties ciblees

[workspace]
  .set name "example-c"
  .set root "."
  .set target_dir "target"
  .set profile "release"
..

[profile debug]
  .set opt 0
  .set debug 1
..

[profile release]
  .set opt 2
  .set debug 0
..

[tool cc]
  .exec "cc"
..

[bake build_debug]
  .make c_src cglob "src/**/*.c"
  [run cc]
    .set "-O${opt}" 1
    .set "-g" "${debug}"
    .takes c_src as "@args"
    .emits exe as "-o"
  ..
  .output exe "target/out/c_app_debug"
..

[bake build_release]
  .make c_src cglob "src/**/*.c"
  [run cc]
    .set "-O${opt}" 1
    .set "-g" "${debug}"
    .takes c_src as "@args"
    .emits exe as "-c"
  ..
  .output exe "target/out/c_app_release"
..
```
### Commandes (le minimum)

```bash
# build tout
steel build steelconf
# ou bien:
steel run
```
---

## Publication

Une ouverture progressive (documentation, guidelines, contribution) est prévue une fois la base suffisamment stable.
