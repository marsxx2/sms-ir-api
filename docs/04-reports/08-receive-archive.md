# 4.8. گزارش پیامک‌های دریافتی آرشیو شده

با فراخوانی متد زیر، گزارشی از پیامک‌های دریافتی در گذشته (تا انتهای روز قبل)، را مشاهده خواهید نمود.

**URL:** <https://api.sms.ir/v1/receive/archive>

**Request Method:** GET

## 4.8.1. پارامترهای درخواست

| مشخصه      | ارسال   | نوع                | توضیح                                             |
| ---------- | ------- | ------------------ | ------------------------------------------------- |
| FromDate   | اختیاری | Integer (UnixTime) | از تاریخ                                          |
| ToDate     | اختیاری | Integer (UnixTime) | تا تاریخ                                          |
| PageSize   | اختیاری | Integer            | تعداد آیتم‌های در صفحه (حداکثر:100 ، پیش‌فرض: 100) |
| PageNumber | اختیاری | Integer            | شماره صفحه درخواستی (مقدار پیش‌فرض 1 می‌باشد)       |
| mobile     | اختیاری | String             | شماره موبایل ارسال کننده پیامک                    |

**Request:** <https://api.sms.ir/v1/receive/archive?fromDate=1613465574&toDate=1623805200>

## 4.8.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)

| مشخصه            | نوع                | توضیح                    |
| ---------------- | ------------------ | ------------------------ |
| ReceiveReturnId  | Long               | شناسه پیامک دریافتی      |
| MessageText      | String             | متن پیامک                |
| Number           | Long               | شماره خط دریافت‌کننده     |
| Mobile           | Long               | شماره موبایل ارسال کننده |
| ReceivedDateTime | Integer (UnixTime) | زمان دریافت              |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [
        {
            "receiveReturnId": 12345678987,
            "messageText": "HyperBox.irفروشگاه اینترنتی اسباب بازی و عروسک",
            "number": 30004505000017,
            "mobile": 912xxxx002,
            "receivedDateTime": 1628683625
        }
    ]
}
```

## 4.8.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1669753800&toDate=1672814257");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("PageSize", "2");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1628683629&toDate=1628693629", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1628683629&toDate=1628693629',
  headers: {
    'PageSize': '2',
    'X-API-KEY': 'YOURAPIKEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**PHP:**

```PHP
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://api.sms.ir/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1628683629&toDate=1628693629',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'PageSize: 2',
    'X-API-KEY: YOURAPIKEY'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = ''
headers = {
  'PageSize': '2',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1628683629&toDate=1628693629", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/receive/archive?pageNumber=1&pageSize=100&fromDate=1628683629&toDate=1628693629")
  .method("GET", body)
  .addHeader("PageSize", "2")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](../07-sdks/README.md#جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

---

[بازگشت به فهرست مطالب](../README.md)
