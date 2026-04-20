import concurrent.futures
import time
from auth_utils.secrets import get_secret

def run_in_thread():
    print('Starting thread...')
    try:
        val = get_secret('gemini-api-key')
        print(f'Secret fetched in thread: {val[:5]}')
    except Exception as e:
        print(f'Exception in thread: {e}')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(run_in_thread).result()
