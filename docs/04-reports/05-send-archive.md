# 4.5. گزارش ارسال‌های آرشیو شده

با فراخوانی متد زیر، گزارشی از ارسال‌های انجام شده در گذشته (تا انتهای روز قبل)، را دریافت خواهید نمود.

**URL:** <https://api.sms.ir/v1/send/archive>

**Request Method:** GET

## 4.5.1. پارامترهای درخواست

| مشخصه      | ارسال   | نوع                | توضیح                                             |
| ---------- | ------- | ------------------ | ------------------------------------------------- |
| FromDate   | اختیاری | Integer (UnixTime) | از تاریخ                                          |
| ToDate     | اختیاری | Integer (UnixTime) | تا تاریخ                                          |
| PageSize   | اختیاری | Integer            | تعداد آیتم‌های در صفحه (حداکثر:100 ، پیش‌فرض: 100) |
| PageNumber | اختیاری | Integer            | شماره صفحه درخواستی (مقدار پیش‌فرض 1 می‌باشد)       |

**Request:** <https://api.sms.ir/v1/send/archive?fromDate=1613465574&toDate=1623805200>

## 4.5.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)

| مشخصه            | نوع                         | توضیح             |
| ---------------- | --------------------------- | ----------------- |
| MessageId        | Integer                     | شناسه یکتای پیامک |
| Mobile           | Long                        | شماره موبایل      |
| MessageText      | String                      | متن پیامک         |
| SendDateTime     | Integer (UnixTime)          | زمان ارسال        |
| LineNumber       | Long                        | شماره خط          |
| Cost             | Decimal                     | اعتبار کسر شده    |
| DeliveryState    | Nullable Byte               | وضعیت دلیوری      |
| DeliveryDateTime | Nullable Integer (UnixTime) | زمان دلیوری       |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [{
        "messageId": 89545112,
        "mobile": 912xxxx677,
        "messageText": "سرویس پیامکی ایده پردازان با بیش از یک دهه سابقه همراه شماست",
        "sendDateTime": 1628583626,
        "lineNumber": 30004505000017,
        "cost": 1.0,
        "deliveryState": 1,
        "deliveryDateTime": 1628683629
    },{
        "messageId": 89545113,
        "mobile": 919xxxx378,
        "messageText": "ipdemy.ir پلتفرم آموزش آنلاین، آکادمی ایده پردازان",
        "sendDateTime": 1628583626,
        "lineNumber": 30004505000017,
        "cost": 1.0,
        "deliveryState": 3,
        "deliveryDateTime": 1628683625
    },{
        "messageId": 89545114,
        "mobile": 921xxxx432,
        "messageText": "HyperBox.irفروشگاه اینترنتی اسباب بازی و عروسک ",
        "sendDateTime": 1628583626,
        "lineNumber": 30004505000017,
        "cost": 1.0,
        "deliveryState": 1,
        "deliveryDateTime": 1628683669
    }]
}
```

## 4.5.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1669753800&toDate=1672814257");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("Accept", "text/plain");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1650016645&toDate=1650880645", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1650016645&toDate=1650880645',
  headers: {
    'Accept': 'text/plain',
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
  CURLOPT_URL => 'https://api.sms.ir/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1650016645&toDate=1650880645',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Accept: text/plain',
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
  'Accept': 'text/plain',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1650016645&toDate=1650880645", payload, headers)
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
  .url("https://api.sms.ir/v1/send/archive?pageNumber=1&pageSize=100&fromDate=1650016645&toDate=1650880645")
  .method("GET", body)
  .addHeader("Accept", "text/plain")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](../07-sdks/README.md#جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

---

[بازگشت به فهرست مطالب](../README.md)
