## Importing libraries and files
import os
from langchain_community.document_loaders import PDFLoader
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import tools
from crewai_tools.tools.serper_dev_tool import SerperDevTool

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class BloodTestReportTool:
    def read_data_tool(self, path='data/sample.pdf'):
        from langchain_community.document_loaders import PDFLoader
        docs = PDFLoader(file_path=path).load()

        full_report = ""
        for data in docs:
            content = data.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report

## Creating Nutrition Analysis Tool
class NutritionTool:
    def analyze_nutrition_tool(self, blood_report_data):
        # Process and analyze the blood report data
        processed_data = blood_report_data
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
        return "Nutrition analysis functionality to be implemented"


## Creating Exercise Planning Tool
class ExerciseTool:
    def create_exercise_plan_tool(self, blood_report_data):        
        # TODO: Implement exercise planning logic here
        return "Exercise planning functionality to be implemented"
