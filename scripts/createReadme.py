#!/usr/bin/env python
# Created by Bruce yuan on 18-1-22.
import requests
import os
import json
import time
import sqlite3


class Config:
    """
    some config, such as your github page
    这里需要配置你自己的项目地址
    １．　本地仓库的的路径
    ２．　github中的仓库leetcode解法的路径
    """
    local_path = '..'
    # solution of leetcode
    github_leetcode_url = 'https://github.com/anbo225/leetcode/blob/master/leetcode-algorithms/'
    # solution of pat,　暂时还没写
    # github_pat_url = 'https://github.com/hey-bruce/algorithms_and_oj/blob/master/pat-algorithms/'
    leetcode_url = 'https://leetcode.com/problems/'




class Question:
    """
    this class used to store the information of every question
    """

    def __init__(self, id_,
                 name, url,
                 lock, difficulty):
        self.id_ = id_
        self.title = name
        # the problem description url　问题描述页
        self.url = url
        self.lock = lock  # boolean，锁住了表示需要购买
        self.difficulty = difficulty
        # the solution url
        self.python = ''
        self.c_plus_plus = ''
        self.date = ''


    def __repr__(self):
        """
        没啥用，我为了调试方便写的
        :return:
        """
        return str(self.id_) + ' ' + str(self.title) + ' ' + str(self.url)


class TableInform:
    def __init__(self):
        # raw questions inform
        self.questions = []
        # this is table index
        self.table = []
        # this is the element of question
        self.table_item = {}
        self.locked = 0

    def get_leetcode_problems(self):
        """
        used to get leetcode inform
        :return:
        """
        # we should look the response data carefully to find law
        # return byte. content type is byte
        content = requests.get('https://leetcode.com/api/problems/algorithms/').content #这个api获取的题目数据不全，用爬虫来得到数据

        # get all problems
        self.questions = json.loads(content)['stat_status_pairs']
        # print(self.questions)
        difficultys = ['Easy', 'Medium', 'Hard']

        test = []
        for i in range(len(self.questions) - 1, -1, -1):
            question = self.questions[i]
            name = question['stat']['question__title']
            url = question['stat']['question__title_slug']
            id_ = str(question['stat']['frontend_question_id'])

            test.append(int(id_))

            if int(id_) < 10:
                id_ = '00' + id_
            elif int(id_) < 100:
                id_ = '0' + id_
            lock = question['paid_only']
            if lock:
                self.locked += 1
            difficulty = difficultys[question['difficulty']['level'] - 1]
            url = Config.leetcode_url + url + '/description/'
            q = Question(id_, name, url, lock, difficulty)
            self.table.append(q.id_)
            self.table_item[q.id_] = q


        return self.table, self.table_item

    # create problems folders
    def __create_folder(self, oj_name):
        oj_algorithms = Config.local_path + '/' + oj_name + '-algorithms'
        if os.path.exists(oj_algorithms):
            print(oj_name, ' algorithms is already exits')
        else:
            print('creating {} algorithms....'.format(oj_name))
            os.mkdir(oj_algorithms)
        for item in self.table_item.values():
            question_folder_name = oj_algorithms + '/' + item.id_ + '. ' + item.title
            if not os.path.exists(question_folder_name):
                print(question_folder_name + ' is not exits, create it now....')
                os.mkdir(question_folder_name)

    def update_table(self, oj_name):
        # the complete inform should be update
        complete_info = CompleteInform()
        self.get_leetcode_problems()
        # the total problem nums
        complete_info.total = len(self.table)
        complete_info.lock = self.locked
        self.__create_folder(oj_name)
        ojFolderPath = Config.local_path + '/' + oj_name + '-algorithms'
        # 查看os.walk看具体返回的是什么东西
        newly_solved_problem = []
        for _, folders, _ in os.walk(ojFolderPath):
            for folder in folders:
                for dirpath, _, files in os.walk(os.path.join(ojFolderPath, folder)):
                    if len(files) != 0:
                        complete_info.complete_num += 1
                    for file in files:
                        if file.endswith('.py'):
                            complete_info.solved['python'] += 1
                            # 如果当前文件没有日期标记的话，则其打上当前日期。 日期标记为  ### 2018-12-1 ###
                            filePath = os.path.join(dirpath, file)
                            with open(filePath,'r') as f:
                                lines = f.readlines()
                            if not lines[0].endswith("###\n"):
                                with open(filePath, 'w') as f:
                                    f.write("### {} solved ###\n".format(time.strftime("%Y-%m-%d")))
                                    f.writelines(lines)
                                    newly_solved_problem.append( folder[:3])
                                    self.table_item[folder[:3]].date = '{}'.format( time.strftime("%Y-%m-%d") )

                            # update problem inform
                            folder_url = folder.replace(' ', "%20")
                            folder_url = os.path.join(folder_url, file)
                            folder_url = os.path.join(Config.github_leetcode_url, folder_url)
                            # print(folder_url)
                            self.table_item[folder[:3]].python = '[Python]({})'.format(folder_url)
                        elif file.endswith('.cpp'):
                            complete_info.solved['c++'] += 1
                            folder_url = folder.replace(' ', "%20")
                            folder_url = os.path.join(folder_url, file)
                            folder_url = os.path.join(Config.github_leetcode_url, folder_url)
                            # print(folder_url)
                            self.table_item[folder[:3]].c_plus_plus = '[C++]({})'.format(folder_url)

        if len(newly_solved_problem) > 0:
            daily_message = '### {} 完成了:\n\n'.format( time.strftime("%Y-%m-%d") )
            for id in newly_solved_problem:
                tmp = '[{}]({})\n\n'.format(self.table_item[id].id_ +" " +  self.table_item[id].title , self.table_item[id].url)
                daily_message = daily_message + tmp
        else:
            daily_message = '### {} 未刷leetcode\n\n'.format( time.strftime("%Y-%m-%d") )
        daily_message += '\n----------------\n'
        readme = Readme(complete_info.total,
                        complete_info.complete_num,
                        complete_info.lock,
                        daily_message,
                        complete_info.solved
                        )
        readme.create_leetcode_readme([self.table, self.table_item])
        print('-------the complete inform-------')
        print(complete_info.solved)


class CompleteInform:
    """
    this is statistic inform
    """

    def __init__(self):
        self.solved = {
            'python': 0,
            'c++': 0,
        }
        self.complete_num = 0
        self.lock = 0
        self.total = 0

    def __repr__(self):
        return str(self.solved)


class Readme:
    """
    generate folder and markdown file
    update README.md when you finish one problem by some language
    """

    def __init__(self, total, solved, locked, daily, others=None):
        """

        :param total: total problems nums
        :param solved: solved problem nums
        :param others: 暂时还没用，我想做扩展
        """
        self.total = total
        self.solved = solved
        self.others = others
        self.locked = locked
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.daily = daily

        # '\n\nCompletion statistic: ' \
        # '\n1. Python: {python}' \
        # '\n2. C++: {c++}' \
        self.msg = '# Keep thinking, keep alive\n' \
                   'Until {}, I have solved **{}** / **{}** problems ' \
                   'while **{}** are still locked.' \
                   '\n\nNote: :lock: means you need to buy a book from LeetCode\n'.format(
                    self.time, self.solved, self.total, self.locked)

    def create_leetcode_readme(self, table_instance):
        """
        create REAdME.md
        :return:
        """
        file_path = Config.local_path + '/README.md'
        # write some basic inform about leetcode

        with open('daily','r+') as f:
            lines = f.readlines()
            lines.append(self.daily)
            f.writelines(lines)

        with open(file_path, 'w') as f:
            f.write(self.msg)
            f.write('\n----------------\n')
            f.writelines(lines)


        with open(file_path, 'a') as f:
            f.write('## LeetCode Solution Table\n')
            f.write('| ID | Title | Difficulty |  Python | C++ |\n')
            f.write('|:---:' * 5 + '|\n')
            table, table_item = table_instance
            # print(table)
            # for i in range(2):
            #     print(table_item[table[i]])
            # exit(1)
            for index in table:
                item = table_item[index]
                if item.lock:
                    _lock = ':lock:'
                else:
                    _lock = ''
                data = {
                    'id': item.id_,
                    'title': '[{}]({}) {}'.format(item.title, item.url, _lock),
                    'difficulty': item.difficulty,
                    'python': item.python if item.python else 'To Do',
                    'c++': item.c_plus_plus if item.c_plus_plus else 'To Do',

                }
                line = '|{id}|{title}|{difficulty}|{python}|{c++}|\n'.format(**data)
                f.write(line)
            print('README.md was created.....')




if __name__ == "__main__":
    table = TableInform()
    table.update_table('leetcode')

    # ToDo :
    # 1.抽出一个flag函数，来标记每天完成的oj
    # 2.抽出一个update函数，用来更新readme