# 3.1. ارسال گروهی

این متد برای ارسال یک متن پیامک به گروهی از شماره موبایل‌ها مورد استفاده قرار می‌گیرد. همچنین شما می‌توانید با مقداردهی به پارامتر زمان ارسال، از قابلیت ارسال پیامک زمان‌بندی شده نیز استفاده نمایید.

**URL:** <https://api.sms.ir/v1/send/bulk>

**Request Method:** POST

> این متد برای ارسال‌های ساده (تکی یا گروهی) از خط اختصاصی شما مناسب است. در صورتی که خط اختصاصی شما به‌عنوان خط خدماتی فعال نشده باشد، پیامک‌های ارسالی با این متد ممکن است برای مخاطبانی که پیامک‌های تبلیغاتی را مسدود کرده‌اند ارسال نشود (به لیست سیاه اصابت کند).

> حداکثر تعداد مجاز شماره‌های مقصد 100 می‌باشد.
> برای ارسال زمان‌بندی شده، انتخاب زمان گذشته نامعتبر می‌باشد.
> برای ارسال زمان‌بندی شده، زمان معتبر می‌تواند در بازه یک ساعت آینده تا حداکثر 365 روز آینده در نظر گرفته شود.

## 3.1.1. پارامترهای بدنه درخواست

| مشخصه        | ارسال   | نوع             | توضیح                                                           |
| ------------ | ------- | --------------- | --------------------------------------------------------------- |
| lineNumber   | اجباری  | Long            | شماره خط ارسالی                                                 |
| MessageText  | اجباری  | String          | متن پیام کوتاه                                                  |
| Mobiles      | اجباری  | Array of String | شماره موبایل‌ها                                                  |
| SendDateTime | اختیاری | UnixTime        | زمان ارسال پیامک (در صورت خالی بودن، ارسال در لحظه انجام می‌شود) |

**Request Body:**

```JSON
{
    "lineNumber": 30004505000017,
    "messageText": "سرویس پیامکی ایده پردازان با بیش از یک دهه سابقه همراه شماست",
    "mobiles": [
        "0912xxxx677",
        "0919xxxx904"
    ]
}
```

## 3.1.2. مدل دیتای بازگشتی

| مشخصه      | نوع              | توضیح                                |
| ---------- | ---------------- | ------------------------------------ |
| PackId     | Guid             | شناسه یکتای مجموعه ارسال             |
| MessageIds | Array of Integer | آرایه‌ای از شناسه‌های یکتای هر پیامک |
| Cost       | Decimal          | اعتبار مصرفی مجموعه ارسال            |

> در آرایه‌ی `MessageIds`، هر عضو می‌تواند مقدار id متناظر پیامک، `0` یا `null` باشد؛ مقدار `0` به معنای قرارگرفتن شماره در لیست سیاه است و مقدار `null` به معنای نامعتبر بودن شماره یا بیش از حد بودن طول متن برای آن مخاطب است.

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": {
        "packId": "2b99e63c-9bf8-4a21-9bfe-3f72dc1b46f1",
        "messageIds": [
            86522023,
            86522024
        ],
        "cost": 2.0
    }
}
```

## 3.1.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var payload = @"{" + "\n" +
@"    ""lineNumber"": 300000000000," + "\n" +
@"    ""messageText"": ""Your Text""," + "\n" +
@"    ""mobiles"": [" + "\n" +
@"        ""Your Mobile 1""" + "\n" +
@"    ]," + "\n" +
@"    ""sendDateTime"": null" + "\n" +
@"}";
HttpContent content = new StringContent(payload, Encoding.UTF8, "application/json");
var response = await httpClient.PostAsync("https://api.sms.ir/v1/send/bulk", content);
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("X-API-KEY", "YOURAPIKEY");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "lineNumber": 300000000000,
  "messageText": "Your Text",
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 2"
  ],
  "sendDateTime": null
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/bulk", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var data = JSON.stringify({
  "lineNumber": 300000000000,
  "messageText": "Your Text",
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 2"
  ],
  "sendDateTime": null
});

var config = {
  method: 'post',
  url: 'https://api.sms.ir/v1/send/bulk',
  headers: {
    'X-API-KEY': 'YOURAPIKEY',
    'Content-Type': 'application/json'
  },
  data : data
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
CURLOPT_URL => 'https://api.sms.ir/v1/send/bulk',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "lineNumber": 300000000000,
    "messageText": "Your Text",
    "mobiles": [
        "Your Mobile 1",
        "Your Mobile 2"
    ],
    "sendDateTime": null
}',
  CURLOPT_HTTPHEADER => array(
    'X-API-KEY: YOURAPIKEY',
    'Content-Type: application/json'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

**Python:**

```Python
conn = http.client.HTTPSConnection("api.sms.ir")
payload = json.dumps({
  "lineNumber": 300000000000,
  "messageText": "Your Text",
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 2"
  ],
  "sendDateTime": None
})
headers = {
  'X-API-KEY': 'YOURAPIKEY',
  'Content-Type': 'application/json'
}
conn.request("POST", "/v1/send/bulk", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
    .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\r\n    \"lineNumber\": 300000000000,\r\n    \"messageText\": \"Your Text\",\r\n
  \"mobiles\": [\r\n        \"Your Mobile 1\",\r\n        \"Your Mobile 2\"\r\n    ],\r\n    \"sendDateTime\": null\r\n}");
Request request = new Request.Builder()
    .url("https://api.sms.ir/v1/send/bulk")
    .method("POST", body)
    .addHeader("X-API-KEY", "YOURAPIKEY")
    .addHeader("Content-Type", "application/json")
    .build();
Response response = client.newCall(request).execute();
```

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](../07-sdks/README.md#جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

---

[بازگشت به فهرست مطالب](../README.md)
