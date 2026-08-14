# 4.6. گزارش تازه‌ترین پیامک‌های دریافتی

شما می‌توانید با استفاده از این متد، تازه‌ترین پیامک‌های دریافتی را مشاهده نمایید. لازم به ذکر است هر پیامک دریافتی تنها یک مرتبه توسط این متد قابل دستیابی می‌باشد و پس از آن به دلیل قرار گرفتن در حالت خوانده شده قابل دسترسی مجدد توسط این متد نمی‌باشند.

**URL:** <https://api.sms.ir/v1/receive/latest>

**Request Method:** GET

## 4.6.1. پارامترهای درخواست

| مشخصه | ارسال   | نوع     | توضیح                                                            |
| ----- | ------- | ------- | ---------------------------------------------------------------- |
| Count | اختیاری | Integer | تعداد درخواستی (حداکثر تعداد درخواستی و مقدار پیش‌فرض 100 می‌باشد) |

**Request:** <https://api.sms.ir/v1/receive/latest?count=50>

## 4.6.2. مدل دیتای بازگشتی (آرایه‌ای از مدل زیر)

| مشخصه            | نوع                | توضیح                     |
| ---------------- | ------------------ | ------------------------- |
| ReceiveReturnId  | Long               | شناسه یکتای پیامک دریافتی |
| MessageText      | String             | متن پیامک                 |
| Number           | Long               | شماره خط دریافت‌کننده      |
| Mobile           | Long               | شماره موبایل ارسال کننده  |
| ReceivedDateTime | Integer (UnixTime) | زمان دریافت               |

**Response Body:**

```JSON
{
    "status": 1,
    "message": "موفق",
    "data": [
        {
            "receiveReturnId": 123456789,
            "messageText": "HyperBox.irفروشگاه اینترنتی اسباب بازی و عروسک",
            "number": 30004505000017,
            "mobile": 912xxxx002,
            "receivedDateTime": 1628683625
        }
    ]
}
```

## 4.6.3. نمونه کد

**C#:**

```C#
HttpClient httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("x-api-key", "YOURAPIKEY");
var response = await httpClient.GetAsync("https://api.sms.ir/v1/receive/latest?count=100");
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

fetch("https://api.sms.ir/v1/receive/latest?count=100", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Node.js:**

```Node.js
var config = {
  method: 'get',
  url: 'https://api.sms.ir/v1/receive/latest?count=100',
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
  CURLOPT_URL => 'https://api.sms.ir/v1/receive/latest?count=100',
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
conn.request("GET", "/v1/receive/latest?count=100", payload, headers)
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
  .url("https://api.sms.ir/v1/receive/latest?count=100")
  .method("GET", body)
  .addHeader("X-API-KEY", "YOURAPIKEY")
  .build();
Response response = client.newCall(request).execute();
```

> **معادل در SDKهای رسمی:** برای مشاهده نام متد معادل این عملیات در پکیج‌های Node.js، PHP، TypeScript، ‎.NET و Python، به [بخش ۷.۳](../07-sdks/README.md#جدول-تناظر-متدهای-api-با-متدهای-هر-sdk) مراجعه کنید.

---

[بازگشت به فهرست مطالب](../README.md)
