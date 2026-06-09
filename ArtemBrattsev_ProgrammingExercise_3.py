# Name: Artem Brattsev
# Course: COP 2373
# Programming Exercise - Spam Detector


# Stores spam keywords and performs spam analysis.
class SpamDetector:

    # Initialize the spam keyword list.
    def __init__(self):

        self.spam_keywords = [
            "free",
            "winner",
            "won",
            "claim now",
            "limited time",
            "act now",
            "urgent",
            "click here",
            "congratulations",
            "guaranteed",
            "risk free",
            "cash",
            "money",
            "earn",
            "income",
            "credit card",
            "loan",
            "investment",
            "buy now",
            "discount",
            "offer",
            "prize",
            "selected",
            "exclusive",
            "gift",
            "bonus",
            "weight loss",
            "million dollars",
            "no obligation",
            "work from home"
        ]

    # Check email message for spam keywords.
    def check_spam(self, email_message):

        # Accumulator for spam score.
        spam_score = 0

        # Store matching spam words.
        found_words = []

        # Search for each spam keyword.
        for keyword in self.spam_keywords:

            if keyword.lower() in email_message.lower():

                spam_score += 1
                found_words.append(keyword)

        return spam_score, found_words

    # Determine spam rating.
    def get_rating(self, score):

        if score <= 2:
            return "Low likelihood of spam"

        elif score <= 5:
            return "Moderate likelihood of spam"

        else:
            return "High likelihood of spam"


# Main function for the program.
def main():

    print("Spam Email Detector")
    print()

    # Create an object from the SpamDetector class.
    detector = SpamDetector()

    # Get email message from the user.
    email_message = input("Enter an email message: ")

    # Check their message for spam.
    spam_score, found_words = detector.check_spam(email_message)

    # Determine spam rating.
    rating = detector.get_rating(spam_score)

    print()
    print("Spam Score:", spam_score)
    print("Spam Rating:", rating)
    print()

    print("Spam Words/Phrases Found:")

    if len(found_words) == 0:

        print("None")

    else:

        for word in found_words:
            print("-", word)


# Start the program.
main()