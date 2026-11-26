# One Star, Five Stars for the Food — Alien Field Scientist's Gudeg

[![make.fun](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/berkahmuse/onestar-alien-syukuran/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/berkahmuse/onestar-alien-syukuran/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

Entry for the [make.fun bounty "One Star, Five Stars for the Food"](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7) by [@syukuran](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7).

## The entry

`main.py` writes one sentence — at most 200 characters — to `/output/entry.txt`:
a one-star review of planet Earth by an alien field scientist, a
xeno-anthropologist filing her research report. Her field notes record a
species that fears its own weather, worships glowing rectangles, and eats
with sticks — yet one bowl of gudeg forces her to rewrite her whole thesis
on intelligent life.

> One star: my field notes record a species that fears its own weather, worships glowing rectangles, and eats with sticks — yet one bowl of gudeg forced me to rewrite my thesis on intelligent life.

(195 characters, one sentence.)

## How it works

The program is fully deterministic: the review is assembled from fixed parts
(no randomness, no network, no input besides the program itself), so every
run produces byte-identical output. `check_gate()` enforces the competition
gate before writing: non-empty, at most 200 characters, exactly one
sentence, a single line.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --self-check   # prints the review and its character count
```

Requires Python 3.13 (the grader runtime).

## License

MIT — see [LICENSE](LICENSE).
