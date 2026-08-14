# 4.2. گزارش مجموعه ارسال‌های روز

شما می‌توانید با استفاده از این گزارش اطلاعات کلی مجموعه ارسال‌های روز جاری را دریافت نمایید.

**URL:** <https://api.sms.ir/v1/send/pack>

**Request Method:** GET

## 4.2.1. پارامترهای درخواست

| مشخصه      | ارسال   | نوع     | توضیح                                             |
| ---------- | ------- | ------- | ------------------------------------------------- |
| PageSize   | اختیاری | Integer | تعداد آیتم‌های در صفحه (حداکثر:100 ، پیش‌فرض: 100) |
| PageNumber | اختیاری | Integer | شماره صفحه درخواستی (مقدار پیش‌فرض 1 می‌باشد)       |

**Request:** <https://api.sms.ir/v1/send/pack>

## 4.2.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)

| مشخصه            | نوع    | توضیح         |
| ---------------- | ------ | ------------- |
| packId           | GUID   | شناسه مجموعه  |
| recipientCount   | Number | تعداد مخاطبان |
| creationDateTime | Number | زمان ایجاد    |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [{
        "packId": e7c09e23f0db4834b9bcb79e7b054f4c,
        "recipientCount": 100,
        "creationDateTime": 1628683626,
    },{
       "packId": 0cf3017fd9d84babbb5ed5579104dab2,
        "recipientCount": 200,
        "creationDateTime": 1628683626,
    }]
}
```

## 4.2.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/send/pack?pageNumber=1&pageSize=100");
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

fetch("https://api.sms.ir/v1/send/pack?pageNumber=1&pageSize=100", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/send/pack?pageNumber=1&pageSize=100',
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
  CURLOPT_URL => 'https://api.sms.ir/v1/send/pack?pageNumber=1&pageSize=100',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Accept: text/plain',
    'X-API-KEY: YOURAPIKEY',
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
conn.request("GET", "/v1/send/pack?pageNumber=1&pageSize=100", payload, headers)
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
  .url("https://api.sms.ir/v1/send/pack?pageNumber=1&pageSize=100")
  .method("GET", body)
  .addHeader("Accept", "text/plain")
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](../07-sdks/README.md#جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

---

[بازگشت به فهرست مطالب](../README.md)
