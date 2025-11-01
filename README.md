# Hooray
A simple Python based package manager for a Debian User Repository.

## Features
- Install packages from any repository in the Debian Public User Repository (or external repositories holding .deb files).
- Manage installed packages (install, remove).
## Installation
To install Hooray, clone the repository and run the script file after chmoding it to be executable:
```bash
git clone https://github.com/MOHAPY24/Hooray.git
sudo cp -r Hooray/* /usr/local/bin/
chmod +x /usr/local/bin/hooray
```
Alternatively, you can run it directly without installation:
```bash
git clone https://github.com/MOHAPY24/Hooray.git
cd Hooray
chmod +x hooray
sudo ./hooray <command> <args>
```

## Usage
After installation, you can use Hooray from the command line. Here are some basic commands
- To install a package:
  ```bash
  hooray make <package-name>
  ```
- To remove a package:
  ```bash
  hooray destroy <package-name>
  ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the GPLv3 License. See the LICENSE file for details.

## Disclaimer
This software is provided "as is", without warranty of any kind. Use at your own risk.