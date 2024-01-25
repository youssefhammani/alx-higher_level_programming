# Project: 0x10 Python Network

## Description

This project focuses on Python Network tasks involving cURL and Bash scripting. It covers various HTTP concepts, including URL, HTTP methods, headers, and more.

## Learning Objectives

By the end of this project, you should be able to explain:

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for an HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## Tasks

1. **cURL Body Size**

   - Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

   ```bash
   ./0-body_size.sh 0.0.0.0:5000
   ```

2. **cURL to the End**

   - Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response for a 200 status code.

   ```bash
   ./1-body.sh 0.0.0.0:5000/route_1
   ```

3. **cURL Method**

   - Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

   ```bash
   ./2-delete.sh 0.0.0.0:5000/route_3
   ```

4. **cURL Only Methods**

   - Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

   ```bash
   ./3-methods.sh 0.0.0.0:5000/route_4
   ```

5. **cURL Headers**

   - Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response with a specific header.

   ```bash
   ./4-header.sh 0.0.0.0:5000/route_5
   ```

6. **cURL POST Parameters**

   - Write a Bash script that takes in a URL, sends a POST request to the URL with specific parameters, and displays the body of the response.

   ```bash
   ./5-post_params.sh 0.0.0.0:5000/route_6
   ```

7. **Find a Peak**

   - Write a Python function that finds a peak in a list of unsorted integers.

   ```bash
   python3 6-main.py
   ```

8. **Only Status Code (Advanced)**

   - Write a Bash script that sends a request to a URL passed as an argument and displays only the status code of the response.

   ```bash
   ./100-status_code.sh 0.0.0.0:5000
   ```

9. **cURL a JSON File (Advanced)**

   - Write a Bash script that sends a JSON POST request to a URL passed as the first argument, using the contents of a file as the body of the request.

   ```bash
   ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0
   ```

10. **Catch Me If You Can! (Advanced)**

    - Write a Bash script that makes a request to 0.0.0.0:5000/catch_me, causing the server to respond with a message in the body of the response.

    ```bash
    ./102-catch_me.sh
    ```

## Requirements

- All scripts are tested on Ubuntu 20.04 LTS.
- Bash scripts should be exactly 3 lines long.
- Python scripts should use Python 3.8.5.
- Follow the specified format for headers, comments, and documentation.

## Author

Youssef Hammani - [GitHub Profile](https://github.com/youssefhammani)