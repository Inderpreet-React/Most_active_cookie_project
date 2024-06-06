import argparse
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description="Find the most active cookie for a given day.")
    parser.add_argument('-f', '--file', required=True, help='Path to the cookie log file')
    parser.add_argument('-d', '--date', required=True, help='Date in YYYY-MM-DD format')
    return parser.parse_args()

def read_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def extract_cookie_data(lines, target_date):
    cookie_count = defaultdict(int)
    for line in lines:
        cookie, timestamp = line.strip().split(',')
        date = timestamp.split('T')[0]
        if date == target_date:
            cookie_count[cookie] += 1
    return cookie_count

def find_most_active_cookies(cookie_count):
    if not cookie_count:
        return []

    max_count = max(cookie_count.values())
    most_active_cookies = [cookie for cookie, count in cookie_count.items() if count == max_count]
    return most_active_cookies

def main():
    args = parse_args()
    target_date = args.date

    lines = read_log_file(args.file)
    cookie_count = extract_cookie_data(lines, target_date)
    most_active_cookies = find_most_active_cookies(cookie_count)

    for cookie in most_active_cookies:
        print(cookie)

if __name__ == "__main__":
    main()
