"""
Created on 6/18/20
@author: Tommy Hessel
"""

import yaml
import csv

def clean_yml(file):
    """
    Cleans up the YAML data by replacing tabs with two spaces.
    Writes a new, cleaned .yml file to the same directory.
    :param: file (string) Input YAML file name to clean
    :return: cleanFileName (string) Output cleaned YAML file name
    """
    if 'Tests' in file:
        clean_file_path = 'CleanedFiles/'+ file[file.rfind('/')+1:file.rfind('.')] + '_clean.yml'
    else:
        clean_file_path = 'CleanedFiles/'+ file[:file.rfind('.')] + '_clean.yml'

    print(clean_file_path)
    file_in = open(file, 'r')
    file_out = open(clean_file_path, 'w')
    file_in.seek(0)
    file_out.seek(0)
    for line in file_in:
        if '\t' in line:
            line = line.replace('\t', '  ')
        file_out.write(line)
    file_in.close()
    file_out.close()
    return clean_file_path


def read_yml(clean_filepath):
    """
    Reads in the cleaned YAML data.
    :param clean_filepath (string) Cleaned YAML file
    :return: data (dict) parsed YAML file
    """
    with open(clean_filepath, 'r') as file:
        data = yaml.safe_load(file)
    return data


def get_max_key(dict):
    """
    Finds key corresponding to first max value. .keys() and .values()
    ensures that the parallel order of the lists is preserved.
    :param dict (dict) dictionary
    :return: (dict key) key corresponding to max val (first)
    """
    keys = list(dict.keys())
    vals = list(dict.values())
    max_key = keys[vals.index(max(vals))]
    return max_key


def all_paths(tree, cur=()):
    """
    Recursive method to trace all paths to end leaves == values within an
    assignment == students.
    :param tree: (dict) corresponding to nested yml structure
    :param cur: (list) list of the path taken to a student
    :return: (list) with path taken to student
    """
    if type(tree) is not dict:
        yield cur
    else:
        for k, v in tree.items():
            for path in all_paths(v, cur+(k,)):
                yield path


def check_scores(scores_dict, PRINT):
    """
    Finds the student who scored the highest per assignment. Iterative DFS
    search using stack to cover all depths. Works if the YAML also had a cycle
    (but shouldn't).
    :param scores_dict (dict) all scores
    :return: high_scores_dict: (dict) all assignments mapped to student with
     the highest grade
    """

    high_scores_dict = dict()
    stack = list(scores_dict.items())
    visited = set()

    while len(stack) > 0:
        t = stack.pop()
        key, val = t[0], t[1]
        if type(val) is dict:
            if key not in visited:
                if 'assignment' in key:
                    high_scores_dict[key] = get_max_key(val)
                else:
                    lvl = val.items()
                    stack.extend(lvl)
            visited.add(key)
    if PRINT:
        print ('High Score Dict:',high_scores_dict)
    return high_scores_dict


def finalize_res(file, full_paths, high_scores_dict, PRINT):
    """
    Pairs the full path to assignment with the highest scoring student
    on the assignment.
    :param file: (string) name of YAML file (and locaion to if not at same
    dir level)
    :param full_paths (list of tuples) list containing all paths to students
    :param high_scores_dict (dict) assignment keys mapped to student names
    with the highest score on the assignment
    :return: res_scores (list of tuples)
    """
    res_scores = []
    vis = set()
    for p in full_paths:
        assign = p[-2]
        if len({assign} & vis) == 0:
            res_scores.append((file+'/'+'/'.join(p[:-1]),high_scores_dict[assign]))
            vis.add(assign)
    if PRINT:
        print ('Res Scores:',res_scores )
    return res_scores


def write_to_csv (file,res_scores):
    """
    Write the results from finalize_res to a csv in the outputs directory.
    :param file (string) name of YAML file
    :param res_scores (list of 2-tuples)
    :return: None
    """
    if 'Tests' in file:
        new_path = 'Output/' + file[file.rfind('/')+1:file.rfind('.')] + '_high_scores.csv'
    else:
        new_path = 'Output/' + file_path[:file_path.find('.')] + '_high_scores.csv'
    with open(new_path, 'w') as csv_f:
        w = csv.writer(csv_f)
        w.writerow(['assignment_id','highest_grade'])
        for t in res_scores:
            path = t[0]
            student = t[1]
            w.writerow([path,student])
    return


def run_all(file_path, PRINT):
    """
    Runner for all of the above functions.
    :param file_path: (string) path to desired YAML file.
    :param PRINT: (bool) toggle for if print statements are desired
    :return: None
    """
    clean_file = clean_yml(file_path)
    yml_dict = read_yml(clean_file)
    full_p = list(all_paths(yml_dict))
    h_s_d = check_scores(yml_dict, PRINT)
    final_res = finalize_res(file_path, full_p, h_s_d, PRINT)
    write_to_csv(file_path, final_res)
    return


if __name__ == "__main__":

    #Run#
    file_path = 'data1.yml'
    #PRINT = False
    PRINT = True #Uncomment this line if want to see full print statements
    run_all(file_path,PRINT)


    #Test Cases# Uncomment these for more checks
    """
    file_path = 'Tests/data2.yml'
    PRINT = True #Uncomment this line if want to see full print statements
    run_all(file_path,PRINT)

    file_path = 'Tests/data3.yml'
    PRINT = True #Uncomment this line if want to see full print statements
    run_all(file_path,PRINT)
    """

