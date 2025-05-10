# 🕵️ Pinkerton
> Investigating JavaScripts files since 1850

<div align="center">
    <img src="https://i.imgur.com/qQXb2ha.png" width=700>
</div>

<br>

<p align="center">
    <img src="https://img.shields.io/github/license/000pp/Pinkerton?color=yellow&logo=github&style=for-the-badge">
    <img src="https://img.shields.io/github/issues/000pp/Pinkerton?color=yellow&logo=github&style=for-the-badge">
    <img src="https://img.shields.io/github/stars/000pp/pinkerton?color=yellow&logo=github&style=for-the-badge">
    <img src="https://img.shields.io/github/forks/000pp/Pinkerton?color=yellow&logo=github&style=for-the-badge">
</p>

___

<br>

<p>Python project to crawl for JavaScript files and search for secrets like API keys, authorization tokens, hardcoded password or related.</p>

<br>

## ⚡ Getting started

<p> A quick guide of how to install and use Pinkerton. </p>

1. Clone the repository with: `git clone https://github.com/000pp/pinkerton.git`
2. Install the libraries with: `pip3 install -r requirements.txt --break-system-packages`
3. Run Pinkerton with: `python3 main.py -u https://example.com`

<br>

### 🐳 Docker

If you want to use pinkerton in a Docker container, follow this commands:

```
1. Clone the repository - git clone https://github.com/000pp/pinkerton.git
2. Build the image - sudo docker build -t pinkerton:latest .
3. Run container - sudo docker run pinkerton:latest
```

<br>

### ⚫ BlackArch

```
pacman -Syu pinkerton
```

<br><br>

## 🔨 Contributing

A quick guide of how to contribute with the project.

1. Create a fork from Pinkerton repository
2. Clone the repository with `git clone https://github.com/your/pinkerton.git`
3. Type `cd pinkerton/`
4. Create a branch and make your changes
5. Commit and make a git push
6. Open a pull request

<br><br>

## 🙏 Credits

- [m4ll0k (SecretFinder creator)](https://github.com/m4ll0k) for the regex patterns
- [h33lit (Jubaer Alnazi)](https://github.com/h33tlit) for the regex patterns
- [zricethezav (GitLeaks creator)](https://github.com/zricethezav/gitleaks) for the regex patterns

<br><br>

## ⚠️ Warning

- The developer is not responsible for any malicious use of this tool.
