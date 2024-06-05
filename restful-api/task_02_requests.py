import requests
import csv

def fetch_and_print_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Print the status code
    print(f'Status Code: {response.status_code}')
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response data into JSON
        posts = response.json()
        
        # Print the titles of all posts
        for post in posts:
            print(post['title'])
    else:
        print('Failed to fetch posts')

def fetch_and_save_posts():
    # Fetch posts from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response data into JSON
        posts = response.json()
        
        # Prepare the data for CSV
        data_to_save = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Write data to CSV
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data_to_save)
        
        print('Data has been saved to posts.csv')
    else:
        print('Failed to fetch posts')

# main_02_requests.py content
if __name__ == '__main__':
    fetch_and_print_posts()
    fetch_and_save_posts()
