import requests

def test_get_product_list():
    base_url = 'https://hluyxndmpmooyznhfwxc.supabase.co'
    endpoint = '/rest/v1/products'
    param = {'select':'*', 'order':'created_at.desc'}
    auth = 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6ImRIWis2SmtoMUxhMlpQMXgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2hsdXl4bmRtcG1vb3l6bmhmd3hjLnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiI3NDlkMjZmYy1mZTA0LTQ5YTItYWZmNS0yYzFkMTlmNzllYjciLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzYzMjg0NDYwLCJpYXQiOjE3NjMyODA4NjAsImVtYWlsIjoidW5vLnRlc3RpbmczQGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsiZW1haWwiOiJ1bm8udGVzdGluZzNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwic3ViIjoiNzQ5ZDI2ZmMtZmUwNC00OWEyLWFmZjUtMmMxZDE5Zjc5ZWI3In0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoicGFzc3dvcmQiLCJ0aW1lc3RhbXAiOjE3NjMyODA4NjB9XSwic2Vzc2lvbl9pZCI6ImFiMDFmMDA2LTgzYWQtNDEzMC05NDk1LWFkYjU1MzJhZTVmYSIsImlzX2Fub255bW91cyI6ZmFsc2V9.q4zH8a1cpGnWu0zeTO8ltYGUPkSb4YASUwyp0ATZlv0'    api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsdXl4bmRtcG1vb3l6bmhmd3hjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk2ODQ4MTQsImV4cCI6MjA2NTI2MDgxNH0.lVhUKhscl3nT6oeVbnXb0BbF0mI0lFR_KKlxYMX6Mnc'

    headers = {'Apikey': api_key, 'Authorization':auth}

    resp = requests.get(base_url+endpoint,headers=headers, params=param)
    assert resp.status_code == 200




