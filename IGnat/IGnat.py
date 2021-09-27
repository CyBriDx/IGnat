import http.client
import json

NODES = {}
conn = http.client.HTTPSConnection("www.instagram.com")
payload = ''
cached_comments_cursor = '17961420901443662'
bifilter_token = 'KEgBDACgACAAGAAQAAgACAD9N99___v_u_6_nb___v___7V_f9_SJrbfSn339e3_v239_f___9_____r_9v____rHyT23bQIUAAA'
while True:

    headers = {
        'cookie': 'mid=YGijbwALAAGg30a2ecdGz7ygN8Y5; ig_did=41C6FA35-EB1D-4971-849E-ED6BCAB2BBB0; ig_nrcb=1; ds_user_id=6987698478; fbm_124024574287414=base_domain=.instagram.com; csrftoken=Hwi67osMeS0VlXNYPT4ufvQgoyihmI66; sessionid=6987698478%3Aqfm7fSl3yeRgVi%3A29; shbid="1168605469876984780541664114060:01f71304fe6ade997e8f5bef4cedab4c34b0bb23af304205d2dfda5a709405672cf6c66c"; shbts="163257806005469876984780541664114060:01f74a78df4c69a2521a5793048a14c954a4d7821231bb0567c5b4fa33ddb7c1b77f0a54"; fbsr_124024574287414=0vTKm2FCz4imv_neVs2uAqToN1nBbk-K2PPahe26fS8.eyJ1c2VyX2lkIjoiMTAwMDAwNDk4NTUxMjQ0IiwiY29kZSI6IkFRQWFtWEF4dC12cEVWZUxZMWJZNE1ra2pucmtCZDhES2N4amlXZ0lPOE9rMFpWWDRYeHFSWkZVa2xBSnRHaGZJSjRieVZ2NEl4NE9SMXp2WXRVUGFfTEVaSU9zaHctMGlTakJvNG4ySk15SlBhMzg2LUFaRkViTTZ0OFlQZUttdWJEVkl1R0U3Y0MydFVTMDZ5WTMwLTJrTWotRXpGcEpNYzRuZHgzQUUwOEk5WjAwVEtnN29zakxUUlJLdzVKWWtDNE40LWtzUWI0WWdsVDY5RHh3TjVwWXNFY0hMT1lqU19mbkhkR1lDVWxLb19PYlhhOENMUW81QklYMTd6UXlmVjBFWDlQbHBjaEJHM3VWWHFQbFV1bF9GUXd2MWRGbDllOWFoQ0FmMC0xMUp4ZXoySWZEclROaFAtcTFEUE9wY2hWZU5Ua2ZaeDJWY19IZ0xXSWFFREhOIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU5yY0czVkpSeXdXYTJHQUF6aU01c0wwalZWWkJaQXhaQW8zc2xkR1JpVWoxUkZYOTlvUWlramJvZUVZRXhTQmtiU3ZTZkZjQWxNMXduencyRDB6clpCODNSeUlnRzRhTE43ZUZJY3p4RFlyTU16YnNBcjdwQ2Jrc2RaQ1lzWVpDUFBMT2pMNjEzMmJQdTBFTmx0ZG4xUnhXNVBhZHdFQVJyeWE4SE9FQjgiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTYzMjY4ODUzNH0; fbsr_124024574287414=tgFbSgsQ1V1r8Vjvtu4hUA8m0DNN7M4zvGOMH21F_c4.eyJ1c2VyX2lkIjoiMTAwMDAwNDk4NTUxMjQ0IiwiY29kZSI6IkFRQ0VueC1aQzIzcEV3Y2tuUW1vTVpNcjhDMmliS1Z3NGJYM3kzMmNkd05UVm5wY0dxRGp6eGswUDVHYUpzZ0tabWlsTzBwLVJ1bXh1WDRNOURidWhKdVhEUGNpSGFlRjdaNUU1R1RZNUEtaUhQQ0lJS09KOWpNZXQycmtxUE8xajhqWGVOQ2E2aWRGNFFUVmVraGZmVnJJcGNHQkVVbnJ2MWFtMzgtMGVSWXp5ZmljbFU5bURPdDVBdGtubTVOTDVlV19OVDhSQTFOUkR4WmhFN25pb1phWDExQzF6a0VLWWVYR0R6anFFT2JQc29OU2VGMDY0cUZqbEoxNFNVcTVXNWFFV2h6N2pPNjMyRzJZODhQbV90X0JGR1Fpcm1QQmpvbkk1QUVsSEVYMFc2OFl2S2lSVnlybThkYkYwaVZ2eXAyWFdSemJpRm5FRWNWblFoOUxGekU4Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU5FRnloaGduYm1QSlpDWkFuRFpCVll3Uk92bjF6bDZLNWhXTXJBR3dKeXRCdkZBZE1NNGJaQ1pCZE9aQmtSTVdZWXFTdTdnelFkQXZLOXY2NVhOTE0yZ0l3bmFrVkdTVEFkcGg0UHcyQXJqOVk2czVvVmlETWQzSFpDSXV2cFl2MVlDR2tuNExLSVlwSTJvejlqWkJtZ3NSUTZISExZWWZ3bDNSNGFXWWRaQ3UiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTYzMjY4OTEzN30; rur="ATN05469876984780541664225141:01f787f0035073aecdecde0b910934fbb824079b128596e83e7d2df8ce291b4b68a6a28b"; csrftoken=buoADu4noYxTAv7cKdFU8ozaK7g7FjYc; ds_user_id=6987698478; ig_did=B0582707-C46B-4EED-B9EB-D980F08B32EC; ig_nrcb=1; mid=YTdXuQALAAHgPByUDg3UIdMV2Vc1; rur="ATN\\0546987698478\\0541664227551:01f7c541c394207a0cfcdab79e21ad968d1af006026eb96d29f0402dd9d54310ab7b62fb"; shbid="11686\\0546987698478\\0541664224757:01f7e8f91857ed3c0fae999b2037ebb233d75ba6402cd5cff5077ca8cbbe0bd091b75e67"; shbts="1632688757\\0546987698478\\0541664224757:01f7f9c4839c536ba3679f86cf8fa0ec4055c8505ae08c5565d07b8f58d976f11406c652"'
    }
    conn.request(
        "GET", f'/graphql/query/?query_hash=bc3296d1ce80a24b1b6e40b1e72903f5&variables=%7B%22shortcode%22%3A%22CUO8DOOoFIy%22%2C%22first%22%3A12%2C%22after%22%3A%22%7B%5C%22cached_comments_cursor%5C%22%3A+%5C%22{cached_comments_cursor}%5C%22%2C+%5C%22bifilter_token%5C%22%3A+%5C%22{bifilter_token}%5C%22%7D%22%7D', payload, headers)
    res = conn.getresponse()
    data = res.read()
    data_json = json.loads(data.decode("utf-8"))
    bifilter_token = json.loads(data_json['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['end_cursor'])['bifilter_token']
    try:
        cached_comments_cursor = json.loads(data_json['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['end_cursor'])['cached_comments_cursor']
    except KeyError: 
        cached_comments_cursor = ''
    for i in data_json['data']['shortcode_media']['edge_media_to_parent_comment']['edges']:
        if i['node']['edge_threaded_comments']['count'] > 0:
            for j in i['node']['edge_threaded_comments']['edges']:
                if j['node']['owner']['username'] == 'rudeguy9024':
                    NODES[j['node']['text']] = i['node']['text']
    if data_json['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['has_next_page'] != True:
        break
print(NODES)
