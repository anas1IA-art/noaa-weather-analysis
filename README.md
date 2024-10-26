# NOAA Weather Data Analysis Project

## Overview
This project analyzes historical weather data from NOAA's National Climatic Data Center (NCDC) to identify temperature trends for specific weather stations. The project implements a MapReduce algorithm using Hadoop to process large-scale weather data, followed by visualization and analysis using PowerBI.

## Project Architecture
```
Weather Data Pipeline:
NOAA Data Source → Data Collection Script → HDFS Storage → MapReduce Processing → NoSQL/CSV Storage → PowerBI Analytics
```

## Technical Stack
- **Big Data Processing**: Apache Hadoop, MapReduce
- **Programming Language**: Java (for MapReduce), Python (for data collection)
- **Data Storage**: HDFS, NoSQL Database/CSV
- **Visualization**: PowerBI
- **Version Control**: Git
- **Build Tool**: Maven

## Project Structure
```
noaa-weather-analysis/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   ├── com/weather/
│   │   │   │   ├── MeteoMap.java
│   │   │   │   ├── MeteoReduce.java
│   │   │   │   └── MeteoMain.java
│   │   └── resources/
├── scripts/
│   └── data_collector.py
├── config/
│   └── hadoop-config.xml
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   └── station_info.md
├── notebooks/
│   └── data_analysis.ipynb
├── pom.xml
├── .gitignore
└── README.md
```

## Prerequisites
- Java JDK 8+
- Apache Hadoop 3.x
- Python 3.x
- PowerBI Desktop
- Git

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/anas1IA-art/noaa-weather-analysis.git
   cd noaa-weather-analysis
   ```

2. Configure Hadoop environment:
   - Ensure Hadoop is properly installed and configured
   - Set HADOOP_HOME environment variable
   - Verify Hadoop cluster is running

3. create an envirment conda :
   ```bash
    conda create --name noaa_weather_analysis python=3.12
     ```
4. Activate the newly created environment:
    ```bash
    conda activate noaa_weather_analysis
      ```

5. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```




6. Build the MapReduce application:
   ```bash
   mvn clean package
   ```

## Project Phases

### Phase 1: Data Collection
- Select a Moroccan weather station
- Develop Python script to download historical weather data
- Implement error handling and logging
- Store raw data in HDFS

### Phase 2: MapReduce Implementation
- Develop MapReduce classes for temperature analysis
- Process weather data to extract temperature trends
- Implement data validation and cleaning
- Generate annual temperature statistics

### Phase 3: Data Storage & Visualization
- Store processed data in NoSQL/CSV format
- Create PowerBI connection
- Develop statistical analysis dashboard
- Implement seasonal trend visualization

## Learning Outcomes
- Big Data processing concepts and architectures
- Hadoop ecosystem and HDFS
- MapReduce programming paradigm
- Data pipeline development
- ETL processes
- Data visualization best practices
- Version control with Git
- Project documentation
- Statistical analysis and interpretation

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments
- NOAA for providing the weather data
- National Climatic Data Center (NCDC)