# rage-bar-generator

A random rage/trap-style bar generator. Every line is assembled at
runtime from original templates and word banks (Mad-Libs style) — an
ad-lib, a subject, a flex or a piece of dark imagery, and an attitude
tag get shuffled together into a fresh line each run.

Nothing in this repo is scraped or copied from any artist's actual
lyrics; it's original vocabulary written to riff on the aesthetic
(ad-libs, flexing, dark/moody imagery, defiant attitude), not to
reproduce anyone's specific words.

## Usage

```bash
python3 generator.py            # print an 8-line verse
python3 generator.py -n 16      # print a 16-line verse
python3 generator.py -s 42      # use a fixed seed for reproducible output
```

## How it works

`generator.py` defines several word banks (`AD_LIBS`, `SUBJECTS`,
`FLEX_VERBS`, `FLEX_NOUNS`, `DARK_IMAGERY`, `ATTITUDE`, `BRAGS`) and a
list of line `TEMPLATES`. Each generated line picks a random template
and fills its slots with random picks from the relevant word banks.

Want different vocabulary or new sentence shapes? Edit the lists at
the top of `generator.py` — add words to a bank or new strings to
`TEMPLATES`, using the same `{slot}` names.

## License

MIT
