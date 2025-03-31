# Python File Server

A simple Python file server that allows you to host and serve files over the network.

## Prerequisites

Before running the file server, ensure you have the following:

- Python 3.x installed on your system
- Basic knowledge of command-line usage

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Thenewchicken55/PyFileServer.git
   ```

# Python File Server

A simple Python file server that allows you to host and serve files over the network.

## Prerequisites

Before running the file server, ensure you have the following:

- Python 3.x installed on your system
- Basic knowledge of command-line usage

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Thenewchicken55/PyFileServer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd PyFileServer
   ```


3. Create the `files` directory to store files:
   ```bash
   mkdir files
   ```


## Running the Server

You can run the server using one of the following methods:

### Using Python
   ```bash
   python fileServer.py
   ```


### Using Make
   ```bash
   make run
   ```


The server will start, and you can access it via your browser or another client by navigating to ```
http://<local-ip>:<port>```
.

## Features

- Simple setup
- Allows easy file hosting within a specified directory
- Works seamlessly on local networks

## Troubleshooting

- Ensure the firewall settings on your system allow incoming connections on the server's port.
- Verify that the client device and server are on the same network.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes and push:
   ```bash
   git commit -m "Add feature"
   ```

   ```bash
   git push origin feature-name
   ```

4. Create a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).
