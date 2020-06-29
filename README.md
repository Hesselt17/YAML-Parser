## Dependencies

- python3
- yaml imported library
- csv imported library

## To Run

#### Method 1 (IDE):
1. Download zip file and unzip
2. Import 'YAML-Parser' folder into your python IDE of choice
3. Import yaml and csv into your IDE
4. Run the HighestScores script (can add more YAML files in the same directory as this
5. Check 'Output' directory or folder for the output file with the 'high_scores.csv' extension
6. Open and view the file from (5)

#### Method 2 (Command Line):
1. Download zip file and unzip
2. Drag the folder to your desktop
3. Open terminal or command line (CL) and copy, paste (into CL), and hit enter on the following: `cd ~/desktop/YAML-Parser`
4. Ensure you have yaml and csv installed (run the below 1 and 2 in the command line if you do not)
	1. `pip install PyYAML`
	2. `pip install python-csv`
5. Copy, paste (into CL), and hit enter on the following: `python HighestScore.py` 
6. Check the 'Outputs' folder (on CL: ls) for an output file with the 'high_scores.csv' extension
7. Open and view the file from 6

## Notes

• I included a clean_yml function in order to clean the files to ensure they are YAML compliant (this verison just cleaned the tabs present in the data1.yml file to ensure it was YAML compliant b/c apparently YAML files cannot have tabs).  
• I kept the full nested file path for the output assignment_id.  
• Students tied with the same highscore were determined by who came first in the YAML file. 