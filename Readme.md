![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green)
![Pytest](https://img.shields.io/badge/Pytest-Testing-orange)
![Logging](https://img.shields.io/badge/Logging-Built--in-yellow)
![ETL](https://img.shields.io/badge/Data%20Engineering-ETL-purple)
![OOP](https://img.shields.io/badge/Programming-OOP-red)
![Tests](https://img.shields.io/badge/tests-pytest-success)
![Architecture](https://img.shields.io/badge/Architecture-modular-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

* [General info](#general-info)

    <details>
    <summary> 
    Click here to see general information about the Project.
    </summary>
    <b>Simple ETL pipeline written in Python using Object-Oriented Programming.
    The project demonstrates a clean architecture with separation of:
    Data sources

    * Data transformations

    * Data loaders

    * Pipeline orchestration

    * Logging

    * Automated testing </b> 
    </details>

* [Technologies](#technologies)

    <details>
    <summary>
     More details..
    </summary>

    Technologies:

    * Python

    * Pandas

    * Pytest

    * Logging

    * ETL Architecture

    * Object-Oriented Programming (OOP)

    * CSV Data Processing

    </details>


* [Setup](#setup)

    <details>
    <summary>
    More details..
    </summary>

    * Clone repository

        git clone https://github.com/AlexArciszewski/etl-project-oop.git

    * Go to project directory

        cd etl_project

    * Install dependencies

        pip install -r requirements.txt

    * Run application

        python main.py
    </details>


* [Project structure](#project_structure)
    <details>
    <summary>
    More details..
    </summary>

    ```
    etl-project-oop
     │ 
     ├── etl 
     |    ├── logger.py
     |    └── pipeline.py 
     │
     ├── sources
     │    ├── base_source.py 
     │    └── csv_source.py 
     │ 
     ├── transform
     │    ├── base_transformer.py 
     │    └── transformers.py 
     │ 
     ├── loaders
     │    ├── base_loader.py
     │    └── csv_loader.py 
     │ 
     ├── interface
     │    └── menu.py
     │ 
     ├── saved_data
     │ 
     ├── logs
     │ 
     ├── tests
     │     ├── test_csv_loader.py
     │     ├── test_csv_source.py
     │     ├── test_pipeline.py
     │     └── test_transformer.py
     │
     ├── main.py
     │ 
     ├──  pytest.ini
     │
     └── requirements.txt
    ```
    </details>


* [ETL pipeline architecture](#ETL_pipeline)
    <details>
    <summary>
    More details..
    </summary>
    
    Pipeline workflow:
    ```
     +------------+ 
     | Data Source| 
     | (CSV file) |
     +------------+
           | 
           v 
     +------------+
     | Transformer|
     | Data clean |
     | Remove null| 
     | Drop dupes |
     +------------+
           | 
           v 
     +------------+
     |   Loader   | 
     |  Save CSV  |
     +------------+
           | 
           v 
     +------------+
     | Saved Data |
     +------------+

    ```

    </details>


* [More detailed information about modules](#more-detailed-information-about-modules)
    <details>
    <summary>
    More details..
    </summary>

    * Sources:

      Responsible for loading raw data.

        Example:

            CsvSource

    * Transformers:

        Responsible for cleaning and transforming data.

        Operations include:

        * removing duplicates

        * removing missing values

        * removing unnecessary columns

    * Loaders

        Responsible for saving processed data.

        Example:

            CsvLoader

    * Pipeline

        Responsible for orchestrating the ETL process.

        Steps:

            Load data

            Transform data

            Save data

    </details>


* [Application view](#application-view)
    <details>
    <summary>
    More details..
    </summary>

    <img width="1331" height="712" alt="Image" src="https://github.com/user-attachments/assets/7cf5c31a-7cf1-44e0-a266-4b64b50fedfe" />


    </details>


