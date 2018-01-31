#!/usr/bin/env python
# Created by Bruce yuan on 18-1-22.
import requests
import os
import json
import time
import sqlite3

from datetime import date,datetime,timedelta

from scripts.database import Question,Daily,session

from sqlalchemy.orm.exc import NoResultFound




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



def update_leetcode_problems():
        """
        爬取leetcode quesions，按需更新问题数据库
        :return:
        """

        # 获取leetcode中所有questions
        content = requests.get('https://leetcode.com/api/problems/algorithms/').content #这个api获取的题目数据不全，用爬虫来得到数据
        questionsFromLeetcode = json.loads(content)['stat_status_pairs']

        #获取数据库中现有的question ids
        questionIDsFromDatabase = []
        for row in  session.query(Question.id).all():
            questionIDsFromDatabase.append(row.id)

        #将problems转化为我们数据库存取的形式，如果没有则添加
        difficulty = ['Easy', 'Medium', 'Hard']

        for question in questionsFromLeetcode:
            id = str(question['stat']['frontend_question_id'])

            if int(id) in questionIDsFromDatabase:
                continue
            else:

                url = Config.leetcode_url + question['stat']['question__title_slug'] + '/description/'
                q = Question(id=id, name=question['stat']['question__title'],url=url,
                             lock = question['paid_only'], difficulty = difficulty[question['difficulty']['level'] - 1]
                        )
                print("向数据库中添加题目 %s \n", q)
                session.add(q)
                #为新题目创建相应的目录
                question_folder_name = Config.local_path+'/leetcode-algorithms/' + "%03d" % int(q.id) + '. ' + q.name
                if not os.path.exists(question_folder_name):
                    print(question_folder_name + ' is not exits, create it now....')
                    os.mkdir(question_folder_name)

        session.commit()


def record_daily_work():
    #从数据库中获取今天的daily，如果不存储则创建
    try:
        today = session.query(Daily).filter_by(date = date.today()).one()
    except NoResultFound:
        today = Daily(date = date.today())
        session.add(today)


    ojFolderPath = Config.local_path + '/leetcode-algorithms'
    for _, folders, _ in os.walk(ojFolderPath):
        for folder in folders:
            for dirpath, _, files in os.walk(os.path.join(ojFolderPath, folder)):
                for file in files:
                    if file.endswith('.py'):
                        # 如果当前文件没有日期标记的话，则其打上当前日期。 日期标记为  ### 2018-12-1 ###
                        filePath = os.path.join(dirpath, file)
                        with open(filePath, 'r') as f:
                            lines = f.readlines()

                        #预处理
                        # id = int(folder[:3])
                        # q = session.query(Question).filter_by(id=id).one()
                        #
                        # folder_url = folder.replace(' ', "%20")
                        # folder_url = os.path.join(folder_url, file)
                        # folder_url = os.path.join(Config.github_leetcode_url, folder_url)
                        # q.python_solution = '[Python]({})'.format(folder_url)
                        # day = lines[0][4:14]
                        # tmp = datetime.strptime(day, "%Y-%m-%d").date()
                        # try:
                        #     tmp_today=session.query(Daily).filter_by(date=tmp).one()
                        # except NoResultFound:
                        #     tmp_today = Daily(date=tmp)
                        # q.daily = tmp_today
                        # session.add(tmp_today)

                            # print(folder_url)

                        if not lines[0].endswith("###\n"):
                            with open(filePath, 'w') as f:
                                f.write("### {} solved ###\n".format(time.strftime("%Y-%m-%d")))
                                f.writelines(lines)

                            #更新问题数据库
                            id = int(folder[:3])
                            q  = session.query(Question).filter_by(id=id).one()
                            q.daily = today
                            # update problem informormatino
                            folder_url = folder.replace(' ', "%20")
                            folder_url = os.path.join(folder_url, file)
                            folder_url = os.path.join(Config.github_leetcode_url, folder_url)
                            # print(folder_url)
                            q.python_solution = '[Python]({})'.format(folder_url)


                    #elif file.endswith('.cpp'):

    session.commit()


def generate_readme():

     file_path = Config.local_path + '/README.md'
     with open(file_path, 'w') as f:

         for daily  in  session.query(Daily).order_by(Daily.date).all():
             if len(daily.questions) == 0:
                 f.write( '### {} 未刷leetcode\n\n'.format( datetime.strftime(daily.date, "%Y-%m-%d") ) )
             else:
                 f.write('### {} 完成了:\n\n'.format(datetime.strftime(daily.date, "%Y-%m-%d")))

             for question in daily.questions:
                 f.write( '| ID | Title | Difficulty |  Python Solution |\n')
                 f.write('|:---:' * 4 + '|\n')
                 if question.lock:
                     _lock = ':lock:'
                 else:
                     _lock = ''
                 data = {
                     'id': question.id,
                     'title': '[{}]({}) {}'.format(question.name, question.url, _lock),
                     'difficulty': question.difficulty,
                     'python': question.python_solution

                 }
                 line = '|{id}|{title}|{difficulty}|{python}|\n'.format(**data)
                 f.write(line)
                 f.write('\n----------------\n')


if __name__ == "__main__":

    # table = TableInform()
    # table.update_table('leetcode')

    # ToDo :
    # 1.抽出一个flag函数，来标记每天完成的oj
    # 2.抽出一个update函数，用来更新quesion数据库
#    update_leetcode_problems()
    record_daily_work()
    generate_readme()