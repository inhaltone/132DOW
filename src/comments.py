from app import GuardianCommentsAPI
import pandas as pd

guardian_df = pd.read_csv('../data/raw/guardian/guard-articles-russia.csv')
comment_keys = guardian_df[~guardian_df['Comments key'].isnull()]['Comments key'].to_numpy()

guardian_comments_df = pd.DataFrame()
total_pages = 0
page = 0
guardian_comments = []
# test response
for key in comment_keys:
    while True:
        page += 1
        response = GuardianCommentsAPI.getCommentsByCommentKey(key, page)
        data = GuardianCommentsAPI.apiResponseToDictionary(response)
        guardian_comments_df = pd.concat([guardian_comments_df, pd.DataFrame(data)], axis=0, ignore_index=True)
        print(f'status: {response["status"]}')
        print(f'title: {response["discussion"]["title"]}')
        total_pages = response['pages']
        if page == total_pages:
            page = 0
            break

guardian_comments_df.to_csv('../data/raw/guardian/guard-articles-russia-comments.csv')
