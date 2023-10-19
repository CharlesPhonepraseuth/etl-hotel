# ETL Hotel pipeline

Written by [Charles Phonepraseuth](https://www.linkedin.com/in/charlesphonepraseuth/)

This document covers everything and provide an overview about this ETL pipeline project.

# Table of Contents

- [ETL Hotel pipeline](#etl-hotel-pipeline)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Prerequisite](#prerequisite)
- [Installation](#installation)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Create logs folder](#step-2-create-logs-folder)
  - [Step 3: Configure Environment Variables](#step-3-configure-environment-variables)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Step 1: Build and Start the Docker Containers](#step-1-build-and-start-the-docker-containers)
  - [Step 2: Access the project](#step-2-access-the-project)
  - [Step 3: Run pipeline](#step-3-run-pipeline)
- [Workflow](#workflow)
- [Running tests](#running-tests)
- [CI/CD Pipeline with Unit Tests](#cicd-pipeline-with-unit-tests)
- [Git Hooks for Pre-commit Checks](#git-hooks-for-pre-commit-checks)
- [Stop and Cleanup](#stop-and-cleanup)
- [Disclaimer](#disclaimer)
- [Contact Information](#contact-information)

# <a id="introduction"></a>Introduction

In the ever-evolving landscape of data-driven decision-making, the ability to harness, transform, and analyze data from diverse sources has become paramount. This data engineering project embarks on this journey by orchestrating an Extract, Transform, Load (ETL) pipeline to seamlessly integrate data from two disparate sources: accommodations and addresses.

Accommodations data, such as hotel listings, ratings and room  details, often reside in one source, while address data, encompassing geographical coordinates, zip codes, and city names, may be found in another. The challenge at hand is to merge these distinct data sets into a unified format that can be effortlessly loaded into a database for in-depth analysis.

----

# <a id="prerequisite"></a>Prerequisite

This ETL (Extract, Transform, Load) pipeline project is designed to be easily deployable through Docker containers. With Docker, you can encapsulate all the necessary components and dependencies, ensuring a consistent and hassle-free setup.

Before you begin, ensure that you have Docker installed on your system. If you haven't installed Docker yet, you can download it from [Docker's official website](https://www.docker.com/get-started/).

----

# <a id="installation"></a>Installation

Provide clear, step-by-step instructions on how to install your ETL pipeline. Include commands, scripts, or any installation tools used.

## Step 1: Clone the Repository

First, clone the ETL pipeline repository to your local machine:

```sh
git clone https://github.com/CharlesPhonepraseuth/etl-hotel.git
cd etl-hotel
```

## Step 2: Create logs folder

To use Airflow correctly, you have to create logs folder into pipeline.

```sh
cd etl-hotel/app/pipeline
mkdir logs
```

## Step 3: Configure Environment Variables

Copy and paste `.env-example` file and rename it `.env` into root directory with the same values or yours.

----

# <a id="project-structure"></a>Project Structure

```
📂 root
└── 📁 .github                      # Github Actions scripts
│   └── 📁 workflows
└── 📁 app                          # Project code
│   └── 📁 config                   # Configuration files
│   └── 📁 api                      # Custom API scripts
│   │   └── 📁 controllers          # API controller scripts
│   └── 📁 dashboard                # Dash application scripts for visualization and analysis
│   │   └── 📁 assets               # Static files like images, stylesheets, and JavaScript files
│   │   └── 📁 callbacks            # Dash callback scripts
│   │   └── 📁 views                # Dash layout scripts
│   │       └── 📁 partials         # Dash common layout scripts
│   └── 📁 data                     # Raw and processed data files
│   │   └── 📁 external             # Data from external sources
│   │   │   └── 📁 accommodations
│   │   │   └── 📁 adress
│   │   │       └── 📁 csv
│   │   │       └── 📁 gz
│   │   └── 📁 processed            # Final data used for loading and analysis
│   └── 📁 docs                     # Project documentation
│   └── 📁 etl                      # ETL (Extract, Tranform, Load) scripts
│   │   └── 📁 extract
│   │   └── 📁 load
│   │   └── 📁 transform
│   └── 📁 pipeline                 # Data pipeline orchestration scripts (Airflow)
│   │   └── 📁 dags
│   │   └── 📁 logs
│   │   └── 📁 plugins
│   └── 📁 src                      # Source code for the project
│   │   └── 📁 data                 # Data processing and transformation scripts
│   │   └── 📁 sql_scripts          # SQL scripts
│   │   └── 📁 utils                # Utility scripts and helper functions
│   │   └── 📁 validation           # Data validation and quality assurance scripts
│   │       └── 📁 validator
│   └── 📁 tests                    # Unit and integration scripts
│       └── 📁 test_files           # Mock test files
│       └── 📁 unit
└── 📁 docker                       # Define Docker container files
│   └── 📁 airflow
│   └── 📁 api
│   └── 📁 dashboard
│   └── 📁 postgres
│   └── 📁 tests
├── 📄 .env-example                 # Environment variables example
├── 📄 .gitignore                   # Git ignore rules
├── 📄 clear.sh                     # Project clear commands 
├── 📄 docker-compose.yml           # Define multi-container applications
├── 📄 README.md                    # Project overview and instructions
└── 📄 setup.sh                     # Project setup commands
```

----

# <a id="usage"></a>Usage

The Dockerized ETL (Extract, Transform, Load) pipeline simplifies the process of data extraction, transformation, and loading. In this section, I'll guide you through the steps to effectively utilize the ETL pipeline within your Docker environment.

## Step 1: Build and Start the Docker Containers

To build and start the Docker containers, execute the following command from the project directory:

```sh
# first of all build containers
./setup.sh build
# then run it
./setup.sh start
```

This command will download the necessary Docker images, create containers, and start the ETL pipeline components.

## Step 2: Access the project

Once the containers are up and running, you can access the ETL pipeline via the provided endpoints or interfaces. For example:

- Airflow UI: [http://localhost:8080](http://localhost:8080)
- pgAdmin UI: [http://localhost:5050](http://localhost:5050)
- Dash UI: [http://localhost:8050](http://localhost:8050)
- FastAPI UI: [http://localhost:8000/docs](http://localhost:8000/docs)

> **Note:** You'll find each credentials inside the `.env` file.  
> **Note\*:** To properly use Dash app, you'll have to run and finish ETL pipeline first.

## Step 3: Run pipeline

It's a personal choice to not run pipeline when starting Airflow container. To launch it, once you've accessed to Airflow UI, you can start it by yourself.

----

# <a id="workflow"></a>Workflow

![workflow](./app/docs/assets/workflow.gif)

For more details: [Technical Documentation](./app/docs/technical-doc.md)

----

# <a id="running-tests"></a>Running tests

Because of the following code:

```yml
# docker-compose.yml (tests container)
command: ["sh", "-c", "pytest --color=yes -v $$TEST_FOLDER"]
```

`$$TEST_FOLDER` allow us to run pytest into specific folder. If not define, it will run into each folder.  

Once `tests` container is build, you can run the following command to run test:

```sh
# test every folder
docker compose run tests
# test unit folder
docker compose run -e TEST_FOLDER=tests/unit tests
```

----

# <a id="cicd-pipeline-with-unit-tests"></a>CI/CD Pipeline with Unit Tests

Firstly, we have to create Github secrets and declare each environment variables from .env file, otherwise, the process will failed. To set it in your repository's settings, you can navigate to `Settings > Secrets and variables > Actions > Add repository secret`.  

This repository includes an automated CI/CD pipeline that runs unit tests on each push. The pipeline is configured using GitHub Actions and executes the following steps:

<details>
  <summary><b>Workflow Configuration Code:</b></summary>

It will declare the worklow name and will triggered on every push to any branch.

```yml
name: Unit Test Check On Push

on:
  push:
    branches:
      - '*'
```

</details>

<details>
  <summary><b>Steps Code:</b></summary>

  <details>
    <summary><b>1 - Checkout Repository</b></summary>

  This step ensures that the latest code from the repository is available for the subsequent tasks.

  ```yml
  - name: Checkout repository
    uses: actions/checkout@v2
  ```

  </details>

  <details>
    <summary><b>2 - Create .env File</b></summary>

  To make next step works, the process need environment variables for Docker.  
  To do it securely, the pipeline creates a .env file with the required environment variables, sourced from GitHub secrets.

  ```yml
  - name: Create .env file
    run: |
      # Add environment variables to .env file
      echo "LOCALHOST_IP=${{ secrets.LOCALHOST_IP }}" > .env
      # Add other variables similarly...
  ```

  </details>

  <details>
    <summary><b>3 - Build Docker Images</b></summary>

  This step builds Docker images, including the test container.

  ```yml
  - name: Build Docker Images
    run: |
      echo --- Building images and starting up docker ---
      docker compose build tests
      echo --- Tests container builded —--
  ```

  </details>

  <details>
    <summary><b>4 - Run Docker Container</b></summary>

  This step executes the tests inside a Docker container.

  ```yml
  - name: Run Docker Container
    run: |
      echo --- Running test cases ---
      docker compose run -e TEST_FOLDER=tests/unit tests
      echo --- Completed test cases ---
  ```

  </details>

</details>

</br>

If we want to be proactive and run pytest before `push`, we can do it on each `commit` by using Git Hooks as shown on the next part.

----

# <a id="git-hooks-for-pre-commit-checks"></a>Git Hooks for Pre-commit Checks

In addition to the CI/CD pipeline, we can implement Git hooks for pre-commit checks. This hook will ensure that tests pass before allowing a commit.  

The pre-commit checks are defined in `.git/hooks/pre-commit`.  

<details>
  <summary><b>File content:</b></summary>

```sh
#!/bin/bash

# Run pytest
docker-compose build tests
docker-compose run -e TEST_FOLDER=tests/unit tests

# If tests pass, allow the commit
if [ $? -eq 0 ]; then
  exit 0
else
  echo "Tests failed. Commit aborted."
  exit 1
fi
```

</details>

</br>

Make sure to make this script executable using `chmod +x .git/hooks/pre-commit`.  

To create the `pre-commit` file, you can run the following code:

<details>
  <summary><b>Code:</b></summary>

```sh
cd etl-hotel
echo '#!/bin/bash\n\ndocker-compose build tests\ndocker-compose run -e TEST_FOLDER=tests/unit tests\n\nif [ $? -eq 0 ]; then\n  exit 0\nelse\n  echo "Tests failed. Commit aborted."\n  exit 1\nfi' > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

</details>

</br>

Consequently, this hook will automatically run each time you attempt to make a commit.

----

# <a id="stop-and-cleanup"></a>Stop and Cleanup

When you've completed your data analysis and ETL operations, you can stop and clean up the Docker containers to conserve ressources with the following command:

```sh
# to stop containers
./clear.sh stop
# to cleanup docker and free up ressources
./clear.sh cleanup
```

----

# <a id="disclaimer"></a>Disclaimer

In the course of developing this project, it is important to note that certain decisions were made based on the specifications and capabilities of the development environment. The system utilized for development may have specific limitations that influenced the choice of tools, libraries, and methodologies.

> The following is my personal computer specs:
>
> - **Model**: MacBook Pro (early 2013)
> - **Processor**: 3.0GHz dual-core Intel Core i7
> - **Memory**: 8GB of 1600MHz DDR3L onboard memory

Due to hardware or software constraints, certain options or features may not have been available or feasible within the given context. As a result, alternative approaches were implemented to ensure the successful completion of the project.

For more details: [Limitations](./app/docs/technical-doc.md#limitations)

----

# <a id="contact-information"></a>Contact Information

If you have questions, need assistance, or would like to provide feedback, please feel free to contact us using the following channels:

Email: charles.phonepraseuth@gmail.com  
GitHub: [CharlesPhonepraseuth](https://github.com/CharlesPhonepraseuth)  
LinkedIn: [Charles Phonepraseuth](https://www.linkedin.com/in/charlesphonepraseuth/)

I value your input and am here to assist you. Don't hesitate to reach out!
