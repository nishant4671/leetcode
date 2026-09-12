import heapq

class SeatManager:

    def __init__(self, n: int):
        # A min-heap to store seat numbers that are currently available for reservation.
        # Initially, this heap will be empty. It will store seats that were
        # previously reserved and then unreserved, allowing them to be
        # reserved again.
        self.available_seats = [] 
        
        # This integer tracks the smallest seat number that has not yet been
        # reserved even once and is therefore available.
        # It acts as a counter for sequentially assigning new seats.
        self.next_seat_to_assign = 1 

    def reserve(self) -> int:
        if self.available_seats:
            # If there are seats in the min-heap (meaning some seats were unreserved),
            # the smallest-numbered among them is the next seat to be reserved.
            return heapq.heappop(self.available_seats)
        else:
            # If the min-heap is empty, it means all previously unreserved seats
            # have been taken. In this case, we assign the next seat in sequential
            # order that has never been reserved before.
            seat = self.next_seat_to_assign
            self.next_seat_to_assign += 1
            return seat

    def unreserve(self, seatNumber: int) -> None:
        # When a seat is unreserved, we add its number to the min-heap.
        # This makes it available for future `reserve` calls, and because it's a
        # min-heap, it ensures that this seat will be picked if it's the
        # smallest available one.
        heapq.heappush(self.available_seats, seatNumber)