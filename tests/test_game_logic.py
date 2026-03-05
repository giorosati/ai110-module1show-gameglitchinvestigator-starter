from logic_utils import check_guess


# FIXME -  these three tests compare a tuple to a string
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Tests targeting the reversed hint message bug ---
# The original bug: when guess > secret, the message said "Go HIGHER!" (wrong),
# and when guess < secret, it said "Go LOWER!" (wrong). Both were swapped.

def test_too_high_message_says_go_lower():
    """Guess above secret must tell the player to go LOWER, not higher."""
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, (
        f"Expected hint to say 'LOWER' when guess is too high, got: '{message}'"
    )
    assert "HIGHER" not in message

def test_too_low_message_says_go_higher():
    """Guess below secret must tell the player to go HIGHER, not lower."""
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, (
        f"Expected hint to say 'HIGHER' when guess is too low, got: '{message}'"
    )
    assert "LOWER" not in message
