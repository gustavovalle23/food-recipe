class OnlyImplementationsAbstractMethodsAllowedException(Exception):
    """Exception raised for errors
    when there is an attempt to implement more methods than the super class
    """

    def __init__(self, message="only implementations of abstract methods are allowed"):
        self.message = message
        super().__init__(self.message)
