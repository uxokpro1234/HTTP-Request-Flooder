# HTTP Request Flooder

A Python script that generates a large number of concurrent HTTP requests against a specified URL.

> **Warning:** This script can generate excessive traffic and potentially disrupt or make a service unavailable. Use it only against systems you own or have explicit authorization to test.

## Features

* Generates random User-Agent strings.
* Accepts a target URL interactively.
* Sends `GET`, `POST`, and `HEAD` requests.
* Uses multiple concurrent threads.
* Continuously sends requests until the process is terminated.

## Requirements

Python 3 and the following packages:

```bash
pip install requests user-agent
```

## Usage

Run the script:

```bash
python script.py
```

Enter a URL when prompted:

```text
[+] Url: https://example.com
```

The program then starts multiple worker threads that continuously send HTTP requests to the specified URL.

## How It Works

The script creates five User-Agent strings and stores them in a list. It then creates a shared HTTP header and starts 800 threads.

Each thread executes an infinite loop:

```text
GET request
POST request
HEAD request
repeat
```

Consequently, the program can generate a substantial amount of traffic from a single machine.

## Limitations

* The User-Agent is selected when the headers are created rather than randomized for every request.
* There is no request timeout.
* There is no rate limiting.
* Threads run indefinitely.
* 800 threads can consume significant system resources.
* The POST requests do not contain a request body.

## Responsible Use

Use this code only for **authorized load/stress testing**, such as testing infrastructure you control or systems where you have written permission to perform testing.

Do not use it to disrupt third-party websites, services, or networks.

## License

Use and modify this code responsibly and in accordance with applicable laws and the authorization requirements of the systems being tested.
