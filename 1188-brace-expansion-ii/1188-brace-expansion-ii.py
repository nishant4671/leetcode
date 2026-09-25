class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        s = expression
        n = len(s)
        def parse_seq(i):
            cur_set, i = parse_factor(i)
            while i < n and s[i] not in '},':
                nxt_set, i = parse_factor(i)
                new_set = set()
                for a in cur_set:
                    for b in nxt_set:
                        new_set.add(a + b)
                cur_set = new_set
            return cur_set, i
        def parse_factor(i):
            if s[i] == '{':
                return parse_union(i)
            return {s[i]}, i + 1
        def parse_union(i):
            i += 1
            union_set = set()
            while True:
                seq_set, i = parse_seq(i)
                union_set.update(seq_set)
                if i < n and s[i] == ',':
                    i += 1
                    continue
                i += 1
                break
            return union_set, i
        result, _ = parse_seq(0)
        return sorted(result)