import re

with open('2023/input03', 'r') as inp:
    inputs = inp.read().splitlines()

line_len = len(inputs[0])
inputs.insert(0, '.'*line_len)
inputs.append('.'*line_len)

# part 1 #
symbols_pos = []
for line in inputs:
    spos = []
    p = re.compile("[^\d\.]")
    for m in p.finditer(line):
        spos.append(m.start())
    symbols_pos.append(spos)

sum_of_parts = 0
for i, line in enumerate(inputs[1:-1]):
    i += 1
    p = re.compile("\d+")
    for m in p.finditer(line):
        part = int(m.group())
        start = m.start()
        end = m.end() - 1
        if start-1 in symbols_pos[i]:
            print(part, start, end, 1)
            sum_of_parts += part
            continue
        if end+1 in symbols_pos[i]:
            print(part, start, end, 2)
            sum_of_parts += part
            continue
        if any([(pos>=(start-1) and pos<=(end+1)) for pos in symbols_pos[i-1]]):
            print(part, start, end, 3)
            sum_of_parts += part
            continue
        if any([(pos>=(start-1) and pos<=(end+1)) for pos in symbols_pos[i+1]]):
            print(part, start, end, 4)
            sum_of_parts += part

# part 2 #
part = []
part_start = []
part_end = []
for line in inputs:
    st, en, pt = [], [], []
    p = re.compile("\d+")
    for m in p.finditer(line):
        pt.append(int(m.group()))
        st.append(m.start())
        en.append(m.end()-1)
    part.append(pt)
    part_start.append(st)
    part_end.append(en)

sum_of_gear_ratio = 0
for i, line in enumerate(inputs[1:-1]):
    i += 1
    p = re.compile("\*")
    for m in p.finditer(line):
        pos = m.start()
        try:
            part1 = [part[i][part_end[i].index(pos-1)]]
        except Exception:
            part1 = []
        try:
            part2 = [part[i][part_start[i].index(pos+1)]]
        except Exception:
            part2 = []
        if any(filter:=[(en>=(pos-1) and st<=(pos+1)) for st, en in zip(part_start[i-1], part_end[i-1])]):
            part3 = [i for i, v in zip(part[i-1], filter) if v]
        else:
            part3 = []
        if any(filter:=[(en>=(pos-1) and st<=(pos+1)) for st, en in zip(part_start[i+1], part_end[i+1])]):
            part4 = [i for i, v in zip(part[i+1], filter) if v]
        else:
            part4 = []
        if len(adj_parts:=part1+part2+part3+part4)==2:
            gear_ratio = adj_parts[0]*adj_parts[1]
            sum_of_gear_ratio += gear_ratio
