import heapq
class SeatManager:

    def __init__(self, n: int):
        self.heap = list(range(1, n+1))

    def reserve(self) -> int:
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)



test_seats = ["SeatManager","reserve","reserve","unreserve","unreserve","reserve","unreserve","reserve","unreserve"]
test_values = [[3],[],[],[1],[2],[],[1],[],[1]]

obj = eval(test_seats[0] + '(' + str(test_values[0][0]) + ')')
for i, j in zip(test_seats[1:], test_values[1:]):
    if j:
        print(
            eval(
                f'obj.{i}({j[0]})'
            )
        )
    else:
        print(eval(f'obj.{i}()'))

print(obj.seats)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)