from collections import deque
import bisect

class Solution(object):
    def minOperations(self, s, k):
        n = len(s)
        z = s.count('0')

        if z == 0:
            return 0

        visited = [False] * (n + 1)
        visited[z] = True

        even = sorted([i for i in range(n + 1) if i % 2 == 0])
        odd = sorted([i for i in range(n + 1) if i % 2 == 1])

        if z % 2 == 0:
            even.remove(z)
        else:
            odd.remove(z)

        q = deque([(z, 0)])

        while q:
            curr, steps = q.popleft()

            low_i = max(0, k - (n - curr))
            high_i = min(k, curr)

            low = curr + k - 2 * high_i
            high = curr + k - 2 * low_i

            parity = (curr + k) % 2
            target_list = even if parity == 0 else odd

            left = bisect.bisect_left(target_list, low)
            right = bisect.bisect_right(target_list, high)

            next_states = target_list[left:right]
            del target_list[left:right]

            for nxt in next_states:
                if nxt == 0:
                    return steps + 1
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, steps + 1))

        return -1


if __name__ == "__main__":
    sol = Solution()

    print(sol.minOperations("110", 1))
    print(sol.minOperations("0101", 3))
    print(sol.minOperations("101", 2))