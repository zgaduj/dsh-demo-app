# dsh-demo-app

Minimalny projekt testowy dla prototypu `dsh-superagent`: filtr priorytetów dla listy zadań.

## Zawartość

- `todo/priority.py` — `parse_level`, `higher_than`, `label`
- `tests/` — pytest

## Uruchomienie testów

```sh
python3 -m pytest -q
```

## Znany brak

`tests/test_sort.py` oczekuje funkcji `priority.sort_by_priority(items)`, której jeszcze nie ma
(posortowanie malejąco po priorytecie, bez mutowania wejścia).
