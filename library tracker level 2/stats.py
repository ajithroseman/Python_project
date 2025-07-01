def show_stat(book):
    if not book:
        print("No book in library")
        return
    total = len(book)
    rating = [b["rating"] for b in book if b.get("rating") is not None]
    ratings = map(int, rating)
    avg_rating = round(sum(ratings) / len(rating), 2) if rating else "N/A"
    print("\n-----Library statistics--------")
    print(f"Total book:{total}")
    print(f"Average rating:{avg_rating}")
