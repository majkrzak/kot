[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!--
  <a href="https://github.com//majkrzak/kot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  -->

  <h3 align="center">Kot</h3>

  <p align="center">
    Packing tool made simple
    <br />
    <br />
    <a href="https://github.com/majkrzak/kot/issues">Report Bug</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)



## About The Project

Project aims for simpler packing than Gradle is currently doing. 

## Getting Started

This is example how you can get started with this tool.

Make sure you have python installed.

```sh
sudo apt install python3 pip -yqq
```

### Installation

Clone and install with pip.


## Usage

Create example configuration, like bellow and run the script.

```json
{
  "name": "my_project",
  "dependencies": [
    "org.jetbrains.kotlin:kotlin-stdlib:1.3.50",
    "org.jetbrains.kotlin:kotlin-reflect:1.3.50",
    "org.jetbrains.kotlinx:kotlinx-coroutines-core:1.3.2",
    "org.koin:koin-core:2.0.1"
  ],
  "modules": {
    "simple":[],
    "complex": [
        "simple"
    ]
  }
}
```


## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- Links -->
[contributors-shield]: https://img.shields.io/github/contributors/majkrzak/kot.svg?style=flat-square
[contributors-url]: https://github.com/majkrzak/kot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/majkrzak/kot.svg?style=flat-square
[forks-url]: https://github.com/majkrzak/kot/network/members
[stars-shield]: https://img.shields.io/github/stars/majkrzak/kot.svg?style=flat-square
[stars-url]: https://github.com/majkrzak/kot/stargazers
[issues-shield]: https://img.shields.io/github/issues/majkrzak/kot.svg?style=flat-square
[issues-url]: https://github.com/majkrzak/kot/issues
[license-shield]: https://img.shields.io/github/license/majkrzak/kot.svg?style=flat-square
[license-url]: https://github.com/majkrzak/kot/blob/master/LICENSE
