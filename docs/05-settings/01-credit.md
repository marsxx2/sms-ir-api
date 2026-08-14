# 5.1. دریافت مقدار اعتبار فعلی

برای مشاهده مقدار اعتبار فعلی از متد زیر استفاده نمایید.

**URL:** <https://api.sms.ir/v1/credit>

**Request Method:** GET

> ⚠️ **نکته:** با اینکه این متد در مستندات رسمی sms.ir با عنوان «اعتبار» (credit) معرفی شده، مقدار بازگشتی آن در عمل **تعداد پیامک باقی‌مانده** حساب شماست، نه مبلغ اعتبار ریالی. این نکته در مستندات رسمی ذکر نشده و بر اساس آزمایش عملی مشخص شده است؛ در صورت مشاهده رفتار متفاوت، مقادیر واقعی حساب خودتان را نیز بررسی کنید.

## 5.1.1. دیتای بازگشتی

| نوع     | توضیح                    |
| ------- | ------------------------ |
| Decimal | تعداد پیامک باقی‌مانده   |

**Request:** <https://api.sms.ir/v1/credit>

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": 165.3
}
```

## 5.1.2. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/credit");
var result = await response.Content.ReadAsStringAsync();
```

**JS:**

```JS
var myHeaders = new Headers();
myHeaders.append("X-API-KEY", "YOURAPIKEY");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.sms.ir/v1/credit", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/credit',
  headers: {
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
  CURLOPT_URL => 'https://api.sms.ir/v1/credit',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
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
  'X-API-KEY': 'YOURAPIKEY'
}
conn.request("GET", "/v1/credit", payload, headers)
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
  .url("https://api.sms.ir/v1/credit")
  .method("GET", body)
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](../07-sdks/README.md#جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

---

[بازگشت به فهرست مطالب](../README.md)
