class Solution:
    def canAliceWin(self, n: int) -> bool:
        remaining_stones = n
        current_move_amount = 10  # Alice starts by removing 10 stones
        alice_turn = True         # True if it's currently Alice's turn, False if Bob's

        while True:
            # Check if the current player can make a valid move.
            # A valid move requires removing a positive number of stones.
            # If current_move_amount is 0 or less, the current player cannot make a valid move.
            if current_move_amount <= 0:
                # This means the previous player successfully removed 1 stone,
                # and now the current player is required to remove 0 or fewer stones.
                # The current player cannot make a move and thus loses.
                # If it's currently Alice's turn (alice_turn is True), it means Bob (previous player) won.
                # So Alice loses (return False).
                # If it's currently Bob's turn (alice_turn is False), it means Alice (previous player) won.
                # So Alice wins (return True).
                return not alice_turn
            
            # Check if there are enough stones for the current player to make their move.
            if remaining_stones < current_move_amount:
                # The current player does not have enough stones to remove the required amount.
                # The current player cannot make a move and thus loses.
                # If it's currently Alice's turn, Alice loses (return False).
                # If it's currently Bob's turn, Bob loses (return True, meaning Alice wins).
                return not alice_turn

            # The current player makes their move by removing stones.
            remaining_stones -= current_move_amount

            # Prepare for the next player's turn.
            current_move_amount -= 1  # The next player removes 1 fewer stone.
            alice_turn = not alice_turn  # Switch turns.