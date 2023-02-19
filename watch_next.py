def watch_next(description):
    # Read the movie descriptions from the file "movies.txt"
    with open('movies.txt', 'r') as file:
        movies = file.readlines()

    # Calculate the similarity between the input description and each movie description
    similarities = []
    for movie in movies:
        similarity = 0
        for word in description.split():
            if word.lower() in movie.lower():
                similarity += 1
        similarities.append(similarity)

    # Get the index of the most similar movie
    index = similarities.index(max(similarities))

    # Return the title of the most similar movie
    return movies[index].strip()
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the aIlluminati trick Hulk into a shuttle nd launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar, where he is sold into slavery and trained as a gladiator."
title = watch_next(description)
print(title)
