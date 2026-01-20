# 2. Create a class with the following attributes:
# •  title
# •  author
# •  list of reviews
# And add methods to:
# •  add a new review
# •  count reviews
# •  display all reviews


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        for review in self.reviews:
            print(review)


book = Book("The Great Gatsby", "F. Scott Fitzgerald")
book.add_review("A masterpiece of 20th-century literature.")
book.add_review("An intriguing exploration of the American Dream.")
print("Number of reviews:", book.count_reviews())
book.display_reviews()
