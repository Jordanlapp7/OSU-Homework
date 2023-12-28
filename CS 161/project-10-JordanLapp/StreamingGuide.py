# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 6/7/2023
# Description: Created movie, streaming platform, and streaming guide classes to organize where to watch movies.

class Movie:
    """Represents a Movie with a title, genre, director, and year."""
    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """Returns movie title."""
        return self._title

    def get_genre(self):
        """Returns movie genre."""
        return self._genre

    def get_director(self):
        """Returns movie director."""
        return self._director

    def get_year(self):
        """Returns movie year."""
        return self._year


class StreamingService:
    """Represents a streaming service with a name and list of movies."""
    def __init__(self, name):
        self._name = name
        self._catalog = {}

    def get_name(self):
        """Returns streaming service name."""
        return self._name

    def get_catalog(self):
        """Returns streaming service catalog."""
        return self._catalog

    def add_movie(self, movie):
        """Adds a movie to a streaming service's catalog."""
        movie_name = movie.get_title()
        self._catalog[movie_name] = movie

    def delete_movie(self, movie):
        """Deletes a movie from a streaming service's catalog."""
        del self._catalog[movie]


class StreamingGuide:
    """Represents a guide containing all streaming services."""
    def __init__(self):
        self._guide = []

    def add_streaming_service(self, service):
        """Adds streaming service to the guide."""
        self._guide.append(service)

    def delete_streaming_service(self, service):
        """Removes streaming service from the guide."""
        for platform in self._guide:
            platform_name = platform.get_name()
            if service == platform_name:
                self._guide.remove(platform)

    def who_streams_this_movie(self, title):
        """Returns a dictionary with the movie title, year, and streaming services it is on."""
        movie_info = {
            "title": title,
            "services": []
        }
        for service in self._guide:
            catalog = service.get_catalog()
            for movie in catalog:
                if title == movie:
                    movie_year = catalog[movie].get_year()
                    service_name = service.get_name()
                    movie_info["year"] = movie_year
                    movie_info["services"].append(service_name)
        if movie_info["services"]:
            return movie_info
        else:
            return None
