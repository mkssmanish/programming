import sys

def prison_dilemma(player1_choice, player2_choice):
    """
    Simulate the outcome of the Prisoner's Dilemma game based on your provided outcomes.
    
    :param player1_choice: 'S' (Silent/Cooperate) or 'T' (Testify/Defect) for Player 1
    :param player2_choice: 'S' (Silent/Cooperate) or 'T' (Testify/Defect) for Player 2
    :return: A tuple of (player1_years, player2_years) representing the number of years in prison for each.
    """
    # Outcome matrix: (Player1_choice, Player2_choice) -> (Player1_years, Player2_years)
    outcome_matrix = {
        ('S', 'S'): (1, 1),  # Both stay silent (cooperate)
        ('S', 'T'): (3, 0),  # Player 1 stays silent, Player 2 testifies
        ('T', 'S'): (0, 3),  # Player 1 testifies, Player 2 stays silent
        ('T', 'T'): (2, 2),  # Both testify (defect)
    }

    return outcome_matrix.get((player1_choice, player2_choice), (0, 0))  # Default to (0, 0) if invalid choices

def main():
    if len(sys.argv) != 3:
        print("Usage: python prisoners_dilemma.py <Player1_choice> <Player2_choice>")
        print("<Player1_choice> and <Player2_choice> should be 'S' (Silent) or 'T' (Testify)")
        sys.exit(1)

    player1_choice = sys.argv[1].upper()
    player2_choice = sys.argv[2].upper()

    if player1_choice not in ['S', 'T'] or player2_choice not in ['S', 'T']:
        print("Error: Choices must be 'S' for Silent (Cooperate) or 'T' for Testify (Defect).")
        sys.exit(1)

    player1_years, player2_years = prison_dilemma(player1_choice, player2_choice)

    print(f"Player 1 chooses: {player1_choice}")
    print(f"Player 2 chooses: {player2_choice}")
    print(f"Player 1 will serve: {player1_years} year(s) in prison")
    print(f"Player 2 will serve: {player2_years} year(s) in prison")

if __name__ == "__main__":
    main()
