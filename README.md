# File Uploader Project

This project is a simple file uploader application that allows users to upload files through a graphical user interface (GUI) and transfer them over a local area network (LAN) to other computers running the same application.

## Project Structure

```
file-uploader
├── src
│   ├── app.py          # Main entry point of the application
│   ├── gui
│   │   └── interface.py # GUI logic for file uploading
│   ├── network
│   │   └── transfer.py  # Network communication for file transfers
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Requirements

To run this project, you need to install the following dependencies:

- Flask
- Any other necessary libraries (to be specified in requirements.txt)

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/file-uploader.git
   ```

2. Navigate to the project directory:
   ```
   cd file-uploader
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Open your web browser and go to `http://localhost:5000` to access the file uploader interface.

3. Use the interface to select files and upload them. The files will be sent over the LAN to other computers running the application.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.