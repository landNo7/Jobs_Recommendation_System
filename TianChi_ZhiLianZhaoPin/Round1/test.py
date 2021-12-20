import pandas as pd
import joblib as jl


def pred():
    clf=jl.load('D:\\WorkFile\\TianChi_ZhiLianZhaoPin\\model\\satisfied.pkl')
    all_data = pd.read_csv('D:\\WorkFile\\TianChi_ZhiLianZhaoPin\\Round1\\alldata.csv')
    use_feats = [c for c in all_data.columns if c not in ['user_id', 'jd_no', 'delivered', 'satisfied'] +
                 ['desire_jd_industry_id', 'desire_jd_type_id', 'cur_industry_id', 'cur_jd_type', 'experience',
                  'jd_title', 'jd_sub_type', 'job_description\n']]

    clf.predict(all_data[all_data['satisfied'] == -1][use_feats], num_iteration=clf.best_iteration)
    print(clf.best_score['valid_0']['auc'])

if __name__ == "__main__":
    print('program test beginning')
    pred()
    # min_work_year = {103: 1, 305: 3, 510: 5, 1099: 10}
    # max_work_year = {103: 3, 305: 5, 510: 10}
    # degree_map = {'其他': 0, '初中': 1, '中技': 2, '中专': 2, '高中': 2, '大专': 3, '本科': 4,
    #               '硕士': 5, 'MBA': 5, 'EMBA': 5, '博士': 6}
    #
    #
    # train_data_path = 'D:\\WorkFile\\TianChi_ZhiLianZhaoPin\\round1_train\\'
    # train_user = pd.read_csv(train_data_path + 'table1_user.csv')
    # print(train_user.loc[:, 'desire_jd_city_id'])
    # print(train_user['desire_jd_city_id'])