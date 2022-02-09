<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/RSWilson1/angolan">
    <img src="images/logo.jpg" alt="University of Manchester logo" width="80" height="80">
  </a>

<h3 align="center">Team Angolan, Project Dashboard </h3>

  <p align="center">
    This is an interactive dashboard to visualise and search the Open Prescribing Dataset.
    <br />
    <a href="https://github.com/RSWilson1/angolan"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/RSWilson1/angolan">View Demo</a>
    ·
    <a href="https://github.com/RSWilson1/angolan/issues">Report Bug</a>
    ·
    <a href="https://github.com/RSWilson1/angolan/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Angolan Dashboard][product-screenshot]](http://127.0.0.1:5000/dashboard/home/)

This is an interactive dashboard to visualise and search the Open Prescribing Dataset.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org)
* [Flask](https://flask.palletsprojects.com/)
* [SQLalchemy](https://www.sqlalchemy.org)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Python3 and Anaconda should be installed before proceeding.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/RSWilson1/angolan.git
   ```
2. Install packages
   ```sh
   conda install --conda-forge flask
   conda install --conda-forge sqlalchemy
   ```
3. Run with
   ```sh
   python run.py
   ```


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Our dashboard contains a subset of the open prescribing dataset with tiles which show the total items in the dataset, average actual cost for the NHS, the highest quantity drug at one PCT and the number of unique drugs.

[![Angolan Dashboard][product-screenshot]](http://127.0.0.1:5000/dashboard/home/)

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Calculator for creatine metabolism
- [ ] Infection treatment drug as % of all infection treatments

See the [open issues](https://github.com/RSWilson1/angolan/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Angolan team - [@Angolan](https://twitter.com/Angolan) - angolan@manchester_client.com

Project Link: [https://github.com/RSWilson1/angolan](https://github.com/RSWilson1/angolan)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Alan Davies]()



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/RSWilson1/angolan.svg?style=for-the-badge
[contributors-url]: https://github.com/RSWilson1/angolan/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/RSWilson1/angolan.svg?style=for-the-badge
[forks-url]: https://github.com/RSWilson1/angolan/network/members
[stars-shield]: https://img.shields.io/github/stars/RSWilson1/angolan.svg?style=for-the-badge
[stars-url]: https://github.com/RSWilson1/angolan/stargazers
[issues-shield]: https://img.shields.io/github/issues/RSWilson1/angolan.svg?style=for-the-badge
[issues-url]: https://github.com/RSWilson1/angolan/issues
[license-shield]: https://img.shields.io/github/license/RSWilson1/angolan.svg?style=for-the-badge
[license-url]: https://github.com/RSWilson1/angolan/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/Screenshot.png