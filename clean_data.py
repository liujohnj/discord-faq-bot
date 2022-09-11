import csv, webbrowser, os, re

""" Script to preprocess and clean training data"""

with open("cleaned_data.csv", 'w', newline='') as write_file:
    csv_writer = csv.writer(write_file)
    with open('original_data.csv') as read_file:
        reader = csv.reader(read_file)
        posts = list(reader)

        for post in posts:
            # remove line breaks
            if '\n' in post[0]:
                chat = (','.join(post[0].splitlines()))
            else:
                chat = post[0]

            # remove non-ASCII characters
            new_chat = chat.encode("ascii", "ignore")
            updated_chat = new_chat.decode()

            # remove URLs
            updated_chat = re.sub(r'http\S+', '', updated_chat)

            # remove Discord usernames
            updated_chat = re.sub(r'<@\S+', '', updated_chat)

            if updated_chat:
                row = [updated_chat, post[1]]
                csv_writer.writerow(row)


    # remove duplicate chat content (e.g., "Thanks!")
    d = {}

    with open('cleaned_data.csv') as read_file:
        reader = csv.reader(read_file)
        posts = list(reader)

        for post in posts:
            if post[0] not in d:
                d[post[0]] = post[1]

    with open("deduped_cleaned_data.csv", 'w', newline='') as write_file:
        csv_writer = csv.writer(write_file)

        for key, value in d.items():
            row = [key, value]
            csv_writer.writerow(row)