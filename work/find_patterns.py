import json, glob, collections, sys
sys.stdout.reconfigure(encoding='utf-8')

phrases = collections.Counter()
for grade in ['senior2', 'senior3']:
    for f in sorted(glob.glob(f'work/data/{grade}/*.json')):
        d = json.load(open(f, encoding='utf-8'))
        for q in d['questions']:
            for opt in q['options'].values():
                for length in [6, 8, 10]:
                    for i in range(len(opt) - length + 1):
                        sub = opt[i:i+length]
                        phrases[sub] += 1

print("Top repeated sub-phrases:")
for p, c in phrases.most_common(40):
    if c >= 15:
        print(f"  {p}: {c}")
