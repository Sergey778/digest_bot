import slacker
from typing import List
from datetime import datetime, timedelta


def sort_messages(messages: List[dict], topk: int = 20) -> List[dict]:
    """
    Sort messages by unique and mysterious algorithm and return most important

    :param messages: list of messages from a channel
    :param topk: amount of messages to return from each channel
    :return: sorted messages
    """

    return sorted(messages, key=lambda x: x.get("reply_count", 0), reverse=True)[:topk]


if __name__ == "__main__":
    # get channels list
    ch_info = slacker.get_channels_list()

    for ch_id, ch_name in ch_info:
        print(f"Channel: {ch_name}")

        week_ago = datetime.now() - timedelta(days=7)
        messages = slacker.get_channel_messages(ch_id, week_ago)

        messages = sort_messages(messages)
        messages = slacker.update_permalinks(channel_id=ch_id, messages=messages)

        print(messages)
        print("\n\n")
