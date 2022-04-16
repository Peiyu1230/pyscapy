// [rule: 抖音 ?] 使用问号匹配

var text = param(1);

var key = encodeURI(text);
var header = {
    "referer": "https://www.douyin.com/search/"+key+"?aid=9b83f210-e680-4a0e-8954-97b425c86c69&publish_time=0&sort_type=0&source=normal_search&type=general",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}
var uri = 'https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_general&sort_type=0&publish_time=0&keyword=' + key + '&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=&offset=0&count=15&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=100.0.4896.75&browser_online=true&engine_name=Blink&engine_version=100.0.4896.75&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7079409696313984526&msToken=_hwCpTlTmKfp-FtghoKJGJmEzsw1C16TWA4bRKdTcc2r4xMdVkjBz9qSa9-0ZNq5ySRFmkbB2eKSirD07tiNxFsz4h3x4_zxnPqWuyvIjIFf_zuWReApCVBvmWW_7gI=&X-Bogus=DFSzswVunPsANx1-SARukr7Tlqtv&_signature=_02B4Z6wo000018hdjBgAAIDAXIvXFfHZipvIXYiAAJBOLP2Gdo-b9fcimFj9dOkU2XzC8Lq5v-CKGuTus.o1GyLYDRhlPgG.c2TFVPqax7jrz-fChkOCCp6eNiuGszaRR8J3Pds7I8fBY6MHdd'
var data = request({
    url: uri,
    method:"get",
    headers: header,
    dataType:"json"
});
var dic= data['data'][0]['aweme_info']['play_addr_lowbr']['url_list'][0];


sendVideo(ur2)