# 3.2. ارسال نظیر به نظیر

این متد برای ارسال به گروهی از موبایل‌ها با متن‌های متفاوت برای هر کدام، مورد استفاده قرار می‌گیرد. همچنین شما می‌توانید با مقداردهی به پارامتر زمان ارسال، از قابلیت ارسال پیامک زمان‌بندی شده نیز استفاده نمایید.

**URL:** <https://api.sms.ir/v1/send/likeToLike>

**Request Method:** POST

> حداکثر تعداد مجاز شماره‌های مقصد 100 می‌باشد.
> برای ارسال زمان‌بندی شده، انتخاب زمان گذشته نامعتبر می‌باشد.
> برای ارسال زمان‌بندی شده، زمان معتبر می‌تواند در بازه یک ساعت آینده تا حداکثر 365 روز آینده در نظر گرفته شود.

تعداد شماره موبایل‌ها و متن‌های پیامک باید برابر باشند.

## 3.2.1. پارامترهای بدنه درخواست

| مشخصه        | ارسال   | نوع             | توضیح                                                           |
| ------------ | ------- | --------------- | --------------------------------------------------------------- |
| lineNumber   | اجباری  | Long            | شماره خط ارسالی                                                 |
| MessageTexts | اجباری  | Array of String | متن‌های پیام کوتاه                                              |
| Mobiles      | اجباری  | Array of String | شماره موبایل‌ها                                                  |
| SendDateTime | اختیاری | UnixTime        | زمان ارسال پیامک (در صورت خالی بودن، ارسال در لحظه انجام می‌شود) |

**Request Body:**

```JSON
{
    "lineNumber": "30004505000017",
    "messageTexts": [
        "سرویس پیامکی ایده پردازان با بیش از یک دهه سابقه همراه شماست",
        "ipdemy.ir پلتفرم آموزش آنلاین، آکادمی ایده پردازان"
    ],
    "mobiles": [
        "912xxxx677",
        "+98919xxxx904"
    ]
}
```

## 3.2.2. مدل دیتای بازگشتی

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

## 3.2.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var payload = @"{" + "\n" +
@"  ""lineNumber"": 300000000000," + "\n" +
@"  ""messageTexts"": [" + "\n" +
@"    ""Your Text 1""" + "\n" +
@"  ]," + "\n" +
@"  ""mobiles"": [" + "\n" +
@"    ""Your Mobile 1""" + "\n" +
@"  ]," + "\n" +
@"  ""sendDateTime"": null" + "\n" +
@"}";
HttpContent content = new StringContent(payload, Encoding.UTF8, "application/json");
var response = await httpClient.PostAsync("https://api.sms.ir/v1/send/likeToLike", content);
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Accept", "text/plain");
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var raw = JSON.stringify({
  "lineNumber": 300000000000,
  "messageTexts": [
    "Your Text 1",
    "Your Text 2"
  ],
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 1"
  ],
  "senddatetime": null
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/send/likeToLike", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var data = JSON.stringify({
  "lineNumber": 300000000000,
  "messageTexts": [
    "Your Text 1",
    "Your Text 2"
  ],
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 1"
  ],
  "senddatetime": null
});

var config = {
  method: 'post',
  url: 'https://api.sms.ir/v1/send/likeToLike',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'text/plain',
    'X-API-KEY': 'YOURAPIKEY'
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
  CURLOPT_URL => 'https://api.sms.ir/v1/send/likeToLike',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
    "lineNumber": 300000000000,
    "messageTexts": [
        "Your Text 1",
        "Your Text 2"
    ],
    "mobiles": [
        "Your Mobile 1",
        "Your Mobile 1"
    ],
    "senddatetime": null
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
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
payload = json.dumps({
  "lineNumber": 300000000000,
  "messageTexts": [
    "Your Text 1",
    "Your Text 2"
  ],
  "mobiles": [
    "Your Mobile 1",
    "Your Mobile 1"
  ],
  "senddatetime": None
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("POST", "/v1/send/likeToLike", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Java:**

```Java
OkHttpClient client = new OkHttpClient().newBuilder()
.build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"lineNumber\": 300000000000,\n
\"messageTexts\": [\n        \"Your Text 1\",\n        \"Your Text 2\"\n    ],\n
  \"mobiles\": [\n        \"Your Mobile 1\",\n        \"Your Mobile 1\"\n    ],\n    \"senddatetime\": null\n}");
Request request = new Request.Builder()
  .url("https://api.sms.ir/v1/send/likeToLike")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Accept", "text/plain")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](../07-sdks/README.md#جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

---

[بازگشت به فهرست مطالب](../README.md)
