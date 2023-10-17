import logging
import os
import time
from urllib.parse import urlencode

import requests
import schedule


def job():
    try:
        auth_url = 'https://ai.fakeopen.com/auth/login'
        register_url = 'https://ai.fakeopen.com/token/register'
        pool_url = 'https://ai.fakeopen.com/pool/update'

        user_info_env = os.environ.get('USER_INFO')
        unique_name = os.environ.get('UNIQUE_NAME')
        pool_token = os.environ.get('POOL_TOKEN')
        expires_in = 0
        user_info_list = user_info_env.split(',')
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        access_token_list: list = []
        for user_info in user_info_list:
            username_passwd = user_info.split(':')
            access_token_payload = {
                'username': username_passwd[0],
                'password': username_passwd[1]
            }
            access_token = requests.post(auth_url, headers=headers, data=urlencode(access_token_payload)).json()['access_token']
            access_token_list.append(access_token)

        share_token_list: list = []
        for _ in access_token_list:
            payload = f'unique_name={unique_name}&access_token={_}&expires_in={expires_in}&show_userinfo=false'
            share_response = requests.post(register_url, headers=headers, data=payload)
            share_token_list.append(share_response.json()['token_key'])
            logging.info(f'Response for {unique_name}: {share_response.text}')

        pool_payload = f'share_tokens={share_token_list[0]}%0A{share_token_list[1]}&pool_token={pool_token}'
        pool_response = requests.request('POST', pool_url, headers=headers, data=pool_payload)
        logging.info(f'Pool Response: {pool_response.text}')
        logging.info('Script executed successfully.')

    except Exception as e:
        logging.error(f'Error: {str(e)}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    job()  # 启动时执行一次
    schedule.every(12).days.at('03:00').do(job)
    logging.info('Script starts.')
    start_time = time.time()

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time % (60 * 60) < 1:
            start_time = current_time
            logging.info('程序正常运行,当前时间: %s', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

        schedule.run_pending()
        time.sleep(1)
