import json, random

with open(r'work\paperC_data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

mcq = d['mcq']

# Desired targets:
# Group A (40): 10 A, 10 B, 10 C, 10 D
# Group B (10): 3 A, 2 B, 2 C, 3 D
# Group C (10): 2 A, 3 B, 3 C, 2 D
# Total: 15 A, 15 B, 15 C, 15 D

target_A = ['A']*10 + ['B']*10 + ['C']*10 + ['D']*10
target_B = ['A']*3 + ['B']*2 + ['C']*3 + ['D']*2
target_C = ['A']*2 + ['B']*3 + ['C']*2 + ['D']*3

# deterministic seed
random.seed(42)
random.shuffle(target_A)
random.shuffle(target_B)
random.shuffle(target_C)

# Function to re-assign correct option to target_letter
def reassign_question(q, target_ans):
    curr_ans = q['ans']
    if curr_ans == target_ans:
        return q
    # swap the option text between curr_ans and target_ans
    opt_curr = q['opts'][curr_ans]
    opt_target = q['opts'][target_ans]
    q['opts'][target_ans] = opt_curr
    q['opts'][curr_ans] = opt_target
    q['ans'] = target_ans
    return q

for i in range(40):
    reassign_question(mcq[i], target_A[i])

for i in range(10):
    reassign_question(mcq[40 + i], target_B[i])

for i in range(10):
    reassign_question(mcq[50 + i], target_C[i])

# verify counts
counts = {}
for q in mcq:
    counts[q['ans']] = counts.get(q['ans'], 0) + 1
print('New overall counts:', sorted(counts.items()))

grpA = [q for q in mcq if q['g'] == 'A']
cA = {}
for q in grpA:
    cA[q['ans']] = cA.get(q['ans'], 0) + 1
print('New Group A counts:', sorted(cA.items()))

grpB = [q for q in mcq if q['g'] == 'B']
cB = {}
for q in grpB:
    cB[q['ans']] = cB.get(q['ans'], 0) + 1
print('New Group B counts:', sorted(cB.items()))

grpC = [q for q in mcq if q['g'] == 'C']
cC = {}
for q in grpC:
    cC[q['ans']] = cC.get(q['ans'], 0) + 1
print('New Group C counts:', sorted(cC.items()))

d['mcq'] = mcq
with open(r'work\paperC_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('Balanced and saved successfully!')
