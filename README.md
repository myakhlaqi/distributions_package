<p align="center">
  <a href="" rel="noopener">
 <!-- <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a> -->
</p>

<h3 align="center">dist_gb</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/myakhlaqi/distributions_package/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 
   Guassian and Binomial distribution package
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This initial package is a simple package for doing statistical operation on a dataset.
Currently, this package support two distribution including Guassian and Binomial.
The future contibutions is encouraged to add more functionality in this pakcage.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

To draw the plot you need to install matplotlib. 
There is no more prerequisit for this package.

```
pip install matplotlib
```

### Installing
This package is poblicly available in pypi repository (https://pypi.org/project/dist-gb-akhlaqi/). To install from pypi repository run:
```
pip install dist-gb-akhlaqi
```

To easy install and use this package follow this commands:

#### Clone the package source code into your local system

```
Git clone https://github.com/myakhlaqi/distributions_package.git
```

#### Go to dist_gb directory, run:

```
pip install pyproject.toml
```
The package will be installed under the name "dist_gb:x.x.x" to make sure run:
```
pip list | grep dist
```


## 🔧 Running the tests <a name = "tests"></a>



### Run test

To run the test cases on this package there is a simple test.py file in the
main direcotry. You can add more test case or just run the existing one to 
make sure that the code run error free.

To run the test type:
```
pytest test.py
```


## 🎈 Usage <a name="usage"></a>
How to use examples:
```
import imp
from dist_gb.src import Gaussian

g1= Gaussian()
g1.read_data_file('data.csv')
g1.plot_histogram()
print(g1.calculate_mean())
print(g1.calculate_stdev)
```

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>


## ✍️ Authors <a name = "authors"></a>

- [@myakhlaqi](https://github.com/myakhlaqi)


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- I inspired by the Udacity AWS ML engineering nano-degreee program to write this package.
- Thanks from AWS and Udacity for giving this opportinity
- https://www.udacity.com/scholarships/aws-machine-learning-scholarship-program
