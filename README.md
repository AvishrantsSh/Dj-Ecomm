<p align="center">
  <!-- <a href="https://github.com/AvishrantsSh/Django-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h1 align="center">Template Django E-commerce Website</h1>

  <p align="center">
    An awesome way to kickstart your Django projects!
    <br>
    <a href="https://github.com/AvishrantsSh/Django-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/AvishrantsSh/Django-Template/issues">Request Feature</a>
  </p>
</p>
<br>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<br>
<!-- TABLE OF CONTENTS -->

## Table of Contents
<ol>
  <li>
    <a href="#about-the-project">About The Project</a>
  </li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
      <li><a href="#installation">Installation</a></li>
    </ul>
  </li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#license">License</a></li>
</ol>

<!-- ABOUT THE PROJECT -->
## About The Project

Our projects integrates local vendors to create a reliable network for local community of a particular city.
Our aim is to make the entire process of taking a business online, simpler for the local sellers. The flexible backend allows the site to form various clusters based on location, seller, product range etc. 

We focus on personalization of a seller's online shop. To avoid getting lost in the crowd, our objective is to maintain the relationship between the seller and the buyer amidst the pandemic. The seller can expand at his own comfort, while the buyer is displayed the seller based on his location. The buyer can either opt for a delivery service or a drive through to keep up the pre-ordered items to maintain social distancing. 

Our website is an easy to use for both the seller and the buyer. Navigation, search, flexible back-end, progressive web app, responsiveness and most importantly the simplicity of the website is what makes us unique. After the campaign is over, we plan to integrate the up-coming features and implement it for a particular town to drive in the traffic through digital marketing and make it the first E-town in India.

Current Website Link: [EnigmaCommerce](https://enigmacommerce.herokuapp.com/) (Currently Inactive)

Managing your Django project and all its dependencies can be a nightmare. This also includes working in virtual environments, securing your `SECRET KEY`, adding files to `.gitignore` and what not.

Why not simplify this tedious and repetetive work? 

With this objective in mind, I created `Django Template`, a simple and minimalistic django project template that fits all your requirements. 


<!-- GETTING STARTED -->
## Getting Started

Simply click on [Use this template](https://github.com/AvishrantsSh/Django-Template/generate) button on top to get started. Go ahead and choose a cool name for your project. Clone the newly created repository and continue with the following steps.

### Prerequisites

This project is optimized to run on Linux Environments. Tests for Windows and Mac are still in progress.

### Installation

After getting a local copy on your system, run the following commands.

1. To build your django project, run
    ```sh
    make project
    ```
    A prompt will ask you to enter a valid project name before continuing. This command will setup your virtual environment, secret keys and all the basic dependencies required by a django project.

    Alternatively, if you prefer a finer control over your project creation,you can use the following commands
    - Install all project dependencies and create virtual environment
        ```sh
        make install
        ```

    - Make django project using `django-admin`
        ```sh
        django-admin startproject --template=./etc/structure ${project-name} .
        ```
    

    _Note: This directory will now function as your root django folder. Upon creation of a project, a folder named `${project-name}` and `manage.py` will appear at the root._

2. Apply database migrations
    ```sh
    make migrate
    ```

<!-- USAGE EXAMPLES -->
## Usage

You can use `make` commands to perform various operations on your django project.
1. Start django server on port `8000`. You can customize it by editing `PORT` in `Makefile`. 
    ```sh
    make run
    ```

2. Apply database migrations
    ```sh
    make migrate
    ```

3. Clear database records.
    ```sh
    make flush
    ```
     _Note: Media files will not be deleted using this command_

4. Update project requirements (useful for deployment)
    ```sh
    make freeze
    ```

5. Check for proper formatting and import style using `black` and `isort`
    ```sh
    make format
    ```

_Note: This is just a subset of most common commands used while working with django. To use other commands as well, activate the virtual environment using_
```sh
. bin/activate
```

_To deactivate the environment, simply use `deactivate` command_
```sh
deactivate
```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AvishrantsSh/Django-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/AvishrantsSh/Django-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AvishrantsSh/Django-Template.svg?style=for-the-badge
[forks-url]: https://github.com/AvishrantsSh/Django-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/AvishrantsSh/Django-Template.svg?style=for-the-badge
[stars-url]: https://github.com/AvishrantsSh/Django-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/AvishrantsSh/Django-Template.svg?style=for-the-badge
[issues-url]: https://github.com/AvishrantsSh/Django-Template/issues
[license-shield]: https://img.shields.io/github/license/AvishrantsSh/Django-Template.svg?style=for-the-badge
[license-url]: https://github.com/AvishrantsSh/Django-Template/blob/main/LICENSE
