# bank_account.py
class BankAccount:
    """A simple BankAccount class demonstrating basic OOP and encapsulation."""

    def __init__(self, initial_balance: float = 0.0):
        # Use a "protected" attribute name to encourage encapsulation.
        try:
            self._account_balance = float(initial_balance)
        except (TypeError, ValueError):
            self._account_balance = 0.0

    def deposit(self, amount: float) -> None:
        """Add amount to account balance. Negative deposits are ignored."""
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Deposit amount must be numeric.")

        if amt <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._account_balance += amt

    def withdraw(self, amount: float) -> bool:
        """
        Attempt to withdraw amount. Returns True on success, False on insufficient funds.
        Negative withdrawals are rejected (ValueError).
        """
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Withdrawal amount must be numeric.")

        if amt <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amt > self._account_balance:
            return False
        self._account_balance -= amt
        return True

    def display_balance(self) -> None:
        """Print the current balance in a friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")

    # Optional convenience: allow read-only access via property
    @property
    def balance(self) -> float:
        return self._account_balance
