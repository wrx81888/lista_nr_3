import subprocess
import json

def send_request(url):
    result = subprocess.run(['curl', '-s', '-w', '%{http_code}', url], stdout=subprocess.PIPE)
    response_body = result.stdout[:-3].decode('utf-8')
    http_status_code = int(result.stdout[-3:].decode('utf-8'))
    return response_body, http_status_code

def check_status_code(http_status_code):
    return http_status_code == 200

def check_json_keys(response_json, keys):
    return all(key in response_json for key in keys)

def test_endpoint(url, expected_keys):
    response_body, http_status_code = send_request(url)
    try:
        response_json = json.loads(response_body)
    except json.JSONDecodeError:
        response_json = {}
    
    if check_status_code(http_status_code) and check_json_keys(response_json, expected_keys):
        return "PASSED"
    else:
        return "FAILED"

def main():
    tests = [
        {
            'url': 'https://jsonplaceholder.typicode.com/posts/1',
            'keys': ['userId', 'id', 'title', 'body']
        },
        {
            'url': 'https://jsonplaceholder.typicode.com/comments/1',
            'keys': ['postId', 'id', 'name', 'email', 'body']
        },
        {
            'url': 'https://jsonplaceholder.typicode.com/users/1',
            'keys': ['id', 'żeby wyszło FAILED', 'username', 'email']
        }
    ]

    for i, test in enumerate(tests):
        result = test_endpoint(test['url'], test['keys'])
        print(f"Test {i + 1}: {result}")

if __name__ == "__main__":
    main()
