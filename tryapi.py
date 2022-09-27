import os
import datetime
from googleapiclient.discovery import build
from art import logo

def get_youtube_data(channel_name):
    """
    This function gets the information of the Youtube Channel requested
    Args:
        channel_name (str): string with the channel name
    Returns:
        statistics (dict): dictionary containing the metrics from the channel
    """
    api_key = os.environ.get("API_KEY")
    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.channels().list(
        part="statistics",
        forUsername=channel_name)
    response = request.execute()
    if "items" in response:
        statistics = response["items"][0]["statistics"]
        return statistics


def format_results(channel_name, results, metric_name="all"):
    """
    Returns a formatted string with the specified metrics
    Args:
        channel_name (str): string with the channel name
        results (dict): dictionary containing the metrics from the channel
        metric_name (str): string that specified the requested metric. Defaults to 'all'
    Returns:
        formatted_text (str): formatted string with the specified metrics
    """
    formatted_text = ""
    subscriber_count = results["subscriberCount"]
    video_count = results["videoCount"]
    view_count = results["viewCount"]
    today = datetime.datetime.now()
    today_text = today.strftime('%A, %d/%m/%Y:')
    subscriber_text = f"{channel_name} - Subscribers count as on {today_text} {subscriber_count}"
    video_text = f"{channel_name} - Videos count as on {today_text} {video_count}"
    view_text = f"{channel_name} - Views count as on {today_text} {view_count}"
    if metric_name == "subscriberCount":
        formatted_text = subscriber_text
    elif metric_name == "videoCount":
        formatted_text = video_text
    elif metric_name == "viewCount":
        formatted_text = view_text
    elif metric_name == "all":
        formatted_text = "\n".join([subscriber_text, video_text, view_text])

    return formatted_text


def print_results(results_text):
    print(results_text)


def save_results(channel_name, results_text):
    with open(f"{channel_name}.txt", "w") as file_results:
        file_results.write(results_text)


def run():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    while True:
        channel_name = input("What is the User name of the Youtube Channel? ")
        results = get_youtube_data(channel_name)
        if not results:
            print("No statistics found")
            return
        metric_name = input("Which metric do you want to see? (subscriberCount / videoCount / viewCount / all) ")
        formatted_results = format_results(channel_name, results, metric_name)
        if not formatted_results:
            print("The metric name you used is not correct!")
        print()
        print_results(formatted_results)
        save_results(channel_name, formatted_results)
        print()
        search_again = input("Do you want to get the information for another Youtube Channel? (y / n) ")
        if search_again == "n":
            break

run()



# guardianwires
# NASAgovVideo
# BBCNews
# NASAKennedy
# ITVNews
# amazonwebservices
