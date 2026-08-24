import requests

from ddgs import DDGS

from langchain_core.tools import tool


def geocode_city(city: str):
    """
    Convert a city name into latitude and longitude.
    """

    url = (
        "https://geocoding-api.open-meteo.com/v1/search"
    )

    response = requests.get(
        url,
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        },
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    results = data.get("results", [])

    if not results:
        return None

    result = results[0]

    return {
        "name": result.get("name"),
        "country": result.get("country"),
        "latitude": result.get("latitude"),
        "longitude": result.get("longitude")
    }


@tool
def calculator(expression: str) -> str:
    """
    Perform a mathematical calculation.

    Use this tool when the user asks for
    mathematical calculations.
    """

    try:

        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return str(result)

    except ZeroDivisionError:

        return (
            "Calculation error: "
            "division by zero is not allowed."
        )

    except Exception as e:

        return f"Calculation error: {str(e)}"


@tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a city.

    Use this tool whenever the user asks about:
    - current weather
    - temperature
    - humidity
    - wind
    - current conditions
    """

    try:

        # Find the city
        location = geocode_city(city)

        if location is None:

            return (
                f"Could not find the city '{city}'. "
                "Please check the spelling."
            )

        # Get coordinates
        latitude = location["latitude"]
        longitude = location["longitude"]

        # Request weather
        url = (
            "https://api.open-meteo.com/v1/forecast"
        )

        response = requests.get(
            url,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "wind_speed_10m"
                ),
                "timezone": "auto"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        current = data["current"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind = current["wind_speed_10m"]

        return (
            f"City: {location['name']}, "
            f"{location['country']}\n"
            f"Temperature: {temperature} °C\n"
            f"Humidity: {humidity}%\n"
            f"Wind speed: {wind} km/h"
        )

    except requests.exceptions.Timeout:

        return (
            "Weather service timed out. "
            "Please try again."
        )

    except requests.exceptions.RequestException:

        return (
            "Weather service is temporarily "
            "unavailable."
        )

    except Exception:

        return (
            "I couldn't retrieve the weather "
            "information."
        )


@tool
def web_search(query: str) -> str:
    """
    Search the web for current or external information.

    Use this tool when:
    - information may have changed
    - the user asks about current people
    - the user asks about companies
    - the user asks about recent events
    - up-to-date information is required

    Do not use this tool for arithmetic
    or weather questions.
    """

    try:

        results = DDGS().text(
            query,
            max_results=5
        )

        if not results:

            return (
                "No search results were found."
            )

        formatted_results = []

        for result in results:

            title = result.get(
                "title",
                ""
            )

            body = result.get(
                "body",
                ""
            )

            url = result.get(
                "href",
                ""
            )

            formatted_results.append(
                f"Title: {title}\n"
                f"Snippet: {body}\n"
                f"URL: {url}"
            )

        return "\n\n".join(
            formatted_results
        )

    except Exception:

        return (
            "Web search is temporarily "
            "unavailable."
        )