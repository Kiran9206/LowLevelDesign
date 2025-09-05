'''
Facade pattern for Data Analysis Application
Problem Statement
You are developing a software application for data analysis. The application involves data collection, preprocessing,
analysis algorithms, and visualization. The interactions between these components can become complex. Your goal is to
provide a simplified interface for data analysts to perform end-to-end analysis tasks without dealing with the inner
workings of each component.

Assignment
Your task is to implement the Facade pattern to refactor the existing data analysis workflow. The current workflow
involves data collection, preprocessing, applying analysis algorithms, and visualization. Your goal is to create a
facade class that provides a unified and simplified interface for data analysts to perform these tasks seamlessly.

Implementing the Facade Pattern
Review the original workflow: Take a closer look at the existing data analysis workflow and the interactions between
different components.

Create the facade class: Create a new class called DataAnalysisFacade that implements the Facade pattern. This class
will encapsulate the complex interactions between data collection, preprocessing, analysis algorithms, and visualization
components.

Remember to call the constructor of your facade using the same arguments from the existing components: The constructor
of your DataAnalysisFacade class should take the same arguments that the existing components require. This allows you to
pass the necessary parameters to the facade.

Test your implementation: Test cases have been provided for you to verify your implementation. Run the test cases to
ensure that your facade class works correctly and provides the expected functionality.
'''
'''
(CLIENT)
┌────────────────────────────────┐
│       Data Analyst/Client      │
└────────────────────────────────┘
             │
             ▼
      (FACADE INTERFACE)
┌────────────────────────────────┐
│   DataAnalysisFacade           │
├────────────────────────────────┤
│ + perform_data_analysis()      │
└────────────────────────────────┘
             │
             ▼
┌────────────────────────────────┐
│     DataCollection             │
├────────────────────────────────┤
│ + collect_data()               │
└────────────────────────────────┘
             │
             ▼
┌────────────────────────────────┐
│     DataPreprocessing          │
├────────────────────────────────┤
│ + preprocess_data()            │
└────────────────────────────────┘
             │
             ▼
┌────────────────────────────────┐
│     AnalysisAlgorithms         │
├────────────────────────────────┤
│ + apply_algorithm()            │
└────────────────────────────────┘
             │
             ▼
┌────────────────────────────────┐
│     DataVisualization          │
├────────────────────────────────┤
│ + visualize_data()             │
└────────────────────────────────┘
'''

class DataCollection:

    def collect_data(self, source)->str:
        return f"Data collected from {source}"

class DataPreprocessing:

    def process_data(self, data:str)-> str:
        return f"Data preprocessed: {data}"

class AnalysisAlgorithms:

    def apply_algorithm(self, data:str, algorithm:str)-> str:
        return f"Applied {algorithm} on {data}"

class DataVisualization:

    def visualize_data(self, data:str, chart_type:str)-> str:
        return f"Visualized {data} using {chart_type} chart"

class DataAnalysisFacade:

    def __init__(self):
        self.data_collector = DataCollection()
        self.data_preprocessor = DataPreprocessing()
        self.analysis_algorithms = AnalysisAlgorithms()
        self.data_visualizer = DataVisualization()

    def perform_data_analysis(self, source:str, algorithm:str, chart_type:str)-> str:

        collect_data = self.data_collector.collect_data(source)
        process_data = self.data_preprocessor.process_data(collect_data)
        analysis_data = self.analysis_algorithms.apply_algorithm(process_data, algorithm)
        visualization = self.data_visualizer.visualize_data(analysis_data, chart_type)

        return visualization

class Client:

    @staticmethod
    def test_facade(facade: DataAnalysisFacade):
        result = facade.perform_data_analysis("Database", "Regression", "Bar")
        print(result)
        assert result == "Visualized Applied Regression on Data preprocessed: Data collected from Database using Bar chart"
        print("All tests passed!")

if __name__ == "__main__":
    facade = DataAnalysisFacade()
    Client.test_facade(facade)