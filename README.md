# Laredoute Scraper

This project is a web scraping tool designed to extract vendor information from the La Redoute e-commerce website. It uses **Botasaurus**, a powerful scraping framework, along with **Pixi** for dependency management, to automate the process of navigating the site, handling pop-ups, and scraping specific vendor data.

## Features

* **Extracts Category Links**: Fetches product category links from a sitemap.
* **Scrapes Vendor Information**: Navigates to product pages, identifies the vendor, and extracts detailed information.
* **CSV Output**: Saves scraped category links and vendor data to CSV files for easy use.
* **Automated Setup**: A `Makefile` is included to simplify the setup, ensuring all dependencies are installed correctly.

---

## Prerequisites

Here are the tools and software required to run the project:

* **`make`**: The `make` build tool is essential for running the installation and launch commands defined in the `Makefile`.
* **Python 3.x**: The project is developed in Python. Ensure you have a version 3.x (e.g., 3.9 or newer) installed on your system.
* **`curl` and `apt`**: The installation script is designed for Debian/Ubuntu-based operating systems. Make sure the `curl` and `apt` commands are available.

---

## Installation and Configuration

The project uses `pixi` for dependency management. The provided `Makefile` automates the entire configuration process.

1.  **Open your terminal** and navigate to the project's root directory.
2.  **Execute the `setup` command**: This command will install `curl` (if not already present), `pixi`, and all project dependencies.

    ```bash
    make setup
    ```

> **Note**: If you encounter a "dpkg was interrupted" error during installation, the `Makefile` will automatically attempt to fix it and continue.

---

## Usage

Once the setup is complete, you can launch the script using the `Makefile`.

1.  **Launch the scraper**: This command will execute the Python script that handles the scraping logic.

    ```bash
    make run
    ```

The script will display its progress in the console. The results will be saved in CSV files in your project directory.

2.  **Generate the final "deliverable" file**: Once the intermediate CSV files are ready, you can merge them and create a final output file.

    ```bash
    make livrable
    ```

---

## For Windows Users

The `Makefile` is optimized for Linux and macOS. **Windows** users must first install `make` via an environment like **Git Bash** or **WSL (Windows Subsystem for Linux)**.

Once `pixi` is installed, you can also run the commands directly from your terminal, without using `make`. This is particularly useful if you encounter issues with `make` on Windows.

* **To install dependencies**:
    ```bash
    pixi install
    ```
* **To launch the scraper**:
    ```bash
    pixi run run
    ```
* **To generate the final "deliverable" file**:
    ```bash
    pixi run livrable
    ```

These commands allow you to bypass the `Makefile` and interact directly with **Pixi** to manage the project.